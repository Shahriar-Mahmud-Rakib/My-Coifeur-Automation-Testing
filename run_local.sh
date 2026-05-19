#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
#  Mehad Autonomous AI Testing — Local Browser Runner
#  Runs tests in a VISIBLE browser so you can watch every action live.
#
#  Usage:
#    ./run_local.sh                    # run ALL tests, browser visible
#    ./run_local.sh qa01               # QA-01 Functional tests only
#    ./run_local.sh qa02               # QA-02 Edge & Boundary tests
#    ./run_local.sh qa03               # QA-03 Security (XSS + SQLi)
#    ./run_local.sh qa04               # QA-04 Performance & JS errors
#    ./run_local.sh qa05               # QA-05 Hallucination & Data integrity
#    ./run_local.sh login              # Legacy login tests
#    ./run_local.sh reset              # Legacy reset-password tests
#    ./run_local.sh fast               # All tests, faster (no slow_mo)
#
#  Environment overrides:
#    BASE_URL=https://dev.mehadedu.com/en ./run_local.sh
#    SLOW_MO=1200 ./run_local.sh          # even slower for demos
#    SLOW_MO=0    ./run_local.sh fast     # headless-speed but still headed
# ─────────────────────────────────────────────────────────────────────────────

set -e

# ── Defaults ─────────────────────────────────────────────────────────────────
BASE_URL="${BASE_URL:-https://dev.mycoifeur.com.sa}"
SLOW_MO="${SLOW_MO:-800}"          # ms between each Playwright action
HEADED=1                           # always open browser window

# ── Colours ──────────────────────────────────────────────────────────────────
TEAL='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'; GREEN='\033[0;32m'

echo ""
echo -e "${BOLD}${TEAL}  My Coifeur Autonomous AI Testing — Local Browser Runner${RESET}"
echo -e "  Target  : ${GREEN}${BASE_URL}${RESET}"
echo -e "  Slow Mo : ${SLOW_MO}ms between actions"
echo ""

# ── Test selection ────────────────────────────────────────────────────────────
ARG="${1:-all}"
case "$ARG" in
  smoke)
    FILTER="tests/test_e2e_master_journey.py -k smoke"
    LABEL="My Coifeur Smoke Tests"
    ;;
  journey)
    FILTER="tests/test_e2e_master_journey.py -k complete_cross_role"
    LABEL="My Coifeur E2E Master Cross-Role Journey"
    ;;
  fast)
    SLOW_MO=0
    FILTER="tests/test_e2e_master_journey.py"
    LABEL="My Coifeur E2E Tests (fast headed)"
    ;;
  all|*)
    FILTER="tests/test_e2e_master_journey.py"
    LABEL="My Coifeur Complete E2E QA Test Suite"
    ;;
esac

echo -e "  Running : ${BOLD}${LABEL}${RESET}"
echo ""

# ── Run ───────────────────────────────────────────────────────────────────────
HEADED=$HEADED \
SLOW_MO=$SLOW_MO \
BASE_URL=$BASE_URL \
python3 -m pytest \
  $FILTER \
  --headed \
  --timeout=90 \
  --timeout-method=thread \
  --tb=short \
  -v \
  --html=reports/report.html --self-contained-html \
  -p no:warnings
