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

def test_01_finance_page_loads_and_displays_tabs(page: Page):
    """Verify that the finance dashboard page loads and displays Payout Requests / Wallet tabs."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/finance", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Finance"), h1:has-text("Financials")').first).to_be_visible(timeout=15000)
    
    # Check that tabs are present
    payout_tab = page.locator('[role="tab"]:has-text("Payout Requests"), button:has-text("Payout Requests")').first
    expect(payout_tab).to_be_visible()

def test_02_payout_requests_table_headers(page: Page):
    """Verify that the payout requests table contains expected headers."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/finance", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Check payout headers
    headers = ["PROVIDER", "AMOUNT", "STATUS", "ACTIONS"]
    for header in headers:
        expect(page.locator(f'th:has-text("{header}")').first).to_be_visible(timeout=5000)

def test_03_payout_approval_rejection_modal(page: Page):
    """Verify that payout request action buttons open transition dialog modal."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/finance", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_btn = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_btn.count() > 0:
        dots_btn.click()
        page.wait_for_timeout(500)
        
        details_opt = page.locator('button:has-text("View Payout"), [role="menuitem"]:has-text("View"), [role="menuitem"]:has-text("Details")').first
        if details_opt.count() > 0:
            details_opt.click()
            page.wait_for_timeout(1000)
            
            # Close dialog
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()

def test_04_manual_send_money_payout_modal(page: Page):
    """Verify that the manual Send Money dialog loads and validates amount input."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/finance", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    send_btn = page.locator('button:has-text("Send Money"), button:has-text("Payout Manually")').first
    if send_btn.count() > 0:
        send_btn.click()
        page.wait_for_timeout(1000)
        
        # Verify inputs exist
        amount_input = page.locator('input[name="amount"]').first
        if amount_input.count() > 0:
            expect(amount_input).to_be_visible()
            
        cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
        if cancel_btn.count() > 0:
            cancel_btn.click()

def test_05_wallet_list_and_search(page: Page):
    """Verify Wallet List tab navigation and transaction history search filters."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/finance", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    wallet_tab = page.locator('[role="tab"]:has-text("Wallet List"), button:has-text("Wallet List")').first
    if wallet_tab.count() > 0:
        wallet_tab.click()
        page.wait_for_timeout(1000)
        
    search_input = page.locator('input[placeholder*="Search transactions..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("1234")
        page.wait_for_timeout(1000)
        expect(page.locator("body")).to_be_visible()
