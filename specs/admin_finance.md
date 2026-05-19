# Page: My Coifeur — Admin Finance (Wallet & Payouts)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Finance Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Finance module covering:
- Withdrawal/Balance requests approval & rejection
- Direct payout transfer (Send money to provider/user)
- Viewing Payment logs and Commissions list
- Sales reports filters (categories, salons, services, date ranges)

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Finance Link | `a[href*="/finance"], a[href*="/wallet"]` | Anchor | Yes | Sidebar finance link |
| Balance Requests Tab | `[data-tab="balances"], button:has-text("Withdrawal Requests")` | Tab/Button | Yes | List salon withdrawal requests |
| First Accept Request Btn | `(.accept-balance, button[data-action="accept"])[0]` | Button | Yes | Accept balance request |
| First Reject Request Btn | `(.reject-balance, button[data-action="reject"])[0]` | Button | Yes | Reject balance request |
| Reject Reason Input | `textarea[name="reason"], textarea[placeholder*="Reason"]` | Text Area | Yes | Rejection reason field |
| Confirm Reject Btn | `button[data-action="confirm-reject"], button:has-text("Confirm Reject")` | Button | Yes | Submits withdrawal rejection |
| Send Money Btn | `button[data-action="send-money"], button:has-text("Send Money")` | Button | Yes | Opens manual payout form |
| Recipient ID Input | `input[name="user_id"], select[name="user_id"]` | Input/Select | Yes | Recipient provider or user ID |
| Payout Amount Input | `input[name="amount"], input[type="number"]` | Number Input | Yes | Amount in SAR |
| Transfer Note Input | `input[name="note"], textarea[name="note"]` | Text Input | Yes | Note/Description for payout |
| Submit Payout Btn | `button[data-action="submit-payout"], button:has-text("Transfer")` | Button | Yes | Executes transaction payout |
| Reports Tab | `[data-tab="reports"], button:has-text("Reports")` | Tab/Button | Yes | Navigates to Sales Reports |
| Date From Input | `input[name="from"], input[type="date"]:first-of-type` | Date Input | Yes | Sales report filter start date |
| Date To Input | `input[name="to"], input[type="date"]:last-of-type` | Date Input | Yes | Sales report filter end date |
| Apply Filters Btn | `button[data-action="apply-filter"], button:has-text("Apply")` | Button | Yes | Updates reports view |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Approve Payout/Withdrawal Request
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Finance Link"
6. Click "Balance Requests Tab"
7. Click "First Accept Request Btn"
8. Assert "Success Toast" is visible

### Flow 2: Reject Withdrawal Request with Reason
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Finance Link"
6. Click "Balance Requests Tab"
7. Click "First Reject Request Btn"
8. Enter Reject Reason Input: "Invalid bank account details provided"
9. Click "Confirm Reject Btn"
10. Assert "Success Toast" is visible

### Flow 3: Send Money (Manual Payout)
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Finance Link"
6. Click "Send Money Btn"
7. Enter Recipient ID Input: "1"
8. Enter Payout Amount Input: "250.00"
9. Enter Transfer Note Input: "Manual payout test"
10. Click "Submit Payout Btn"
11. Assert "Success Toast" is visible

### Flow 4: Filter Sales Report by Date Range
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Finance Link"
6. Click "Reports Tab"
7. Enter Date From Input: "2026-01-01"
8. Enter Date To Input: "2026-12-31"
9. Click "Apply Filters Btn"
10. Assert reports data updates successfully without errors

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Payout Amount Input | Greater than 0 | "Amount must be a positive number" |
| Reject Reason Input | Required on rejection | "Reason is required" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Send negative amount payout | Validation error should block action |
| EC-02 | Withdrawal reject without comment reason | UI alerts user to enter reason |
