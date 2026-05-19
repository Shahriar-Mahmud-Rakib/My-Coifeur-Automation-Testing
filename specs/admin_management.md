# Page: My Coifeur — Admin Management (Admins & Roles)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Management Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Management module covering:
- Creating a new Admin account
- Verifying and toggling Admin active status
- Creating Roles and configuring role permissions
- Modifying and deleting Roles

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Admins Link | `a[href*="/admins"], a[href*="/management"]` | Anchor | Yes | Sidebar management link |
| Add Admin Btn | `button[data-action="add-admin"], .add-admin-btn, button:has-text("Add Admin")` | Button | Yes | Opens Add Admin account form |
| New Admin Email Input | `input[name="admin_email"], input[type="email"]` | Email Input | Yes | New admin's login email |
| New Admin Password Input | `input[name="admin_password"], input[type="password"]` | Password | Yes | New admin's login password |
| New Admin First Name | `input[name="fname"], input[placeholder*="First Name"]` | Text Input | Yes | New admin first name |
| New Admin Last Name | `input[name="lname"], input[placeholder*="Last Name"]` | Text Input | Yes | New admin last name |
| New Admin Phone | `input[name="phone"], input[type="tel"]` | Text Input | Yes | New admin phone number |
| Save Admin Btn | `button[data-action="save-admin"], button:has-text("Create Admin")` | Button | Yes | Submits new admin creation |
| Toggle Active Btn | `(.toggle-status-btn, button[data-action="active"])[0]` | Button | Yes | Toggles admin active/suspended status |
| Verify Admin Btn | `(.verify-btn, button[data-action="verify"])[0]` | Button | Yes | Verifies new admin account |
| Roles Tab | `[data-tab="roles"], button:has-text("Roles")` | Tab/Button | Yes | Navigates to Roles list |
| Add Role Btn | `button[data-action="add-role"], button:has-text("Add Role")` | Button | Yes | Opens role creation form |
| Role Name Input | `input[name="role_name"], input[name="name"]` | Text Input | Yes | Name of the role (e.g. Supervisor) |
| Permission Checkbox | `input[type="checkbox"][name="permissions[]"]` | Checkbox | No | Permissions checkboxes list |
| Save Role Btn | `button[data-action="save-role"], button:has-text("Save Role")` | Button | Yes | Submits role form |
| First Delete Role Btn | `(.delete-role-btn, button[data-action="delete-role"])[0]` | Button | Yes | Deletes first custom role |
| Confirm Delete Btn | `button[data-action="confirm-delete"], button:has-text("Yes")` | Button | Yes | Deletes role modal confirmation |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Create New Admin Account
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Admins Link"
6. Click "Add Admin Btn"
7. Enter New Admin Email Input: "sub_admin_qa@example.com"
8. Enter New Admin Password Input: "SecureAdminPass123!"
9. Enter New Admin First Name: "Sub"
10. Enter New Admin Last Name: "Admin"
11. Enter New Admin Phone: "966509876543"
12. Click "Save Admin Btn"
13. Assert "Success Toast" is visible

### Flow 2: Toggle Admin Status and Verify
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Admins Link"
6. Click "Verify Admin Btn" on the newly created admin row
7. Assert "Success Toast" is visible
8. Click "Toggle Active Btn" to toggle account suspension
9. Assert "Success Toast" is visible

### Flow 3: Create Role with Permissions
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Admins Link"
6. Click "Roles Tab"
7. Click "Add Role Btn"
8. Enter Role Name Input: "QA Senior Supervisor"
9. Check "Permission Checkbox" for the first two options
10. Click "Save Role Btn"
11. Assert "Success Toast" is visible

### Flow 4: Delete Custom Role
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Admins Link"
6. Click "Roles Tab"
7. Click "First Delete Role Btn"
8. Click "Confirm Delete Btn"
9. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| New Admin Email Input | Email format | "Invalid email format" |
| New Admin Phone | Length & numbers | "Phone number must start with 966" |
| Role Name Input | Required | "Role name is required" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Create Admin with short weak password | Validation warning should show |
| EC-02 | Create Role without selecting permissions | Create role successfully or show select permission warning |
