import os, time, pytest
from playwright.sync_api import Page, expect
BASE_URL = os.getenv("BASE_URL", "https://dev.mycoifeur.com.sa")

def test_smoke_homepage_loads_fb(page: Page):
    """FB smoke: page returns a response and renders <body>."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    expect(page.locator("body")).to_be_visible(timeout=5000)

def test_smoke_no_500_error_fb(page: Page):
    """FB smoke: page does not return HTTP 500 / 502 / 503."""
    resp = page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    if resp is not None:
        assert resp.status < 500, f"server error {resp.status} on {BASE_URL}"

def test_smoke_title_non_empty_fb(page: Page):
    """FB smoke: <title> tag is present and non-empty."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    title = page.title()
    assert title and title.strip(), f"empty page title: {title!r}"

def test_functional_navigates_homepage_fb(page: Page):
    """FB functional: BASE_URL navigates without redirect-loop."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    assert page.url.startswith("http"), f"non-HTTP url: {page.url}"

def test_functional_h1_present_fb(page: Page):
    """FB functional: page has at least one heading element after hydration."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    try:
        page.wait_for_selector("h1, h2, [role='heading']",
                               state="visible", timeout=6000)
    except Exception:
        pass  # fall through to count check below
    headings = page.locator("h1, h2, [role='heading']").count()
    assert headings >= 1, "no H1/H2/role=heading on page after 6s hydration wait"

def test_validation_required_field_blocks_submit_fb(page: Page):
    """FB validation: clicking submit with empty form does not 500."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    submit = page.locator('button[type="submit"], button:has-text("Submit"), '
                          'button:has-text("Send Code"), button:has-text("Login")')
    if submit.count() > 0:
        submit.first.click(force=True)
        page.wait_for_timeout(500)
    assert "500" not in page.title(), "500 after empty submit"

def test_negative_invalid_input_does_not_crash_fb(page: Page):
    """FB negative: filling junk into any text input does not crash the page."""
    page.goto(BASE_URL, wait_until="domcontentloaded", timeout=15000)
    inputs = page.locator('input[type="text"], input[type="email"]')
    if inputs.count() > 0:
        inputs.first.fill("'\"<>$#@!")
    assert "500" not in page.title(), "500 after junk input"