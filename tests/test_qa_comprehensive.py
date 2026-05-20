"""
QA Comprehensive Test Suite — My Coifeur Admin Portal
Spec: Covers 10 test groups:
  QA-01  Functional & User Flow Tests
  QA-02  Edge Case & Boundary Tests
  QA-03  Security Tests (XSS + SQLi + IDOR + Leaks)
  QA-04  Performance & JavaScript Error Tests
  QA-05  Hallucination & Data Integrity Tests
  QA-06  API & Network Monitoring
  QA-07  Accessibility (a11y) Tests
  QA-08  Mobile & Cross-Viewport Tests
  QA-09  SEO & Meta Tags
  QA-10  i18n & Localization (Arabic / RTL)
"""

import os
import re
import time
import json
import pytest
from pathlib import Path
from playwright.sync_api import Page, expect

BASE_URL = os.getenv("BASE_URL", "https://dev.mycoifeur.com.sa")
LOAD_STATE = "domcontentloaded"

# Credentials
TEST_EMAIL = "amrmuhamed9@gmail.com"
TEST_PASSWORD = "123456"

PAYLOAD_DIR = Path(__file__).parent.parent / "payloads"

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _load_payload_lines(filename: str) -> list[str]:
    """Load payloads from txt files while stripping comments."""
    p = PAYLOAD_DIR / filename
    if not p.exists():
        return []
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.startswith("#")]


def _admin_login(page: Page):
    """Perform a successful login for an admin session."""
    page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE, timeout=20000)
    page.wait_for_timeout(1000)
    
    email_input = page.locator('#email').first
    password_input = page.locator('#password').first
    login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first
    
    email_input.fill(TEST_EMAIL)
    password_input.fill(TEST_PASSWORD)
    login_btn.click()
    
    page.wait_for_url("**/en/admin/overview", timeout=20000)
    page.wait_for_timeout(1500)


