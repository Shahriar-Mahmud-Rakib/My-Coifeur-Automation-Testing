# Page: My Coifeur — Admin Promo Codes (Coupons CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Promo Codes Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Promo Codes (Coupons) module covering:
- Creating new promo codes (Code string, percentage/fixed discount, usage limits, expiration date)
- Checking promo code validations (empty fields, expired dates, negative discount values)
- Editing, activating, and deleting promo codes

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Promo Codes Link | `a[href*="/promocodes"], a[href*="/coupons"]` | Anchor | Yes | Sidebar promotional codes link |
| Add Promo Btn | `button[data-action="add-promo"], button:has-text("Add Promo Code")` | Button | Yes | Opens Promo creation form |
| Promo Code Input | `input[name="code"], input[placeholder*="Code"]` | Text Input | Yes | Code string (e.g. SUMMER50) |
| Discount Type Select | `select[name="type"], select[name="discount_type"]` | Select | Yes | Percentage or Fixed value selection |
| Discount Value Input | `input[name="value"], input[name="discount_value"]` | Number Input | Yes | Discount amount in percentage or SAR |
| Max Usage Input | `input[name="usage_limit"], input[name="max_uses"]` | Number Input | Yes | Max total usage limit |
| Expiry Date Input | `input[name="expiry_date"], input[type="date"]` | Date Input | Yes | Promotion expiration date |
| Save Promo Btn | `button[data-action="save-promo"], button:has-text("Save Code")` | Button | Yes | Submits creation/edit form |
| First Edit Promo Btn | `(.edit-promo, button[data-action="edit"])[0]` | Button | Yes | Opens promo edit modal |
| First Delete Promo Btn | `(.delete-promo, button[data-action="delete"])[0]` | Button | Yes | Deletes selected promo code |
| Confirm Delete Btn | `button[data-action="confirm-delete"], button:has-text("Yes")` | Button | Yes | Modal confirm delete button |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Create Promo Code with Valid Data
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Promo Codes Link"
6. Click "Add Promo Btn"
7. Enter Promo Code Input: "TESTE2E100"
8. Select Discount Type Select: Percentage ("percentage")
9. Enter Discount Value Input: "20"
10. Enter Max Usage Input: "500"
11. Enter Expiry Date Input: "2026-12-31"
12. Click "Save Promo Btn"
13. Assert "Success Toast" is visible

### Flow 2: Form Validation - Invalid Expiry Date & Negative Discount
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Promo Codes Link"
6. Click "Add Promo Btn"
7. Enter Promo Code Input: "EXPIREDCODE"
8. Enter Discount Value Input: "-50"
9. Enter Expiry Date Input: "2020-01-01"
10. Click "Save Promo Btn"
11. Assert validation error is displayed (discount must be positive, expiry date must be in future)

### Flow 3: Edit and Update Promo Code
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Promo Codes Link"
6. Click "First Edit Promo Btn"
7. Enter Max Usage Input: "1000"
8. Click "Save Promo Btn"
9. Assert "Success Toast" is visible

### Flow 4: Delete Promo Code
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Promo Codes Link"
6. Click "First Delete Promo Btn"
7. Click "Confirm Delete Btn"
8. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Promo Code Input | Required | "Promo code name is required" |
| Discount Value Input | Positive number | "Discount must be greater than 0" |
| Expiry Date Input | Future date | "Expiry date must be a future date" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Create Promo Code with discount value > 100 on percentage type | Validation error blocks submission |
| EC-02 | Create duplicate promo code name | Shows "Promo code already exists" error |
| EC-03 | Delete promo code without confirmation | Delete modal opens, does not execute immediately |
