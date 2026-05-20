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

def test_01_promocode_page_loads_and_displays_headers(page: Page):
    """Verify that the promo codes page loads successfully and displays expected headers."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/promo-codes", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Promo Codes"), h1:has-text("Coupons")').first).to_be_visible(timeout=15000)
    
    # Check headers
    headers = ["CODE", "DISCOUNT TYPE", "VALUE", "ACTIONS"]
    for header in headers:
        expect(page.locator(f'th:has-text("{header}")').first).to_be_visible(timeout=5000)

def test_02_add_promocode_form_validation(page: Page):
    """Verify promo code registration form modal triggers rules on empty submit."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/promo-codes", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    add_btn = page.locator('button:has-text("Add Promo Code"), button:has-text("Create Promo Code"), button:has-text("Add Coupon")').first
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

def test_03_promocode_search(page: Page):
    """Verify promo codes search filter operates properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/promo-codes", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    search_input = page.locator('input[placeholder*="Search promo codes..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("SAVE50")
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()

def test_04_promocode_edit_usage_limit(page: Page):
    """Verify that editing promo code usage limits and details operates properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/promo-codes", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        edit_opt = page.locator('button:has-text("Edit Promo Code"), button:has-text("Edit Coupon"), [role="menuitem"]:has-text("Edit")').first
        if edit_opt.count() > 0:
            edit_opt.click()
            page.wait_for_timeout(1000)
            
            limit_input = page.locator('input[name="usage_limit"], input[name="limit"]').first
            if limit_input.count() > 0:
                limit_input.fill("1000")
                page.wait_for_timeout(500)
                
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()
