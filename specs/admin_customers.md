# Page: My Coifeur — Admin Customers (Detailed CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Customers Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Customers module covering:
- Customer Creation (CRUD)
- Image Upload (Profile image/avatar)
- Input Validations (Wrong/correct Email, empty Name, password requirements)
- Customer Edit and Delete

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Customers Link | `a[href*="/customers"]` | Anchor | Yes | Sidebar menu navigation link |
| Add Customer Btn | `button[data-action="add"], .add-btn, button:has-text("Add Customer")` | Button | Yes | Opens Add Customer form/modal |
| Customer Name Input | `input[name="name"], input[placeholder*="Name"]` | Text Input | Yes | Customer's full name field |
| Customer Email Input | `input[name="customer_email"], input[type="email"]` | Email Input | Yes | Customer's email address |
| Customer Password Input | `input[name="customer_password"], input[type="password"]` | Password | Yes | Customer's initial password |
| Customer Image Input | `input[type="file"]` | File Input | No | Profile photo/avatar upload |
| Save Customer Btn | `button[data-action="save"], .save-btn, button:has-text("Save")` | Button | Yes | Submits creation/edit form |
| Search Customer Input | `input[placeholder*="Search"]` | Text Input | No | Filter bar to search customers |
| First Edit Btn | `(.edit-btn, button[data-action="edit"])[0]` | Button | Yes | Edit action on the first list item |
| First Delete Btn | `(.delete-btn, button[data-action="delete"])[0]` | Button | Yes | Delete action on the first list item |
| Confirm Delete Btn | `button[data-action="confirm-delete"], button:has-text("Yes")` | Button | Yes | Delete modal confirmation button |
| Error Message Box | `.error-message, .invalid-feedback, .text-danger` | Element | No | Displays inline validation errors |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms successful CRUD operations |

---

## User Flows

### Flow 1: Create Customer with Valid Data & Image Upload
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Customers Link"
6. Click "Add Customer Btn"
7. Enter Customer Name Input: "John Doe QA"
8. Enter Customer Email Input: "johndoe_qa@example.com"
9. Enter Customer Password Input: "SecurePass123!"
10. Upload Customer Image Input: "dummy_avatar.png"
11. Click "Save Customer Btn"
12. Assert "Success Toast" is visible

### Flow 2: Form Validation - Invalid/Wrong Email & Empty Name
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Customers Link"
6. Click "Add Customer Btn"
7. Enter Customer Name Input: ""
8. Enter Customer Email Input: "invalidemailaddress"
9. Enter Customer Password Input: "123"
10. Click "Save Customer Btn"
11. Assert "Error Message Box" is visible (validation failed for empty name, bad email, short password)

### Flow 3: Edit and Update Customer Details
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Customers Link"
6. Click "First Edit Btn"
7. Enter Customer Name Input: "John Doe QA Updated"
8. Click "Save Customer Btn"
9. Assert "Success Toast" is visible

### Flow 4: Delete Customer
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Customers Link"
6. Click "First Delete Btn"
7. Click "Confirm Delete Btn"
8. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Customer Name Input | Required | "Name is required" |
| Customer Email Input | Email Format | "Invalid email format" |
| Customer Password Input | Minimum 6 characters | "Password must be at least 6 characters" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Create Customer with duplicate email | Error message indicating email is already registered |
| EC-02 | Upload invalid image format (e.g., pdf or txt) | Should show file format error |
| EC-03 | Delete without confirmation | Delete modal opens, does not delete immediately |
