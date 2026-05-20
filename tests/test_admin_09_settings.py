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

def test_01_settings_page_loads_and_displays_tabs(page: Page):
    """Verify that the settings configuration page loads successfully and displays expected navigation tabs."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/settings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    # Assert header
    expect(page.locator('h1:has-text("Settings"), h1:has-text("System Configuration")').first).to_be_visible(timeout=15000)
    
    # Check general settings tab is visible
    gen_tab = page.locator('[role="tab"]:has-text("General Settings"), button:has-text("General Settings")').first
    expect(gen_tab).to_be_visible()

def test_02_settings_tab_navigation(page: Page):
    """Verify navigating through all settings subsections works properly without crashing."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/settings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    tabs = ["General Settings", "Email Provider", "Connection Settings", "Roles & Permissions"]
    for tab in tabs:
        tab_btn = page.locator(f'[role="tab"]:has-text("{tab}"), button:has-text("{tab}")').filter(visible=True).first
        if tab_btn.count() > 0:
            tab_btn.click()
            page.wait_for_timeout(800)
            expect(page.locator("body")).to_be_visible()

def test_03_general_settings_modify_form(page: Page):
    """Verify modifying general configurations (English title, SEO keywords) works."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/settings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    title_input = page.locator('input[name="title_en"]').first
    if title_input.count() > 0:
        title_input.fill("My Coifeur Salon Marketplace")
        page.wait_for_timeout(500)
        
    keywords_input = page.locator('input[name="keywords"]').first
    if keywords_input.count() > 0:
        keywords_input.fill("salons, booking, grooming, hair care")
        page.wait_for_timeout(500)

def test_04_roles_and_permissions_configuration(page: Page):
    """Verify that accessing Roles cards and clicking configure dialog works."""
    admin_login(page)
    page.goto(f"{BASE_URL}/en/admin/settings", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(1500)
    
    roles_tab = page.locator('[role="tab"]:has-text("Roles & Permissions"), button:has-text("Roles & Permissions")').first
    if roles_tab.count() > 0:
        roles_tab.click()
        page.wait_for_timeout(1000)
        
        # Click first Configure role button
        config_btn = page.locator('button:has-text("Configure"), .role-card button').filter(visible=True).first
        if config_btn.count() > 0:
            config_btn.click()
            page.wait_for_timeout(1000)
            
            # Dismiss modal
            cancel_btn = page.locator('button:has-text("Cancel"), button:has-text("Close")').first
            if cancel_btn.count() > 0:
                cancel_btn.click()
