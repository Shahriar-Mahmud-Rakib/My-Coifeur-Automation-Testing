# Page: My Coifeur — Admin Promo Codes (Coupons CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/promo-codes`
**Type:** E2E Admin Promo Codes Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Promo Codes module. Admins manage discounts, configure fixed or percentage coupons, set start and expiration dates, usage limits, and track promotion metrics.

**API Endpoints:**
- `GET /api/v1/admin/promocodes` — list promo codes
- `POST /api/v1/admin/promocodes` — create promo code
- `PUT /api/v1/admin/promocodes/{id}` — edit promo code
- `DELETE /api/v1/admin/promocodes/{id}` — delete promo code

---

## UI Elements

### Promo Codes Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Promo Codes")` | Heading | Yes | Title "Promo Codes" |
| Search Input | `input[placeholder*="Search promo codes..."]` | Text Input | Yes | Filters promo list |
| Add Promo Code Btn | `button:has-text("Add Promo Code")` | Button | Yes | Open create promocode form |
| Promo Codes Table | `table` | Table | Yes | Promotional discount grid |
| Table Columns | `th` | Header | Yes | Columns: CODE, DISCOUNT TYPE, VALUE, USAGE, START DATE, EXPIRY DATE, STATUS, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Edit Promo Code | `[role="menuitem"]:has-text("Edit Promo Code")` | Menu Item | Yes | Opens edit modal |
| Delete Promo Code | `[role="menuitem"]:has-text("Delete Promo Code")` | Menu Item | Yes | Deletes promo code |

### Add / Edit Promo Code Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Promo Code * | `input[name="code"]` | Text Input | Yes | Code string (e.g., SAVE50) |
| Discount Type * | `select[name="discount_type"], select[name="type"]` | Select | Yes | Dropdown: Percentage, Fixed Amount |
| Value * | `input[name="value"]` | Number Input | Yes | Discount amount value |
| Usage Limit * | `input[name="usage_limit"]` | Number Input | Yes | Max coupon usage limit |
| Start Date * | `input[name="start_date"], button:has-text("Start Date")` | Date Input | Yes | Promotion start date |
| Expiry Date * | `input[name="expiry_date"], button:has-text("Expiry Date")` | Date Input | Yes | Promotion end date |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close |

---

## User Flows

### Flow 1: Verify Columns on Promo Codes Table
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/promo-codes`
3. Assert page title "Promo Codes" is visible
4. Assert table columns exist: CODE, DISCOUNT TYPE, VALUE, USAGE, START DATE, EXPIRY DATE, STATUS, ACTIONS

### Flow 2: Create a Percentage Discount Promo Code
1. Login as admin
2. Navigate to `/en/admin/promo-codes`
3. Click "Add Promo Code" button
4. Fill Promo Code "DISCOUNT50", Discount Type "Percentage", Value "50", Usage Limit "100", and select Start & Expiry dates
5. Click "Save Changes"
6. Assert success toast is shown and new promo is in table

### Flow 3: Create a Fixed Amount Promo Code
1. Login as admin
2. Navigate to `/en/admin/promo-codes`
3. Click "Add Promo Code" button
4. Fill Promo Code "SAR25", Discount Type "Fixed Amount", Value "25", Usage Limit "500", and select Start & Expiry dates
5. Click "Save Changes"
6. Assert success toast is shown and new promo is in table

### Flow 4: Edit Promo Code Usage Limit
1. Login as admin
2. Navigate to `/en/admin/promo-codes`
3. Click 3-dot Actions menu on a promo code row
4. Select "Edit Promo Code"
5. Assert Edit modal appears
6. Change Usage Limit to "1000"
7. Click "Save Changes"
8. Assert success toast and table updates

### Flow 5: Delete Promo Code
1. Login as admin
2. Navigate to `/en/admin/promo-codes`
3. Click Actions -> Delete Promo Code on a row
4. Confirm delete action in dialog
5. Assert success toast is shown and promo code is removed from table

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Promo Code * | Required, alphanumeric | "Promo code is required" |
| Value * | Required, positive number | "Value must be positive" |
| Usage Limit * | Required, positive integer | "Limit must be positive" |
| Start Date * | Required | "Start date is required" |
| Expiry Date * | Required, must be after Start Date | "Expiry date must be after start date" |

---

## Edge Cases
- EC-01: Create coupon with duplicate promo code string (validation error)
- EC-02: Fixed amount discount greater than service price (returns validation error)
- EC-03: Access without authentication (redirect to login)
