# Page: My Coifeur — Admin Providers (Salon Management)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Providers Flow
**Priority:** P0

---

## Page Purpose
End-to-End test for the Admin Providers (Salons) module covering:
- Salon List, search, and pagination
- Updating Salon Information
- Ban/Block and Unban/Restore Salons
- Setting/unsetting Salon VIP status
- Gallery photo uploads and Working days review

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Providers Link | `a[href*="/providers"], a[href*="/salons"]` | Anchor | Yes | Sidebar navigation link |
| Search Providers Input | `input[placeholder*="Search"]` | Text Input | No | Search bar to filter salons |
| First Edit Btn | `(.edit-btn, button[data-action="edit"])[0]` | Button | Yes | Edit action on the first salon |
| Provider Name Input | `input[name="salon_name"], input[name="fname"]` | Text Input | Yes | Provider Name field |
| Save Provider Btn | `button[data-action="save"], button:has-text("Save")` | Button | Yes | Saves provider details changes |
| Ban Provider Btn | `button[data-action="ban"], .ban-btn, button:has-text("Ban")` | Button | Yes | Opens block/ban confirmation modal |
| Ban Reason Input | `textarea[name="ban_reason"], textarea[placeholder*="Reason"]` | Text Area | Yes | Input field for explanation reason |
| Confirm Ban Btn | `button[data-action="confirm-ban"], button:has-text("Confirm Ban")` | Button | Yes | Confirms ban operation |
| Restore Banned Btn | `button[data-action="restore"], .restore-btn, button:has-text("Restore")` | Button | No | Reverses ban block |
| VIP Toggle Switch | `input[type="checkbox"][name="is_vip"], .vip-toggle` | Checkbox | Yes | Toggles VIP status |
| Gallery Tab | `[data-tab="gallery"], button:has-text("Gallery")` | Tab/Button | Yes | Navigates to Salon gallery |
| Gallery Image Upload | `input[type="file"][name="gallery_image"]` | File Input | Yes | Image upload control for gallery |
| Working Days Tab | `[data-tab="working-days"], button:has-text("Working Days")` | Tab/Button | Yes | Navigates to Salon working hours |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Update Provider Details
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Providers Link"
6. Click "First Edit Btn"
7. Enter Provider Name Input: "Automated Premium Salon QA"
8. Click "Save Provider Btn"
9. Assert "Success Toast" is visible

### Flow 2: Ban & Restore Salon Provider
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Providers Link"
6. Click "Ban Provider Btn" on the first salon
7. Enter Ban Reason Input: "Temporary block for payment discrepancy"
8. Click "Confirm Ban Btn"
9. Assert "Success Toast" is visible
10. Click "Restore Banned Btn" to restore the salon
11. Assert "Success Toast" is visible

### Flow 3: Toggle VIP Status
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Providers Link"
6. Click "First Edit Btn"
7. Check or Uncheck "VIP Toggle Switch" to change status
8. Click "Save Provider Btn"
9. Assert "Success Toast" is visible

### Flow 4: Upload Photo to Gallery
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Providers Link"
6. Click "First Edit Btn"
7. Click "Gallery Tab"
8. Upload Gallery Image Upload: "dummy_salon_photo.png"
9. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Provider Name Input | Required | "Provider name cannot be empty" |
| Ban Reason Input | Required when banning | "Ban reason must be specified" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Ban salon without reason | Error message displays on form |
| EC-02 | Upload invalid file type to gallery | Shows error toast "Invalid file format" |
