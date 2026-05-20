# Page: My Coifeur — Admin Contact Requests (Support Tickets)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/contact-requests`
**Type:** E2E Admin Contact Requests Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Contact Requests module. Admins view, inspect, delete, and manage customer & provider support inquiries/tickets.

**API Endpoints:**
- `GET /api/v1/admin/contact_us` — list support tickets
- `GET /api/v1/admin/contact_us/{id}/show` — show ticket detail
- `DELETE /api/v1/admin/contact_us/{id}/delete` — delete resolved ticket

---

## UI Elements

### Contact Requests Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Contact Requests")` | Heading | Yes | Title "Contact Requests" |
| Search Input | `input[placeholder*="Search tickets..."]` | Text Input | Yes | Filters tickets |
| Requests Table | `table` | Table | Yes | Customer message grid |
| Table Columns | `th` | Header | Yes | Columns: NAME, EMAIL, PHONE, SUBJECT, MESSAGE, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| View Ticket | `[role="menuitem"]:has-text("View Ticket")` | Menu Item | Yes | Opens message details modal |
| Delete Ticket | `[role="menuitem"]:has-text("Delete Ticket")` | Menu Item | Yes | Deletes ticket |

### View Ticket Details Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Sender Name | `.sender-name, h3` | Text | Yes | Sender's Name |
| Sender Email | `.sender-email, p` | Text | Yes | Sender's Email |
| Message Body | `.message-body, p` | Text | Yes | Full message text |
| Close Modal | `button:has-text("Close")` | Button | Yes | Dismiss details |

---

## User Flows

### Flow 1: List Contact Requests and Verify Columns
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/contact-requests`
3. Assert page title "Contact Requests" is visible
4. Assert table columns exist: NAME, EMAIL, PHONE, SUBJECT, MESSAGE, ACTIONS

### Flow 2: Search Tickets by Sender Name
1. Login as admin
2. Navigate to `/en/admin/contact-requests`
3. Type a known sender's name in search input
4. Assert only matching rows are displayed
5. Clear search input and assert all rows reappear

### Flow 3: View Contact Request Details via Modal
1. Login as admin
2. Navigate to `/en/admin/contact-requests`
3. Click 3-dot Actions menu on a ticket row
4. Select "View Ticket"
5. Assert Details modal appears with full message text, sender name, and email
6. Click "Close" to close modal

### Flow 4: Delete Support Ticket
1. Login as admin
2. Navigate to `/en/admin/contact-requests`
3. Click Actions -> Delete Ticket on a row
4. Confirm delete action in dialog
5. Assert success toast is shown and ticket is removed from list

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Delete Confirmation | Required | Action must be confirmed |

---

## Edge Cases
- EC-01: Delete already resolved/deleted ticket (handled gracefully, returns 404/no crash)
- EC-02: Search with script payload (sanitized)
- EC-03: Access without authentication (redirect to login)
