# Page: My Coifeur — Admin Settings (System Configuration)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Settings Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Settings module covering:
- General configurations (App Name, Maintenance Mode status toggle)
- SMS Provider integrations (Twilio credentials)
- SMTP/Mail server configurations (SMTP Host, Port value bounds, secure transport toggle)

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Settings Link | `a[href*="/settings"]` | Anchor | Yes | Sidebar settings menu link |
| App Name Input | `input[name="app_name"]` | Text Input | Yes | Platform name field |
| Maintenance Toggle | `input[type="checkbox"][name="maintenance_mode"], .maintenance-toggle` | Checkbox | Yes | Toggles offline maintenance mode |
| Connection Settings Tab | `[data-tab="connection"], button:has-text("Connection")` | Tab/Button | Yes | Navigates to SMS Connection |
| SMS Provider Select | `select[name="sms_provider"]` | Select | Yes |twilo or other SMS provider |
| SMS API Key Input | `input[name="sms_api_key"]` | Password | Yes | Twilio auth token or key |
| Mail Provider Tab | `[data-tab="mail"], button:has-text("Mail Provider")` | Tab/Button | Yes | SMTP server configurations |
| SMTP Host Input | `input[name="host"], input[placeholder*="Host"]` | Text Input | Yes | Mail server hostname |
| SMTP Port Input | `input[name="port"], input[type="number"]` | Number Input | Yes | Port code (e.g. 587, 465) |
| Save Settings Btn | `button[data-action="save-settings"], button:has-text("Save Settings")` | Button | Yes | Submits settings form changes |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Update Platform General Settings
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Settings Link"
6. Enter App Name Input: "My Coifeur Portal QA"
7. Check or Uncheck "Maintenance Toggle" to switch maintenance mode status
8. Click "Save Settings Btn"
9. Assert "Success Toast" is visible

### Flow 2: Configure SMS Connections
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Settings Link"
6. Click "Connection Settings Tab"
7. Select SMS Provider Select: Twilio ("twilio")
8. Enter SMS API Key Input: "TwilioTokenQAValue12345!"
9. Click "Save Settings Btn"
10. Assert "Success Toast" is visible

### Flow 3: Update SMTP Mail Configurations
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Settings Link"
6. Click "Mail Provider Tab"
7. Enter SMTP Host Input: "smtp.mailgun.org"
8. Enter SMTP Port Input: "587"
9. Click "Save Settings Btn"
10. Assert "Success Toast" is visible

### Flow 4: Form Validation - Invalid Port Number
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Settings Link"
6. Click "Mail Provider Tab"
7. Enter SMTP Port Input: "-999"
8. Click "Save Settings Btn"
9. Assert validation error displays near port field (port must be greater than or equal to 0)

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| App Name Input | Required | "App name cannot be empty" |
| SMTP Host Input | Required | "Mail host is required" |
| SMTP Port Input | Must be positive | "Port must be positive number" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Set App Name length greater than 255 chars | Validation blocks submit / truncates |
| EC-02 | Set zero (0) for SMTP Port number | Handled safely by validation rules |
| EC-03 | Security - ensure admin password fields are masked | Elements show type="password" attribute |
