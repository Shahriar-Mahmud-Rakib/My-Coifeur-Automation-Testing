# Page: My Coifeur — Admin Management (Admins & Roles CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/admin-management`
**Type:** E2E Admin Management Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Management (Admins & Roles) module. Admins manage other administrator accounts, define roles, and assign permissions for role-based access control.

**API Endpoints:**
- `GET /api/v1/web/admin/admins` — list all admins
- `POST /api/v1/web/admin/admins` — create new admin
- `PUT /api/v1/web/admin/admins/{id}` — edit admin details
- `DELETE /api/v1/web/admin/admins/{id}` — delete admin account

---

## UI Elements

### Admin Management Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Admin Management")` | Heading | Yes | Title "Admin Management" |
| Search Input | `input[placeholder*="Search by admin name..."]` | Text Input | Yes | Filters admins |
| Add Admin Btn | `button:has-text("Add Admin")` | Button | Yes | Open create admin form |
| Admins Table | `table` | Table | Yes | Admin accounts list |
| Table Columns | `th` | Header | Yes | Columns: ADMIN NAME, E-MAIL, ROLE, STATUS, LAST ACTIVE, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Edit Admin | `[role="menuitem"]:has-text("Edit Admin")` | Menu Item | Yes | Opens edit modal |
| Delete Admin | `[role="menuitem"]:has-text("Delete Admin")` | Menu Item | Yes | Deletes admin account |

### Add / Edit Admin Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Full Name * | `input[name="name"]` | Text Input | Yes | Admin Name |
| E-mail * | `input[name="email"]` | Email Input | Yes | Login email |
| Password | `input[name="password"]` | Password | No | Password input |
| Confirm Password | `input[name="password_confirmation"]` | Password | No | Match check |
| Role * | `select[name="role"], select[name="role_id"]` | Select | Yes | Role dropdown (e.g. Admin, Manager) |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close |

---

## User Flows

### Flow 1: Verify Columns on Admin Table
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/admin-management`
3. Assert page title "Admin Management" is visible
4. Assert table columns exist: ADMIN NAME, E-MAIL, ROLE, STATUS, LAST ACTIVE, ACTIONS

### Flow 2: Create a New Admin Account
1. Login as admin
2. Navigate to `/en/admin/admin-management`
3. Click "Add Admin" button
4. Fill Full Name, Email, Password, Confirm Password, and select a Role
5. Click "Save Changes"
6. Assert success toast is shown and new admin is in table

### Flow 3: Edit Admin Profile and Role
1. Login as admin
2. Navigate to `/en/admin/admin-management`
3. Click 3-dot Actions menu on an admin row
4. Select "Edit Admin"
5. Assert Edit modal appears
6. Change full name or select a different role
7. Click "Save Changes"
8. Assert success toast and table updates

### Flow 4: Delete Admin Account
1. Login as admin
2. Navigate to `/en/admin/admin-management`
3. Click Actions -> Delete Admin on a row
4. Confirm delete action in dialog
5. Assert success toast is shown and account is removed from table

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Full Name * | Required | "Full name is required" |
| E-mail * | Required, valid email | "Invalid email format" |
| Password | Required on creation | "Password is required" |
| Role * | Required | "Please select a role" |

---

## Edge Cases
- EC-01: Create admin with duplicate email (validation error shown)
- EC-02: Self-delete active logged-in admin (should be blocked by UI or return error)
- EC-03: Access without authentication (redirect to login)