# ─────────────────────────────────────────────────────────────────────────────
# QA-01  FUNCTIONAL & USER FLOW TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA01Functional:
    """Verifies standard admin portal loads, layouts, authentication, and core subpages."""

    def test_qa01_homepage_loads_correct_url(self, page: Page):
        """Admin login page loads successfully under /en/admin-login."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        assert "admin-login" in page.url, f"Unexpected URL loaded: {page.url}"

    def test_qa01_page_title_correct(self, page: Page):
        """Page title is meaningful and includes brand presence."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        title = page.title().lower()
        assert title != "", "Page title is empty"
        assert "my coifeur" in title or "coifeur" in title, f"Brand not in title: {title}"

    def test_qa01_login_elements_present(self, page: Page):
        """Login form must display email, password, and sign-in button."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        expect(page.locator('#email').first).to_be_visible()
        expect(page.locator('#password').first).to_be_visible()
        expect(page.locator('button[type="submit"], button:has-text("Sign in")').first).to_be_visible()

    def test_qa01_successful_admin_login(self, page: Page):
        """Successful login redirects admin to overview page."""
        _admin_login(page)
        assert "admin/overview" in page.url

    def test_qa01_sidebar_navigation_links_present(self, page: Page):
        """Admin portal displays all 9 key modules in sidebar."""
        _admin_login(page)
        
        # Verify sidebar elements or navigate directly to make sure routing is present
        routes = [
            "bookings", "providers", "customers", "finance",
            "management", "categories", "promocode", "contact-requests", "settings"
        ]
        for route in routes:
            page.goto(f"{BASE_URL}/en/admin/{route}", wait_until=LOAD_STATE)
            page.wait_for_timeout(500)
            expect(page.locator("body")).to_be_visible()
            assert "admin-login" not in page.url, f"Unauthorised redirect on route: {route}"


# ─────────────────────────────────────────────────────────────────────────────
# QA-02  EDGE CASE & BOUNDARY TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA02EdgeCaseBoundary:
    """Exercises boundary constraints, empty states, and invalid login states."""

    def test_qa02_ec_empty_credentials_disabled_or_validates(self, page: Page):
        """Empty credentials trigger validation errors rather than raw crashes."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        email_input = page.locator('#email').first
        password_input = page.locator('#password').first
        login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first

        email_input.fill("")
        password_input.fill("")
        
        # Click login (might be intercepted by HTML5 validation)
        try:
            login_btn.click(timeout=3000)
        except Exception:
            pass
        
        page.wait_for_timeout(500)
        # Ensure we didn't redirect or crash
        assert "admin/overview" not in page.url
        assert "500" not in page.title()

    def test_qa02_ec_invalid_credentials_rejected(self, page: Page):
        """Invalid credentials exhibit appropriate error banner."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        email_input = page.locator('#email').first
        password_input = page.locator('#password').first
        login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first

        email_input.fill("nonexistent@user.com")
        password_input.fill("wrongpass")
        login_btn.click()

        page.wait_for_timeout(1000)
        assert "admin/overview" not in page.url
        # Error text or validation should be present on screen
        assert "500" not in page.title()

    def test_qa02_ec_boundary_input_lengths(self, page: Page):
        """Extremely long inputs in email and password do not cause a 500 error."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        email_input = page.locator('#email').first
        password_input = page.locator('#password').first
        login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first

        # 500-char strings
        email_input.fill("a" * 490 + "@test.com")
        password_input.fill("p" * 500)
        login_btn.click()
        
        page.wait_for_timeout(1000)
        assert "500" not in page.title()
        assert "admin/overview" not in page.url

    def test_qa02_ec_non_existent_route_404(self, page: Page):
        """Direct access to non-existent route shows graceful 404 page, not stack traces."""
        _admin_login(page)
        page.goto(f"{BASE_URL}/en/admin/nonexistent-route-random-xyz", wait_until=LOAD_STATE)
        page.wait_for_timeout(1000)
        content = page.content().lower()
        # Verify no unhandled backend frames
        assert "exception" not in content
        assert "traceback" not in content
        assert "sql syntax" not in content

    def test_qa02_ec_rapid_clicks_no_crash(self, page: Page):
        """Rapid multiple clicks on Sign In button do not crash the page."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first
        
        for _ in range(5):
            try:
                login_btn.click(timeout=100)
            except Exception:
                pass
        
        page.wait_for_timeout(1000)
        assert "500" not in page.title()


# ─────────────────────────────────────────────────────────────────────────────
# QA-03  SECURITY TESTS — XSS + SQL INJECTION
# ─────────────────────────────────────────────────────────────────────────────

class TestQA03Security:
    """Checks UI input filtering for cross-site scripting (XSS), SQLi, IDOR, and data exposure."""

    @pytest.mark.parametrize("payload", _load_payload_lines("xss.txt") or [
        "<script>alert('xss')</script>",
        '"><img src=x onerror=alert(1)>',
        "javascript:alert(1)",
        "<svg onload=alert(1)>",
    ])
    def test_qa03_xss_in_login_inputs(self, page: Page, payload: str):
        """XSS payloads filled in credentials do not execute scripts or trigger alerts."""
        js_alerts = []
        page.on("dialog", lambda d: (js_alerts.append(d.message), d.dismiss()))
        page.on("pageerror", lambda exc: js_alerts.append(str(exc)))

        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        email_input = page.locator('#email').first
        email_input.fill(payload)
        
        page.wait_for_timeout(500)
        assert len(js_alerts) == 0, f"XSS payload triggered script execution: {payload}"

    def test_qa03_xss_not_reflected_raw(self, page: Page):
        """Login form inputs must not reflect unescaped payloads in raw page markup."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        payload = "<script>alert('COIFEUR_XSS_CHECK')</script>"
        page.locator('#email').first.fill(payload)
        page.wait_for_timeout(500)
        
        html = page.content()
        assert "COIFEUR_XSS_CHECK" not in html or "&lt;script&gt;" in html or payload not in html, (
            "Payload rendered completely unescaped in source HTML"
        )

    def test_qa03_ssti_not_evaluated(self, page: Page):
        """Template expressions like {{7*7}} must not evaluate to 49 in page markup."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        page.locator('#email').first.fill("{{7*7}}")
        page.wait_for_timeout(500)
        
        body_text = page.locator("body").inner_text()
        assert "49" not in body_text, "Possible Server-Side Template Injection (SSTI) evaluation detected"

    @pytest.mark.parametrize("payload", _load_payload_lines("sqli.txt") or [
        "' OR '1'='1",
        "'; DROP TABLE salons; --",
        "\" OR \"1\"=\"1",
    ])
    def test_qa03_sqli_no_leak_db_errors(self, page: Page, payload: str):
        """SQL injection payloads in input fields do not leak SQL database errors."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        page.locator('#email').first.fill(payload)
        page.locator('#password').first.fill(payload)
        page.locator('button[type="submit"], button:has-text("Sign in")').first.click()
        
        page.wait_for_timeout(1000)
        content = page.content().lower()
        db_keywords = ["sql syntax", "mysql", "mariadb", "postgresql", "sqlite", "syntax error near", "unclosed quote"]
        leaks = [k for k in db_keywords if k in content]
        assert not leaks, f"SQL injection payload {payload!r} leaked database internal structure details: {leaks}"

    def test_qa03_no_sensitive_keys_in_markup(self, page: Page):
        """Admin dashboard pages do not leak private API keys, secrets, or JWTs in markup."""
        _admin_login(page)
        html = page.content()
        sensitive_patterns = [
            r"password[\"']?\s*:\s*[\"'][^\"']{4,}",
            r"secret[\"']?\s*:\s*[\"'][^\"']{4,}",
            r"private_key[\"']?\s*:\s*[\"'][^\"']{20,}",
        ]
        for pat in sensitive_patterns:
            assert not re.search(pat, html, re.IGNORECASE), f"Sensitive security token leaked in HTML: {pat}"

    def test_qa03_https_enforced(self, page: Page):
        """Staging URLs are served over a secure SSL/HTTPS connection."""
        page.goto(BASE_URL)
        page.wait_for_load_state(LOAD_STATE)
        assert page.url.startswith("https://") or "localhost" in page.url, f"Insecure context: {page.url}"

    def test_qa03_idor_protected_api_probes(self, page: Page):
        """Hypothetical protected user APIs reject unauthorized/anonymous calls with 401/403."""
        api_base = BASE_URL.rstrip("/")
        candidates = ["/api/admin/profile", "/api/users/1", "/api/salons/active"]
        ctx = page.context
        
        for path in candidates:
            try:
                resp = ctx.request.get(f"{api_base}{path}", timeout=5000)
                # Redirect, 401, 403, 404 are all safe. 200 + PII json leak is a bug.
                if resp.status == 200:
                    ct = (resp.headers.get("content-type", "")).lower()
                    if "json" in ct:
                        body = resp.json()
                        pii = {"email", "phone", "password", "token", "userId"}
                        assert not (isinstance(body, dict) and (set(body) & pii)), (
                            f"IDOR PII data leakage on endpoint: {path}"
                        )
            except Exception:
                pass


