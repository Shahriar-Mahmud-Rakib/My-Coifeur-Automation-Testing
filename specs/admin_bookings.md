# Page: My Coifeur — Admin Bookings (Orders CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Bookings Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Bookings (Orders) module, covering:
- Viewing Bookings (All, Pending, Other, Carts)
- Booking Status Actions (Accept pending, Reject with reason, Assign to Salon)
- Deleting and Restoring Bookings

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Bookings Link | `a[href*="/bookings"], a[href*="/orders"]` | Anchor | Yes | Sidebar bookings menu |
| Pending Bookings Tab | `[data-tab="pending"], button:has-text("Pending")` | Tab/Button | Yes | Switch to Pending bookings list |
| Other Bookings Tab | `[data-tab="other"], button:has-text("Other")` | Tab/Button | Yes | Switch to Other bookings list |
| Carts Tab | `[data-tab="carts"], button:has-text("Carts")` | Tab/Button | Yes | Switch to Carts list |
| First Booking Card | `(.booking-item, tr.booking-row)[0]` | Element | Yes | The first booking in the list |
| Accept Booking Btn | `button[data-action="accept"], .accept-btn, button:has-text("Accept")` | Button | Yes | Accept action for pending booking |
| Reject Booking Btn | `button[data-action="reject"], .reject-btn, button:has-text("Reject")` | Button | Yes | Reject action for pending booking |
| Reject Reason Input | `textarea[name="reject_reason"], textarea[placeholder*="Reason"]` | Text Area | Yes | Rejection reason comment |
| Submit Rejection Btn | `button[data-action="submit-reject"], button:has-text("Confirm Reject")` | Button | Yes | Submits rejection reason form |
| Assign Salon Btn | `button[data-action="assign"], .assign-btn, button:has-text("Assign")` | Button | Yes | Opens Assign Salon form/modal |
| Salon Select Dropdown | `select[name="salon_id"], .salon-dropdown` | Select | Yes | Dropdown to choose provider/salon |
| Confirm Assign Btn | `button[data-action="confirm-assign"], button:has-text("Assign Salon")` | Button | Yes | Confirms assignment |
| Delete Booking Btn | `button[data-action="delete"], .delete-btn` | Button | Yes | Opens booking delete confirmation |
| Confirm Delete Btn | `button[data-action="confirm-delete"], button:has-text("Yes, Delete")` | Button | Yes | Confirms booking deletion |
| Restore Booking Btn | `button[data-action="restore"], .restore-btn` | Button | No | Restores soft-deleted booking |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms action success |

---

## User Flows

### Flow 1: Accept Pending Booking
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Bookings Link"
6. Click "Pending Bookings Tab"
7. Click "Accept Booking Btn" on the first item
8. Assert "Success Toast" is visible

### Flow 2: Reject Pending Booking with Reason
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Bookings Link"
6. Click "Pending Bookings Tab"
7. Click "Reject Booking Btn" on the first item
8. Enter Reject Reason Input: "Testing booking rejection functionality"
9. Click "Submit Rejection Btn"
10. Assert "Success Toast" is visible

### Flow 3: Assign Booking to a Salon/Provider
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Bookings Link"
6. Click "First Booking Card"
7. Click "Assign Salon Btn"
8. Select Salon Select Dropdown option with value or text
9. Click "Confirm Assign Btn"
10. Assert "Success Toast" is visible

### Flow 4: Delete & Restore Booking
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Bookings Link"
6. Click "Delete Booking Btn" on the first item
7. Click "Confirm Delete Btn"
8. Assert "Success Toast" is visible
9. Click "Restore Booking Btn" (if visible/available) to revert deletion
10. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Reject Reason Input | Required when rejecting | "Rejection reason is required" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Rejection without comment reason | Form should display validation error |
| EC-02 | View Details of non-existent booking | Displays 404 page / error toast |
