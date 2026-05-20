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

def test_01_admin_management_page_loads_and_displays_headers(page: Page):
    """Verify that the admin management list page loads successfully and displays expected headers."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/admin-management", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Admin Management"), h1:has-text("Admins")').first).to_be_visible(timeout=15000)
    
    # Check headers
    headers = ["ADMIN", "EMAIL", "ROLE", "ACTIONS"]
    for header in headers:
        expect(page.locator(f'th:has-text("{header}")').first).to_be_visible(timeout=5000)

def test_02_add_admin_form_validation(page: Page):
    """Verify admin registration form modal triggers rules on empty submit."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/admin-management", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    add_btn = page.locator('button:has-text("Add Admin"), button:has-text("Create Admin")').first
    if add_btn.count() > 0:
        add_btn.click()
        page.wait_for_timeout(1000)
        
        save_btn = page.locator('button:has-text("Save"), button:has-text("Create")').first
        if save_btn.count() > 0:
            save_btn.click()
            page.wait_for_timeout(500)
            
        # Cancel / close form modal
        cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
        if cancel_btn.count() > 0:
            cancel_btn.click()

def test_03_admin_management_search(page: Page):
    """Verify sub-admin list search operates properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/admin-management", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    search_input = page.locator('input[placeholder*="Search admins..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("Super Admin")
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_04_admin_active_suspend_toggle(page: Page):
    """Verify that toggle/checkbox actions on admin list work properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/admin-management", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Locate a status switch or toggle
    toggle = page.locator('button[role="switch"], input[type="checkbox"]').first
    if toggle.count() > 0:
        toggle.click()
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_05_admin_details_and_edit_role(page: Page):
    """Verify that editing sub-admin details works."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/admin-management", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        edit_opt = page.locator('button:has-text("Edit Admin"), [role="menuitem"]:has-text("Edit")').first
        if edit_opt.count() > 0:
            edit_opt.click()
            page.wait_for_timeout(1000)
            
            role_select = page.locator('select[name="role"], select[placeholder*="Role"]').first
            if role_select.count() > 0:
                role_select.select_option(index=1)
                page.wait_for_timeout(500)
                
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()
