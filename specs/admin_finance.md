# Page: My Coifeur — Admin Finance (Wallet, Commission & Payouts)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/finance`
**Type:** E2E Admin Finance Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Finance module. Admins manage wallet balances, process payouts, verify payout requests (Withdrawal), manage commissions, and inspect reports.

**API Endpoints:**
- `GET /api/v1/web/admin/wallet/balances` — list withdrawal requests
- `POST /api/v1/web/admin/wallet/balances/{id}/accept` — accept payout request
- `POST /api/v1/web/admin/wallet/balances/{id}/reject` — reject payout request
- `POST /api/v1/web/admin/wallet/send-money` — process manual transfer
- `GET /api/v1/web/admin/commissions` — list commissions

---

## UI Elements

### Finance Page Layout
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Finance")` | Heading | Yes | Title "Finance" |
| Send Money Btn | `button:has-text("Send Money")` | Button | Yes | Open manual transfer form |
| Wallet Tab | `[role="tab"]:has-text("Wallet")` | Tab | Yes | Wallet balances list |
| Withdrawal Requests Tab | `[role="tab"]:has-text("Withdrawal Requests")` | Tab | Yes | Pending payouts list |
| Commission Tab | `[role="tab"]:has-text("Commission")` | Tab | Yes | Commissions dashboard |
| Payout Requests Table | `table` | Table | Yes | List of payouts |
| Table Columns | `th` | Header | Yes | Columns: PROVIDER, AMOUNT, REQUEST DATE, STATUS, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Send Money / Manual Payout Form (Modal)
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Recipient Dropdown | `select[name="recipient"], select[name="salon_id"]` | Select | Yes | Choose salon to pay |
| Payout Amount Input | `input[name="amount"]` | Number | Yes | Transfer amount in SAR |
| Transfer Note | `textarea[name="note"]` | Text Area | No | Transfer note/details |
| Submit Payout | `button:has-text("Send"), button[type="submit"]` | Button | Yes | Submit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close |

---

## User Flows

### Flow 1: Verify Finance Tabs and Balances
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/finance`
3. Assert page title "Finance" is visible
4. Assert tabs exist: Wallet, Withdrawal Requests, Commission

### Flow 2: View Withdrawal Payout Requests Table
1. Login as admin
2. Navigate to `/en/admin/finance`
3. Click "Withdrawal Requests" tab
4. Assert table shows columns: PROVIDER, AMOUNT, REQUEST DATE, STATUS, ACTIONS

### Flow 3: Accept Pending Withdrawal Payout
1. Login as admin
2. Navigate to `/en/admin/finance`
3. Click "Withdrawal Requests" tab
4. Click Actions -> Accept Payout on a pending row
5. Confirm action in dialog
6. Assert success toast and status updates to "Paid"

### Flow 4: Reject Pending Withdrawal Payout with Reason
1. Login as admin
2. Navigate to `/en/admin/finance`
3. Click "Withdrawal Requests" tab
4. Click Actions -> Reject Payout
5. Fill "Reject Reason Input" with "Invalid bank data"
6. Click "Confirm Reject"
7. Assert success toast and status updates to "Rejected"

### Flow 5: Send Manual Payout (Send Money)
1. Login as admin
2. Navigate to `/en/admin/finance`
3. Click "Send Money" button
4. Assert modal opens
5. Select a recipient from dropdown
6. Fill amount "100" and add note "QA test payout"
7. Click "Submit Payout"
8. Assert success toast and transaction appears in wallet list

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Recipient Dropdown | Required | "Please select a provider" |
| Payout Amount Input | Required, positive value > 0 | "Amount must be greater than 0" |
| Reject Reason Input | Required on reject | "Reason is required" |

---

## Edge Cases
- EC-01: Transfer negative amount (blocked by form validation)
- EC-02: Accept already-processed payout (not visible/possible)
- EC-03: Access without authentication (redirect to login)
