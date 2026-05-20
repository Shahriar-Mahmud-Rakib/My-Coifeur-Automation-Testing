#!/usr/bin/env python3
"""run.py — single command to run Mehad Autonomous AI Testing.

Auto-runs install.py the first time if anything is missing.
Always opens a real browser window so you SEE what's happening.

Usage:
    python run.py            # demo: TestQA01Functional with visible browser (~3 min)
    python run.py --ai       # full AI Test Agent v5 — auto-generates from md specs
    python run.py --all      # every QA agent — full suite, ~30 min
    python run.py --headless # same as default but no visible browser
    python run.py --url X    # override BASE_URL (default: dev.mehadedu.com/en)
"""

from __future__ import annotations
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()


def needs_install() -> bool:
    """True when at least one critical dep is missing."""
    try:
        import playwright  # noqa
        import pytest  # noqa
    except ImportError:
        return True
    if shutil.which("ollama") is None:
        return True
    return False


def parse_args(argv: list[str]) -> dict:
    out = {"mode": "demo", "headed": True, "url": None}
    for a in argv:
        if a == "--ai":
            out["mode"] = "ai"
        elif a == "--all":
            out["mode"] = "all"
        elif a == "--admin":
            out["mode"] = "admin"
        elif a == "--headless":
            out["headed"] = False
        elif a.startswith("--url="):
            out["url"] = a.split("=", 1)[1]
        elif a == "--url":
            pass  # next arg
        elif a in ("-h", "--help", "help"):
            print(__doc__)
            sys.exit(0)
    # Handle --url X (space form)
    for i, a in enumerate(argv):
        if a == "--url" and i + 1 < len(argv):
            out["url"] = argv[i + 1]
    return out


