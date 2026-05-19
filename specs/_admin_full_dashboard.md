# Page: My Coifeur — Admin Full Dashboard (CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Dashboard Flow
**Priority:** P0

---

## Page Purpose
End-to-End test for the Admin Dashboard covering Login, Overview, Bookings, Customers, and Admin Management (Add, Edit, Delete).

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits login |
| Overview Link | `a[href="/en/admin/overview"]` | Anchor | Yes | Navigates to Overview |
| Overview Chart | `canvas.chart, .overview-chart` | Element | Yes | Verifies chart presence |
| Bookings Link | `a[href="/en/admin/bookings"]` | Anchor | Yes | Navigates to Bookings |
| Edit Booking Btn | `button[data-action="edit-booking"]` | Button | Yes | Opens booking edit modal |
| Delete Booking Btn | `button[data-action="delete-booking"]` | Button | Yes | Opens delete confirm |
| Confirm Delete Btn | `button[data-action="confirm-delete"]` | Button | Yes | Confirms deletion |
| Customers Link | `a[href="/en/admin/customers"]` | Anchor | Yes | Navigates to Customers |
| Add Customer Btn | `button[data-action="add-customer"]` | Button | Yes | Opens add modal |
| Customer Name | `input[name="customerName"]` | Text Input | Yes | Customer name field |
| Save Customer Btn | `button[data-action="save-customer"]` | Button | Yes | Saves customer |
| Edit Customer Btn | `button[data-action="edit-customer"]` | Button | Yes | Edits customer |
| Delete Customer Btn | `button[data-action="delete-customer"]` | Button | Yes | Deletes customer |
| Admins Link | `a[href="/en/admin/management"]` | Anchor | Yes | Navigates to Admins |
| Add Admin Btn | `button[data-action="add-admin"]` | Button | Yes | Opens add admin modal |
| Admin Name | `input[name="adminName"]` | Text Input | Yes | Admin name field |
| Save Admin Btn | `button[data-action="save-admin"]` | Button | Yes | Saves admin |
| Edit Admin Btn | `button[data-action="edit-admin"]` | Button | Yes | Edits admin |
| Delete Admin Btn | `button[data-action="delete-admin"]` | Button | Yes | Deletes admin |
| Success Toast | `.toast-success, .success-message` | Element | Yes | Confirms action success |

---

## User Flows

### Flow 1: Admin Login and Overview
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "admin@mycoifeur.com"
3. Enter Admin Password: "AdminPassword123!"
4. Click "Login Button"
5. Click "Overview Link"
6. Assert "Overview Chart" is visible

### Flow 2: Bookings Management (Edit and Delete)
1. Navigate to `/en/admin/bookings`
2. Click "Edit Booking Btn" on the first item
3. Click "Confirm Delete Btn" to save changes (or save button)
4. Click "Delete Booking Btn" on the first item
5. Click "Confirm Delete Btn"
6. Assert "Success Toast" is visible

### Flow 3: Customers Management (CRUD)
1. Navigate to `/en/admin/customers`
2. Click "Add Customer Btn"
3. Enter Customer Name: "Test Customer QA"
4. Click "Save Customer Btn"
5. Assert "Success Toast" is visible
6. Click "Edit Customer Btn"
7. Enter Customer Name: "Test Customer QA Updated"
8. Click "Save Customer Btn"
9. Click "Delete Customer Btn"
10. Click "Confirm Delete Btn"
11. Assert "Success Toast" is visible

### Flow 4: Admin Management (CRUD)
1. Navigate to `/en/admin/management`
2. Click "Add Admin Btn"
3. Enter Admin Name: "QA Super Admin"
4. Click "Save Admin Btn"
5. Assert "Success Toast" is visible
6. Click "Edit Admin Btn"
7. Enter Admin Name: "QA Super Admin Edited"
8. Click "Save Admin Btn"
9. Click "Delete Admin Btn"
10. Click "Confirm Delete Btn"
11. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Admin Name | Required | "Name is required" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Delete Admin without confirmation | Should require confirmation |
