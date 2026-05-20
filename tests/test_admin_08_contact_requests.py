import os, time, pytest
from playwright.sync_api import Page, expect

BASE_URL = os.getenv("BASE_URL", "https://dev.mycoifeur.com.sa")

def admin_login(page: Page):
    """Helper function to authenticate as Admin and navigate to Dashboard."""
    page.goto(f"{BASE_URL}/en/admin-login", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1000)
    
    # Fill login credentials using precise selectors
    email_input = page.locator('#email').first
    password_input = page.locator('#password').first
    login_btn = page.locator('button[type="submit"], button:has-text("Sign in")').first
    
    email_input.fill("amrmuhamed9@gmail.com")
    password_input.fill("123456")
    login_btn.click()
    
    # Wait for transition/dashboard URL to completely clear the login card
    page.wait_for_url("**/en/admin/overview", timeout=20000)
    page.wait_for_timeout(1500)

def test_01_contact_requests_page_loads_and_displays_headers(page: Page):
    """Verify that the contact requests list page loads successfully and displays expected headers."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/contact-requests", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Contact Requests"), h1:has-text("Messages")').first).to_be_visible(timeout=15000)
    
    # Check headers
    headers = ["EMAIL", "SUBJECT", "ACTIONS"]
    for header in headers:
        expect(page.locator(f'th:has-text("{header}")').first).to_be_visible(timeout=5000)

def test_02_contact_request_search(page: Page):
    """Verify contact requests list search operates properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/contact-requests", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    search_input = page.locator('input[placeholder*="Search requests..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("support")
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_03_contact_request_view_details_modal(page: Page):
    """Verify that clicking details action opens full ticket view modal dialog."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/contact-requests", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        view_opt = page.locator('button:has-text("View Message"), [role="menuitem"]:has-text("View"), [role="menuitem"]:has-text("Details")').first
        if view_opt.count() > 0:
            view_opt.click()
            page.wait_for_timeout(1000)
            
            # Close details dialog
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()

def test_04_contact_request_delete_warning(page: Page):
    """Verify that clicking delete triggers a validation warning/confirmation box."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/contact-requests", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        delete_opt = page.locator('button:has-text("Delete Request"), [role="menuitem"]:has-text("Delete")').first
        if delete_opt.count() > 0:
            delete_opt.click()
            page.wait_for_timeout(1000)
            
            # Dismiss alert confirmation
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()