def ensure_ollama_serving() -> None:
    """Start ollama serve in background if it isn't already responding."""
    if os.getenv("OLLAMA_NO_GPU") == "true":
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        os.environ["GGML_VK_VISIBLE_DEVICES"] = "-1"
    try:
        subprocess.check_output(["ollama", "list"], stderr=subprocess.DEVNULL, timeout=4)
        return
    except Exception:
        pass
    print("→ Starting ollama serve in background...")
    subprocess.Popen(["ollama", "serve"], env=os.environ,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Brief wait so the agent's first call doesn't fail
    import time
    for _ in range(10):
        time.sleep(1)
        try:
            subprocess.check_output(["ollama", "list"], timeout=3)
            print("  ✓ ollama serve responding")
            return
        except Exception:
            continue
    print("  ⚠ ollama serve didn't respond in 10s — agent may use fallbacks")


def run_demo(env: dict) -> int:
    """Visible-browser demo: Smoke tests across all specs. ~10 tests, ~2 min."""
    print("=" * 64)
    print("DEMO MODE — Smoke tests with visible browser")
    print(f"Target: {env.get('BASE_URL')}")
    print("=" * 64)
    cmd = [sys.executable, "-m", "pytest",
           "tests", "-k", "smoke",
           "--browser=chromium",
           "--tb=short", "-v", "--timeout=90",
           "-p", "no:cacheprovider"]
    if env.get("HEADED") == "1":
        cmd.append("--headed")
    return subprocess.call(cmd, env=env)


def run_ai(env: dict) -> int:
    """AI Test Agent v5: auto-generates tests for every spec, runs them.
    The agent itself spawns Playwright; the HEADED env var makes the
    spawned browser visible so you can watch the generated tests run."""
    print("=" * 64)
    print("AI MODE — AI Test Agent v5 (auto-generation + auto-run)")
    print(f"Target: {env.get('BASE_URL')}")
    print(f"Model:  {env.get('AI_MODEL', 'qwen2.5-coder:1.5b')}")
    print("=" * 64)
    cmd = [sys.executable, "-m", "ai_engine.agent"]
    return subprocess.call(cmd, env=env)


def run_all(env: dict) -> int:
    """Run all tests in tests/. ~50+ tests, ~10 min."""
    print("=" * 64)
    print("FULL MODE — Running all generated tests in tests/")
    print(f"Target: {env.get('BASE_URL')}")
    print("=" * 64)
    cmd = [sys.executable, "-m", "pytest",
           "tests",
           "--browser=chromium",
           "--tb=short", "-v", "--timeout=90",
           "--html=reports/report.html", "--self-contained-html",
           "-p", "no:cacheprovider"]
    if env.get("HEADED") == "1":
        cmd.append("--headed")
    return subprocess.call(cmd, env=env)


def run_admin(env: dict) -> int:
    """Run all admin tests in tests/. ~11 files, ~297+ unique tests.
    Generates the rich dark-theme bug report using reporter.py."""
    base_url = env.get("BASE_URL", "https://dev.mycoifeur.com.sa")
    model    = env.get("AI_MODEL", "qwen2.5-coder:1.5b")
    print("=" * 64)
    print("ADMIN MODE — Running all Admin tests in tests/")
    print(f"Target: {base_url}")
    print("=" * 64)
    cmd = [sys.executable, "-m", "pytest",
           "tests", "-k", "admin",
           "--browser=chromium",
           "--tb=short", "-v", "--timeout=90",
           "-p", "no:cacheprovider"]
    if env.get("HEADED") == "1":
        cmd.append("--headed")
    rc = subprocess.call(cmd, env=env)

    # ── Generate rich dark-theme bug report ────────────────────────────────
    _build_rich_report(base_url, model)
    return rc


def _build_rich_report(base_url: str, model: str) -> None:
    """Post-process test_results.json → reporter.py → bug-report.html."""
    import json as _json

    results_path = ROOT / "reports" / "test_results.json"
    if not results_path.exists():
        print("[WARN] No test_results.json found -- skipping rich report generation")
        return

    try:
        outcomes = _json.loads(results_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[WARN] Could not parse test_results.json: {e}")
        return

    # Load screenshot index for embedding PoC images
    shot_index = {}
    shot_idx_path = ROOT / "reports" / "screenshots" / "_index.json"
    if shot_idx_path.exists():
        try:
            shot_index = _json.loads(shot_idx_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # Load evidence index
    ev_index = {}
    ev_idx_path = ROOT / "reports" / "evidence"
    if ev_idx_path.exists():
        for ev_file in ev_idx_path.glob("*.json"):
            if ev_file.name == "_index.json":
                continue
            try:
                ev_data = _json.loads(ev_file.read_text(encoding="utf-8"))
                ev_index[ev_file.stem] = ev_data
            except Exception:
                pass

    # Group outcomes by test file → spec_name
    from collections import defaultdict
    by_spec = defaultdict(lambda: {"passed_tests": [], "bugs": [],
                                    "passed": 0, "failed": 0, "total": 0,
                                    "status": "passed", "gaps": ""})

    for t in outcomes:
        filepath = t.get("filepath", "")
        # Extract spec name from filepath: tests/test_admin_bookings.py → admin_bookings
        import re as _re
        stem = filepath.split("/")[-1].replace(".py", "")
        spec_name = _re.sub(r"^test_", "", stem)

        by_spec[spec_name]["total"] += 1

        if t["outcome"] == "passed":
            by_spec[spec_name]["passed"] += 1
            by_spec[spec_name]["passed_tests"].append({
                "name":      t["fn_name"],
                "docstring": t.get("docstring", ""),
                "params":    t.get("params", ""),
                "duration":  t.get("duration", 0.0),
            })
        elif t["outcome"] == "failed":
            by_spec[spec_name]["failed"] += 1
            by_spec[spec_name]["status"] = "failed"

            # Build a bug ticket for each failure
            nodeid = t.get("nodeid", "")
            shot_data = shot_index.get(nodeid, {})
            shot_path = shot_data.get("path", "")

            # Try to embed screenshot as base64
            shot_b64 = ""
            if shot_path:
                import base64
                abs_shot = ROOT / shot_path
                if abs_shot.exists():
                    try:
                        raw = abs_shot.read_bytes()
                        shot_b64 = "data:image/png;base64," + base64.b64encode(raw).decode()
                    except Exception:
                        pass

            # Load evidence for this test
            safe_nodeid = _re.sub(r"[^\w\-]", "_", nodeid)[:120]
            ev_data = {}
            ev_file = ROOT / "reports" / "evidence" / f"{safe_nodeid}.json"
            if ev_file.exists():
                try:
                    ev_data = _json.loads(ev_file.read_text(encoding="utf-8"))
                except Exception:
                    pass

            # Video PoC path
            video_path = ""
            video_idx_path = ROOT / "reports" / "videos" / "_index.json"
            if video_idx_path.exists():
                try:
                    video_idx = _json.loads(video_idx_path.read_text(encoding="utf-8"))
                    video_path = video_idx.get(nodeid, "")
                except Exception:
                    pass

            bug_id = f"BUG-ADMIN-{len(by_spec[spec_name]['bugs']) + 1:03d}"
            by_spec[spec_name]["bugs"].append({
                "id":           bug_id,
                "severity":     "HIGH" if "security" in t["fn_name"] else "MEDIUM",
                "priority":     "P1" if "security" in t["fn_name"] else "P2",
                "title":        t.get("error_msg", "Test failed") or "Test failed",
                "test_name":    t["fn_name"],
                "page_url":     base_url,
                "timestamp":    "",
                "duration":     f"{t.get('duration', 0):.2f}s",
                "description":  t.get("docstring", ""),
                "steps":        [f"Run test: {t['fn_name']}"],
                "expected":     "Test should pass without errors",
                "actual":       t.get("error_msg", "Test failed"),
                "root_cause":   "",
                "suggested_fix": "",
                "error_message": t.get("error_msg", ""),
                "traceback":    t.get("traceback", ""),
                "screenshot_b64": shot_b64,
                "video_path":   video_path,
                "test_data":    t.get("params", ""),
                "performance":  ev_data.get("performance", {}),
                "error_log":    ev_data.get("errors", []),
                "network_log":  ev_data.get("network", []),
            })
        elif t["outcome"] == "skipped":
            by_spec[spec_name]["passed"] += 1  # count skips as non-failures

    # Now generate the rich report
    try:
        sys.path.insert(0, str(ROOT))
        from ai_engine.reporter import generate_report
        out = generate_report(
            all_results=dict(by_spec),
            base_url=base_url,
            model=model,
            output_filename="bug-report.html",
        )
        print()
        print("=" * 64)
        print(f"[OK] Rich bug report generated: {out}")
        print(f"     Open in browser: file:///{out.resolve()}")
        print("=" * 64)
    except Exception as e:
        print(f"[WARN] Rich report generation failed: {e}")
        import traceback
        traceback.print_exc()


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if needs_install():
        print("First run detected — running installer...\n")
        rc = subprocess.call([sys.executable, str(ROOT / "install.py")])
        if rc != 0:
            return rc
        print()

    ensure_ollama_serving()

    env = os.environ.copy()
    env.setdefault("BASE_URL", args["url"] or "https://dev.mycoifeur.com.sa")
    if args["url"]:
        env["BASE_URL"] = args["url"]
    env["HEADED"] = "1" if args["headed"] else "0"
    # Default to the small first-run model
    env.setdefault("AI_MODEL", "qwen2.5-coder:1.5b")

    if args["mode"] == "ai":
        return run_ai(env)
    if args["mode"] == "all":
        return run_all(env)
    if args["mode"] == "admin":
        return run_admin(env)
    return run_demo(env)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
