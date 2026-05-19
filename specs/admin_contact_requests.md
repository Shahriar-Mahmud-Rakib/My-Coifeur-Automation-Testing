# Page: My Coifeur — Admin Contact Requests (Support Tickets)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Contact Requests Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Contact Requests (Support Tickets) module covering:
- Viewing incoming contact inquiries/messages
- Replying/Responding to a contact request
- Resolving/Updating status of contact inquiries

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Contacts Link | `a[href*="/contacts"], a[href*="/contact-requests"]` | Anchor | Yes | Sidebar contact inquiries link |
| First Inquire Card | `(.contact-item, tr.inquiry-row)[0]` | Element | Yes | The first contact request in the list |
| View Inquire Btn | `button[data-action="view"], .view-btn, button:has-text("View")` | Button | Yes | Opens contact details modal |
| Reply Message Input | `textarea[name="reply_message"], textarea[placeholder*="Reply"]` | Text Area | Yes | Form input to draft support response |
| Submit Reply Btn | `button[data-action="send-reply"], button:has-text("Send Reply")` | Button | Yes | Dispatches reply email to user |
| Status Select | `select[name="status"], .status-dropdown` | Select | Yes | Updates ticket status (Pending, In-Progress, Resolved) |
| Save Status Btn | `button[data-action="save-status"], button:has-text("Save Status")` | Button | Yes | Commits ticket status changes |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Reply to Support Contact Request
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Contacts Link"
6. Click "View Inquire Btn" on the first contact request item
7. Enter Reply Message Input: "Hello, we have received your request and our technical team is investigating."
8. Click "Submit Reply Btn"
9. Assert "Success Toast" is visible

### Flow 2: Update Inquiry Status to Resolved
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Contacts Link"
6. Click "First Inquire Card"
7. Select Status Select: Resolved ("resolved")
8. Click "Save Status Btn"
9. Assert "Success Toast" is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Reply Message Input | Required | "Reply message content cannot be empty" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Submit empty reply message draft | Form validation should block submit |
| EC-02 | Modify ticket status without saving | Warning should show when navigating away, or no status change committed |
