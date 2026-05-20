# Page: My Coifeur — Admin Customers (Users CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/customers`
**Type:** E2E Admin Customers Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Customers (Users) module. Admins manage consumer profiles, verify accounts, manage reward points, toggle block status, and search customer tables.

**API Endpoints:**
- `GET /api/v1/web/admin/users` — list all users
- `PUT /api/v1/web/admin/users/{id}` — update user profile
- `POST /api/v1/web/admin/users/block` — block user
- `POST /api/v1/web/admin/users/{id}/restore` — restore user
- `GET /api/v1/web/admin/users/{id}/rewards` — user rewards data

---

## UI Elements

### Customers List Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Customers")` | Heading | Yes | Title "Customers" |
| Search Input | `input[placeholder*="Search customers..."]` | Text Input | Yes | Filters customers list |
| Add Customer Btn | `button:has-text("Add Customer")` | Button | Yes | Open create form |
| Customers Table | `table` | Table | Yes | Customer data grid |
| Table Columns | `th` | Header | Yes | Columns: CUSTOMER, EMAIL, PHONE, STATUS, REWARDS, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| View Details | `[role="menuitem"]:has-text("View Details")` | Menu Item | Yes | View user details |
| Edit Customer | `[role="menuitem"]:has-text("Edit Customer")` | Menu Item | Yes | Opens edit modal |
| Block Customer | `[role="menuitem"]:has-text("Block Customer")` | Menu Item | Yes | Blocks user account |
| Restore Customer | `[role="menuitem"]:has-text("Restore Customer")` | Menu Item | No | Restores blocked account |

### Add / Edit Customer Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Customer Name | `input[name="name"]` | Text Input | Yes | Full Name |
| Customer Email | `input[name="email"]` | Email Input | Yes | Email address |
| Customer Phone | `input[name="phone"]` | Text Input | Yes | Phone starting with 966 |
| Customer Password | `input[name="password"]` | Password | No | Leave blank to keep current |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close |

---

## User Flows

### Flow 1: List Customers and Verify Columns
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/customers`
3. Assert page heading "Customers" is visible
4. Assert table columns exist: CUSTOMER, EMAIL, PHONE, STATUS, REWARDS, ACTIONS

### Flow 2: Search Customer by Email
1. Login as admin
2. Navigate to `/en/admin/customers`
3. Type a known customer email in search input
4. Assert only matching customer rows are displayed
5. Clear search input and assert all rows reappear

### Flow 3: Create New Customer Account
1. Login as admin
2. Navigate to `/en/admin/customers`
3. Click "Add Customer" button
4. Fill Name, Email, Phone (starts with 966), and Password
5. Click "Save Changes"
6. Assert success toast is shown and new customer is in table

### Flow 4: Edit Customer Profile via Modal
1. Login as admin
2. Navigate to `/en/admin/customers`
3. Click 3-dot Actions menu on a customer row
4. Select "Edit Customer"
5. Assert Edit modal appears
6. Change customer name to "QA Updated Customer"
7. Click "Save Changes"
8. Assert success toast and table updates

### Flow 5: Block Customer Account
1. Login as admin
2. Navigate to `/en/admin/customers`
3. Click Actions -> Block Customer
4. Confirm block action in dialog
5. Assert success toast and status badge changes to "Blocked"

### Flow 6: Restore Blocked Customer
1. Login as admin
2. Navigate to `/en/admin/customers`
3. Click Actions -> Restore Customer
4. Assert success toast and status badge updates to "Active"

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Customer Name | Required | "Customer name is required" |
| Customer Email | Required, valid email | "Invalid email format" |
| Customer Phone | Required, starts with 966 | "Invalid phone number" |

---

## Edge Cases
- EC-01: Block already blocked customer (not visible/possible)
- EC-02: Search with SQL injection payload (sanitized)
- EC-03: Access without authentication (redirect to login)