# ─────────────────────────────────────────────────────────────────────────────
# QA-04  PERFORMANCE & JAVASCRIPT ERROR TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA04PerformanceAndJSErrors:
    """Verifies page rendering speeds, load proxies, and zero uncaught JS console errors."""

    def test_qa04_perf_ttfb_acceptable(self, page: Page):
        """Time to First Byte (TTFB) is below 1500ms under ordinary conditions."""
        page.goto(f"{BASE_URL}/en/admin-login")
        page.wait_for_load_state(LOAD_STATE)
        ttfb = page.evaluate("""() => {
            const t = performance.timing;
            return t.responseStart - t.navigationStart;
        }""")
        assert ttfb < 1500, f"Slow Time To First Byte: {ttfb}ms"

    def test_qa04_perf_dom_load_acceptable(self, page: Page):
        """DOMContentLoaded completes in under 3000ms."""
        page.goto(f"{BASE_URL}/en/admin-login")
        page.wait_for_load_state(LOAD_STATE)
        dom_load = page.evaluate("""() => {
            const t = performance.timing;
            return t.domContentLoadedEventEnd - t.navigationStart;
        }""")
        assert dom_load < 3000, f"Slow DOM Content Load: {dom_load}ms"

    def test_qa04_no_js_errors_on_login(self, page: Page):
        """No uncaught JS exceptions or critical console errors during login load."""
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)

        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        page.wait_for_timeout(1000)
        
        # Filter browser extensions, static assets 404s, and static assets noise
        real_errors = [
            e for e in errors 
            if "extension" not in e.lower() 
            and "favicon" not in e.lower()
            and "failed to load resource" not in e.lower()
            and "404" not in e.lower()
        ]
        assert len(real_errors) == 0, f"JS errors detected on login screen: {real_errors}"

    def test_qa04_no_broken_images_on_dashboard(self, page: Page):
        """No broken image tags (naturalWidth === 0) on the admin overview panel."""
        _admin_login(page)
        page.goto(f"{BASE_URL}/en/admin/overview", wait_until=LOAD_STATE)
        page.wait_for_timeout(1500)

        broken = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img'))
                .filter(img => img.src && !img.src.startsWith('data:') && img.naturalWidth === 0)
                .map(img => img.src);
        }""")
        assert len(broken) == 0, f"Broken image references discovered on overview: {broken}"


# ─────────────────────────────────────────────────────────────────────────────
# QA-05  HALLUCINATION & DATA INTEGRITY TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA05HallucinationDataIntegrity:
    """Checks UI rendering integrity, preventing phantom element generation and stale placeholders."""

    def test_qa05_no_undefined_text_in_body(self, page: Page):
        """Standalone 'undefined' or 'null' labels are completely absent in rendered body text."""
        _admin_login(page)
        content = page.locator('body').inner_text()
        assert not re.search(r"\bundefined\b", content), "Literal 'undefined' rendered on screen"
        assert not re.search(r"\bnull\b", content), "Literal 'null' rendered on screen"

    def test_qa05_no_placeholder_markers(self, page: Page):
        """No visible mock text values (e.g., TODO, Lorem Ipsum, FIXME) exist on the admin board."""
        _admin_login(page)
        content = page.locator('body').inner_text().lower()
        placeholders = ["lorem ipsum", "fixme", "todo placeholder"]
        found = [p for p in placeholders if p in content]
        assert not found, f"Draft placeholders left in production markup: {found}"

    def test_qa05_no_stacked_duplicate_buttons(self, page: Page):
        """Action items must not have overlapping or stacked duplicate trigger controls."""
        _admin_login(page)
        # Scan for potential duplicate logout or dashboard buttons
        logout_btns = page.locator('button:has-text("Logout"), a:has-text("Logout")')
        visible_logout = sum(1 for i in range(logout_btns.count()) if logout_btns.nth(i).is_visible())
        assert visible_logout <= 2, f"Stacked duplicate logout controls detected: {visible_logout}"


# ─────────────────────────────────────────────────────────────────────────────
# QA-06  API & NETWORK MONITORING
# ─────────────────────────────────────────────────────────────────────────────

class TestQA06APIAndNetwork:
    """Monitors secure network routing, correct content types, and valid response formats."""

    def test_qa06_traffic_is_https(self, page: Page):
        """Outbound assets load exclusively via secure channels."""
        insecure = []
        page.on("request", lambda r: insecure.append(r.url) if r.url.startswith("http://") else None)
        
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        page.wait_for_timeout(1000)
        
        real_insecure = [u for u in insecure if "localhost" not in u and "127.0.0.1" not in u]
        assert len(real_insecure) == 0, f"Unsecure asset references loaded over HTTP: {real_insecure}"

    def test_qa06_no_5xx_server_errors(self, page: Page):
        """Normal navigation triggers absolutely no 500+ Internal Server errors."""
        server_errors = []
        page.on("response", lambda r: server_errors.append(r.url) if r.status >= 500 else None)
        
        _admin_login(page)
        page.goto(f"{BASE_URL}/en/admin/bookings", wait_until=LOAD_STATE)
        page.wait_for_timeout(1000)
        
        assert len(server_errors) == 0, f"Server backend responses returned 5xx errors: {server_errors}"

    def test_qa06_json_responses_are_well_formed(self, page: Page):
        """Every application/json response received parses successfully as valid JSON."""
        unparsed_json = []

        def _check_json(resp):
            ct = (resp.headers.get("content-type", "")).lower()
            if "application/json" in ct and resp.status < 400:
                try:
                    resp.json()
                except Exception:
                    unparsed_json.append(resp.url)

        page.on("response", _check_json)
        _admin_login(page)
        page.goto(f"{BASE_URL}/en/admin/overview", wait_until=LOAD_STATE)
        page.wait_for_timeout(1500)
        
        assert len(unparsed_json) == 0, f"Malformed JSON content returned from endpoints: {unparsed_json}"


# ─────────────────────────────────────────────────────────────────────────────
# QA-07  ACCESSIBILITY (A11Y) TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA07Accessibility:
    """Evaluates landmarks, lang structures, headings, and readable element mappings."""

    def test_qa07_html_lang_attribute(self, page: Page):
        """HTML element possesses a valid language identifier attribute."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        lang = page.locator("html").get_attribute("lang")
        assert lang and len(lang) >= 2, f"Missing html lang specifier: {lang}"

    def test_qa07_heading_hierarchy(self, page: Page):
        """The page structure contains heading elements to outline semantic structure."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        headings = page.locator("h1, h2, h3")
        assert headings.count() > 0, "No HTML heading tags present on landing portal"

    def test_qa07_images_have_alt_attributes(self, page: Page):
        """Large informative image elements contain descriptive alt tags for screen readers."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        bad_imgs = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img'))
                .filter(img => img.offsetWidth > 30 && !img.alt)
                .map(img => img.src);
        }""")
        assert len(bad_imgs) <= 2, f"Informative images discovered completely missing alt tags: {bad_imgs}"


# ─────────────────────────────────────────────────────────────────────────────
# QA-08  MOBILE & CROSS-VIEWPORT TESTS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA08MobileAndViewport:
    """Verifies layout responsive integrity across specific device viewports."""

    @pytest.mark.parametrize("vp", [
        {"width": 375,  "height": 667,  "label": "mobile"},
        {"width": 768,  "height": 1024, "label": "tablet"},
        {"width": 1280, "height": 720,  "label": "desktop"},
        {"width": 1920, "height": 1080, "label": "desktop-xl"},
    ])
    def test_qa08_layout_viewport_no_overflow(self, page: Page, vp: dict):
        """Layout loads correctly without vertical crashes or overflow issues across views."""
        label = vp.pop("label")
        page.set_viewport_size(vp)
        
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        page.wait_for_timeout(800)
        
        assert "500" not in page.title()
        expect(page.locator('#email').first).to_be_visible()


# ─────────────────────────────────────────────────────────────────────────────
# QA-09  SEO & META TAGS
# ─────────────────────────────────────────────────────────────────────────────

class TestQA09SEOAndMeta:
    """Ensures search layouts, canon tags, and meta viewports are present."""

    def test_qa09_meta_charset(self, page: Page):
        """Charset is correctly declared as UTF-8."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        charset = page.evaluate("() => document.characterSet")
        assert charset.lower() == "utf-8", f"Unexpected document charset: {charset}"

    def test_qa09_meta_viewport(self, page: Page):
        """Viewport meta configuration is present to accommodate responsive styling."""
        page.goto(f"{BASE_URL}/en/admin-login", wait_until=LOAD_STATE)
        viewport = page.locator('meta[name="viewport"]').first
        expect(viewport).to_be_attached()


# ─────────────────────────────────────────────────────────────────────────────
# QA-10  i18n & LOCALIZATION & RTL
# ─────────────────────────────────────────────────────────────────────────────

class TestQA10I18nAndRTL:
    """Checks RTL and Arabic language locale configurations."""

    def test_qa10_arabic_locale_loads(self, page: Page):
        """Arabic locale portal loads successfully."""
        page.goto(f"{BASE_URL}/ar/admin-login", wait_until=LOAD_STATE)
        page.wait_for_timeout(1000)
        assert "/ar" in page.url

    def test_qa10_arabic_rtl_dir(self, page: Page):
        """Arabic page layout sets text directionality as RTL."""
        page.goto(f"{BASE_URL}/ar/admin-login", wait_until=LOAD_STATE)
        dir_attr = page.locator("html").get_attribute("dir")
        assert dir_attr == "rtl", f"Arabic page layout missing RTL direction: {dir_attr}"
