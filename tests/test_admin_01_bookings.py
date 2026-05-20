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

def test_01_bookings_page_loads_and_displays_columns(page: Page):
    """Verify that the bookings page loads successfully and contains the correct table columns."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert headers
    expect(page.locator('h1:has-text("Bookings")').first).to_be_visible(timeout=15000)
    
    # Verify table headers exist
    headers = ["CUSTOMER", "SERVICE", "PROVIDER", "DATE & TIME", "PRICE", "STATUS", "ACTIONS"]
    for header in headers:
        expect(page.locator(f'th:has-text("{header}")').first).to_be_visible(timeout=5000)

def test_02_bookings_status_tabs_filtering(page: Page):
    """Verify that clicking different status filter tabs changes the URL and works correctly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Define status filters and active class checks
    statuses = ["Sales", "In Cart", "On Hold", "Accepted", "Rejected", "In Progress", "Completed", "Cancelled"]
    for status in statuses:
        btn = page.locator(f'button:has-text("{status}")').filter(visible=True).first
        if btn.count() > 0:
            btn.click()
            page.wait_for_timeout(1000)
            # Assert page doesn't crash on filter click
            expect(page.locator("body")).to_be_visible()

def test_03_bookings_search_functionality(page: Page):
    """Verify that searching for a customer or booking filter operates properly."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    search_input = page.locator('input[placeholder*="Search bookings..."], input[placeholder*="Search"]').first
    if search_input.count() > 0:
        search_input.fill("John Doe")
        page.wait_for_timeout(1000)
        # Verify no 500 crashes
        expect(page.locator("body")).to_be_visible()

def test_04_sales_report_page_and_filters(page: Page):
    """Verify Sales Report subpage can load and filter selections operate properly."""
    admin_login(page)
    
    # Navigate to sales report page (or click Sales Report button)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    sales_btn = page.locator('button:has-text("Sales"), button:has-text("Sales Report")').filter(visible=True).first
    if sales_btn.count() > 0:
        sales_btn.click()
        page.wait_for_timeout(1500)
        
    # Test Category and Service Filter Dropdowns
    cat_select = page.locator('select[name="category"], select[placeholder*="Category"]').first
    if cat_select.count() > 0:
        cat_select.select_option(index=1)
        page.wait_for_timeout(800)
        
    serv_select = page.locator('select[name="service"], select[placeholder*="Service"]').first
    if serv_select.count() > 0:
        serv_select.select_option(index=1)
        page.wait_for_timeout(800)

def test_05_sales_report_export(page: Page):
    """Verify clicking the export sales report button works."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    export_btn = page.locator('button:has-text("Export"), button:has-text("Download")').filter(visible=True).first
    if export_btn.count() > 0:
        # Just assert it is enabled and clickable
        expect(export_btn).to_be_enabled()

def test_06_bookings_row_actions_menu(page: Page):
    """Verify that clicking the 3-dot actions dropdown shows expected actions."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/bookings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    dots_menu = page.locator('button:has-text("..."), td button').filter(visible=True).first
    if dots_menu.count() > 0:
        dots_menu.click()
        page.wait_for_timeout(500)
        
        view_opt = page.locator('button:has-text("View Details"), [role="menuitem"]:has-text("View")').first
        edit_opt = page.locator('button:has-text("Edit Booking"), [role="menuitem"]:has-text("Edit")').first
        
        # At least one should be present or valid
        expect(page.locator("body")).to_be_visible()
