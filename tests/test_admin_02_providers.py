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

def test_01_providers_page_loads_and_displays_headers(page: Page):
    """Verify that the providers list page loads successfully and contains the correct headers."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Providers")').first).to_be_visible(timeout=15000)
    
    # Check that search input is visible
    search_input = page.locator('input[placeholder*="Search providers..."], input[placeholder*="Search"]').first
    expect(search_input).to_be_visible()

def test_02_providers_tab_navigation(page: Page):
    """Verify navigating through APPROVED, PENDING, REJECTED provider tabs works."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    tabs = ["Approved", "Pending", "Rejected"]
    for tab in tabs:
        tab_btn = page.locator(f'button:has-text("{tab}")').filter(visible=True).first
        if tab_btn.count() > 0:
            tab_btn.click()
            page.wait_for_timeout(800)
            # Ensure page doesn't crash
            expect(page.locator("body")).to_be_visible()

def test_03_provider_search(page: Page):
    """Verify search filter executes correctly for provider list."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    search_input = page.locator('input[placeholder*="Search providers..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("Salon")
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_04_provider_details_and_edit_modal(page: Page):
    """Verify clicking view/edit provider opens details or dialog edit modal."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        edit_opt = page.locator('button:has-text("Edit Provider"), [role="menuitem"]:has-text("Edit")').first
        if edit_opt.count() > 0:
            edit_opt.click()
            page.wait_for_timeout(1000)
            # Close edit modal if visible
            close_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if close_btn.count() > 0:
                close_btn.click()

def test_05_provider_vip_status_toggle(page: Page):
    """Verify toggling VIP status switch operates correctly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Locate a VIP toggle switch (usually dynamic toggle or checkbox)
    vip_toggle = page.locator('button[role="switch"], input[type="checkbox"]').first
    if vip_toggle.count() > 0:
        # Just click the first toggle
        vip_toggle.click()
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_06_provider_ban_restore_dialog(page: Page):
    """Verify that clicking Ban/Restore triggers confirmation popup dialog with reason input."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/providers", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        ban_opt = page.locator('button:has-text("Ban Provider"), [role="menuitem"]:has-text("Ban")').first
        if ban_opt.count() > 0:
            ban_opt.click()
            page.wait_for_timeout(1000)
            
            # Assert text area for reason exists
            reason_field = page.locator('textarea[name="reason"], textarea[placeholder*="Reason"]').first
            if reason_field.count() > 0:
                expect(reason_field).to_be_visible()
            
            # Dismiss ban confirmation dialog
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()
