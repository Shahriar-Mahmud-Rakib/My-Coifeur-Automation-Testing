# Page: My Coifeur — Admin Bookings (Full E2E CRUD + Sales Report)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/bookings`
**Sales Report URL:** `https://dev.mycoifeur.com.sa/en/admin/bookings/sales-report`
**Type:** E2E Admin Bookings Flow (Login → Bookings Management → Sales Report)
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Bookings module — the central hub for managing all marketplace bookings.
Admin logs in with real credentials, navigates to Bookings page, manages orders via status filters,
performs CRUD actions (View Details, Assign to Another Provider, Delete), inspects booking detail cards
(Customer / Provider / Service / Payment), and manages the Sales Report with filters and export.

**API Endpoints:**
- `GET /api/v1/web/admin/orders` — list all bookings
- `GET /api/v1/web/admin/orders?status={status}` — filter by status
- `GET /api/v1/web/admin/orders/{id}` — booking detail
- `POST /api/v1/web/admin/orders/{id}/accept` — accept pending booking
- `POST /api/v1/web/admin/orders/{id}/reject` — reject pending booking
- `POST /api/v1/web/admin/orders/{id}/assign` — assign to another provider
- `DELETE /api/v1/web/admin/orders/{id}/delete` — soft delete booking
- `POST /api/v1/web/admin/orders/{id}/restore` — restore deleted booking
- `GET /api/v1/web/admin/sales-report` — sales report data
- `GET /api/v1/web/admin/sales-report/export` — export sales report

---

## UI Elements

### Login Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input#email, input[type="email"]` | Email Input | Yes | Real admin: amrmuhamed9@gmail.com |
| Admin Password | `input#password, input[type="password"]` | Password | Yes | Real password: 123456 |
| Login Button | `button:has-text("Sign in"), button[type="submit"]` | Submit Button | Yes | Submits admin login |

### Sidebar Navigation
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Overview Link | `a:has-text("Overview"), nav a[href*="/admin/overview"]` | Anchor | Yes | Dashboard overview |
| Bookings Link | `a:has-text("Bookings"), nav a[href*="/admin/bookings"]` | Anchor | Yes | Shows badge with count (e.g. "24") |
| Bookings Badge | `.badge, span:near(a:has-text("Bookings"))` | Badge | No | Booking count indicator |
| Providers Link | `a:has-text("Providers")` | Anchor | Yes | Sidebar nav |
| Customers Link | `a:has-text("Customers")` | Anchor | Yes | Sidebar nav |
| Finance Link | `a:has-text("Finance")` | Anchor | Yes | Sidebar nav |
| Admin Management Link | `a:has-text("Admin Management")` | Anchor | Yes | Sidebar nav |
| Categories Link | `a:has-text("Categories")` | Anchor | Yes | Sidebar nav |
| Promo Codes Link | `a:has-text("Promo Codes")` | Anchor | Yes | Sidebar nav |
| System Status | `text="System Status"` | Element | No | Shows "Operational" status at bottom |

### Bookings List Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Bookings"), h2:has-text("Bookings")` | Heading | Yes | "Bookings" |
| Page Description | `text="Operational view of all marketplace bookings"` | Text | Yes | Subtitle text |
| Sales Report Button | `button:has-text("Sales Report"), a:has-text("Sales Report")` | Button | Yes | Top-right, navigates to /admin/bookings/sales-report |
| Search Bar | `input[placeholder*="Search by user ID or salon ID"]` | Text Input | Yes | Filters bookings by user ID or salon ID |
| Status Filter Dropdown | `select, [role="combobox"]:near(text="All Status")` | Dropdown | Yes | Options: All Status, In Cart, On Hold, Admin Accepted, Admin Rejected, Artist Accepted, Artist Rejected, Cancelled by User |

### Bookings Table
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Table Header - Booking | `th:has-text("BOOKING"), th:has-text("Booking")` | Table Header | Yes | Booking reference ID column (#801, #10, etc.) |
| Table Header - Customer | `th:has-text("CUSTOMER")` | Table Header | Yes | Customer name + email |
| Table Header - Provider | `th:has-text("PROVIDER")` | Table Header | Yes | Provider name + email |
| Table Header - Service | `th:has-text("SERVICE")` | Table Header | Yes | Service name + duration |
| Table Header - Date & Time | `th:has-text("DATE & TIME"), th:has-text("DATE")` | Table Header | Yes | Scheduled date/time |
| Table Header - Status | `th:has-text("STATUS")` | Table Header | Yes | Status badge column |
| Table Header - Payment | `th:has-text("PAYMENT")` | Table Header | Yes | Paid / Pending badge |
| Table Header - Amount | `th:has-text("AMOUNT")` | Table Header | Yes | Currency amount (SAR) |
| Table Header - Actions | `th:has-text("ACTIONS")` | Table Header | Yes | 3-dot action menu column |
| Booking Row | `table tbody tr, [data-booking-id]` | Table Row | Yes | Each booking row |
| Booking ID | `table tbody tr td:first-child` | Cell | Yes | e.g. "#801" |
| Customer Name | `table tbody tr td:nth-child(2)` | Cell | Yes | Name + email displayed |
| Status Badge | `.badge, span:has-text("Admin Accepted"), span:has-text("Admin Rejected"), span:has-text("Artist Accepted"), span:has-text("Artist Rejected"), span:has-text("Artist on the way"), span:has-text("In Cart"), span:has-text("On Hold"), span:has-text("Cancelled by User")` | Badge | Yes | Color-coded status |
| Payment Badge | `span:has-text("Paid"), span:has-text("Pending")` | Badge | Yes | Payment status |
| Amount Value | `td:has-text("SAR"), td:has-text("0")` | Cell | Yes | Monetary amount with currency icon |
| Actions Menu Button | `button:has-text("..."), button[aria-label*="action"], td:last-child button` | Button | Yes | 3-dot "..." menu per row |
| Pagination Info | `text="Showing", text="Page"` | Element | No | e.g. "Showing 4 of 4 bookings (Page 1 of 1)" |
| Previous Page Button | `button:has-text("Previous")` | Button | No | Pagination |
| Next Page Button | `button:has-text("Next")` | Button | No | Pagination |

### Action Menu Dropdown (3-dot menu)
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| View Details | `button:has-text("View Details"), a:has-text("View Details"), [role="menuitem"]:has-text("View Details")` | Menu Item | Yes | Navigates to /admin/bookings/{id} |
| Assign to Another Provider | `button:has-text("Assign to Another Provider"), [role="menuitem"]:has-text("Assign")` | Menu Item | Yes | Opens assign provider dialog |
| Delete Booking | `button:has-text("Delete Booking"), [role="menuitem"]:has-text("Delete")` | Menu Item | Yes | Opens delete confirmation |

### Booking Detail Page (/admin/bookings/{id})
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Back to Bookings | `a:has-text("Back to bookings"), button:has-text("Back")` | Link | Yes | Returns to bookings list |
| Customer Details Card | `text="Customer Details", [data-section="customer"]` | Card | Yes | Name, email, phone, registration date, booking frequency |
| Customer Name | `div:near(text="Customer Details"):has-text("name")` | Text | Yes | Customer full name |
| Customer Email | `div:near(text="Customer Details"):has-text("@")` | Text | Yes | Customer email address |
| Customer Phone | `div:near(text="Customer Details"):has-text("phone")` | Text | No | Customer phone number |
| Provider Details Card | `text="Provider Details", [data-section="provider"]` | Card | Yes | Name, email, ratings, completed bookings |
| Provider Name | `div:near(text="Provider Details"):has-text("name")` | Text | Yes | Provider full name |
| Provider Email | `div:near(text="Provider Details"):has-text("@")` | Text | Yes | Provider email address |
| Provider Rating | `div:near(text="Provider Details") .stars, div:near(text="Provider Details"):has-text("rating")` | Element | No | Star rating display |
| Service Details Card | `text="Service Details", [data-section="service"]` | Card | Yes | Service name, duration, address, scheduled date/time |
| Service Name | `div:near(text="Service Details"):has-text("name")` | Text | Yes | Service name |
| Service Duration | `div:near(text="Service Details"):has-text("duration")` | Text | Yes | e.g. "2h", "4h 24m" |
| Service Location | `div:near(text="Service Details"):has-text("address")` | Text | No | Service location/address |
| Payment Details Card | `text="Payment Details", [data-section="payment"]` | Card | Yes | Amount, status, method |
| Payment Amount | `div:near(text="Payment Details"):has-text("amount")` | Text | Yes | Total booking cost |
| Payment Status | `div:near(text="Payment Details"):has-text("Pending"), div:near(text="Payment Details"):has-text("Paid")` | Badge | Yes | Pending / Paid |
| Payment Method | `div:near(text="Payment Details"):has-text("Cash"), div:near(text="Payment Details"):has-text("Card")` | Text | No | Cash / Card |

### Sales Report Page (/admin/bookings/sales-report)
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Back to Bookings | `a:has-text("Back to bookings")` | Link | Yes | Returns to bookings list |
| Sales Report Title | `h1:has-text("Sales Report"), h2:has-text("Sales Report")` | Heading | Yes | Page title |
| Refresh Button | `button:has-text("Refresh")` | Button | Yes | Reloads sales data |
| Export Button | `button:has-text("Export")` | Button | Yes | Downloads report as file |
| Service Provider Filter | `select:near(text="Service Provider"), [role="combobox"]:near(text="Service Provider")` | Dropdown | Yes | Filter by provider; default "All Providers" |
| Categories Filter | `select:near(text="Categories"), [role="combobox"]:near(text="Categories")` | Dropdown | Yes | Filter by category; default "All Categories" |
| Services Filter | `select:near(text="Services"), [role="combobox"]:near(text="Services")` | Dropdown | Yes | Filter by service; default "All Services" |
| Start Date Picker | `input[type="date"]:near(text="Start Date"), input[placeholder="mm/dd/yyyy"]:first-of-type` | Date Input | Yes | Start date range filter |
| End Date Picker | `input[type="date"]:near(text="End Date"), input[placeholder="mm/dd/yyyy"]:last-of-type` | Date Input | Yes | End date range filter |
| Reset Filters Button | `button:has-text("Reset Filters")` | Button | Yes | Clears all filters |
| Apply Filters Button | `button:has-text("Apply Filters")` | Button | Yes | Applies selected filters |
| Sales Table Header - Currency | `th:has-text("CURRENCY")` | Table Header | Yes | Currency column (SAR, Unknown) |
| Sales Table Header - Total Orders | `th:has-text("TOTAL ORDERS")` | Table Header | Yes | Total orders amount |
| Sales Table Header - Total Taxes | `th:has-text("TOTAL TAXES")` | Table Header | Yes | Taxes collected |
| Sales Table Header - Total Taxes for iCover | `th:has-text("TOTAL TAXES FOR ICOVER")` | Table Header | Yes | iCover tax amount |
| Sales Table Header - Total Taxes Paid in Cash | `th:has-text("TOTAL TAXES PAID IN CASH")` | Table Header | Yes | Cash tax payments |
| Sales Data Row | `table tbody tr` | Table Row | Yes | e.g. SAR / Unknown currency rows |

---

## Requirements
- REQ-001: Admin can log in with valid credentials and see the Overview dashboard
- REQ-002: Admin can navigate to Bookings page via sidebar
- REQ-003: Bookings page shows all bookings in a table with correct columns
- REQ-004: Admin can filter bookings by status (In Cart, On Hold, Admin Accepted, Admin Rejected, Artist Accepted, Artist Rejected, Cancelled by User)
- REQ-005: Admin can search bookings by user ID or salon ID
- REQ-006: Admin can view booking details via 3-dot menu → View Details
- REQ-007: Booking detail page shows 4 cards: Customer, Provider, Service, Payment
- REQ-008: Admin can assign booking to another provider via 3-dot menu
- REQ-009: Admin can delete a booking via 3-dot menu → Delete Booking
- REQ-010: Admin can access Sales Report page from the Sales Report button
- REQ-011: Sales Report can be filtered by Service Provider, Categories, Services, Date Range
- REQ-012: Sales Report can be exported
- REQ-013: Sales Report can be refreshed
- REQ-014: Bookings table supports pagination
- REQ-015: Status badges are color-coded (green for accepted, red for rejected, etc.)

---

## User Flows

### Flow 1: Admin Login and Navigate to Bookings
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin-login`
2. Fill `input#email` with "amrmuhamed9@gmail.com"
3. Fill `input#password` with "123456"
4. Click `button:has-text("Sign in")`
5. Assert URL contains "/admin/overview" (login succeeded)
6. Assert sidebar shows "Bookings" link with badge count
7. Click "Bookings" link in sidebar
8. Assert URL contains "/admin/bookings"
9. Assert page heading "Bookings" is visible
10. Assert "Sales Report" button is visible at top-right
11. Assert bookings table has rows with columns: BOOKING, CUSTOMER, PROVIDER, SERVICE, DATE & TIME, STATUS, PAYMENT, AMOUNT, ACTIONS

### Flow 2: Filter Bookings by Status — In Cart
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/bookings`
3. Click the Status dropdown (default: "All Status")
4. Select "In Cart"
5. Assert table updates to show only bookings with "In Cart" status badge
6. Assert each visible row's STATUS column contains "In Cart"

### Flow 3: Filter Bookings by Status — On Hold
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "On Hold"
4. Assert table shows only "On Hold" status bookings
5. Verify table or "no results" message displays correctly

### Flow 4: Filter Bookings by Status — Admin Accepted
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "Admin Accepted"
4. Assert table shows only bookings with green "Admin Accepted" badge
5. Assert booking count updates in pagination info

### Flow 5: Filter Bookings by Status — Admin Rejected
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "Admin Rejected"
4. Assert table shows only bookings with red "Admin Rejected" badge

### Flow 6: Filter Bookings by Status — Artist Accepted
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "Artist Accepted"
4. Assert table shows only "Artist Accepted" status bookings

### Flow 7: Filter Bookings by Status — Artist Rejected
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "Artist Rejected"
4. Assert table shows only "Artist Rejected" status bookings

### Flow 8: Filter Bookings by Status — Cancelled by User
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Open Status dropdown, select "Cancelled by User"
4. Assert table shows only "Cancelled by User" status bookings or empty state

### Flow 9: Search Bookings by User ID
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Type "801" into the search bar
4. Assert table filters to show booking #801
5. Assert other bookings are hidden
6. Clear search bar
7. Assert all bookings reappear

### Flow 10: Search Bookings by Salon ID
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Type a known salon/user ID into search
4. Assert table filters accordingly

### Flow 11: View Booking Details via 3-dot Menu
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Click the "..." (3-dot) action button on the first booking row
4. Assert dropdown menu appears with: "View Details", "Assign to Another Provider", "Delete Booking"
5. Click "View Details"
6. Assert URL changes to `/admin/bookings/{id}`
7. Assert "Back to bookings" link is visible
8. Assert "Customer Details" card is visible with name and email
9. Assert "Provider Details" card is visible with name and email
10. Assert "Service Details" card is visible with service name and duration
11. Assert "Payment Details" card is visible with amount and status

### Flow 12: Navigate Back from Booking Details
1. Login as admin
2. Navigate to a booking detail page
3. Click "Back to bookings" link
4. Assert URL returns to `/admin/bookings`
5. Assert bookings table is visible again

### Flow 13: Assign Booking to Another Provider
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Click "..." on a booking row
4. Click "Assign to Another Provider"
5. Assert assign dialog/modal appears
6. Select a different provider from the list (if available)
7. Confirm assignment
8. Assert success feedback (toast or status change)

### Flow 14: Delete Booking
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Click "..." on a booking row
4. Click "Delete Booking"
5. Assert confirmation modal/dialog appears
6. Click confirm delete button
7. Assert success toast or booking removed from list
8. Assert bookings count decreases

### Flow 15: Navigate to Sales Report
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Click "Sales Report" button (top-right)
4. Assert URL contains "/admin/bookings/sales-report"
5. Assert "Sales Report" heading is visible
6. Assert Refresh and Export buttons are visible
7. Assert filter section with Service Provider, Categories, Services, Start Date, End Date is visible
8. Assert Reset Filters and Apply Filters buttons are visible
9. Assert sales summary table is visible with columns: CURRENCY, TOTAL ORDERS, TOTAL TAXES, TOTAL TAXES FOR ICOVER, TOTAL TAXES PAID IN CASH

### Flow 16: Sales Report — Filter by Service Provider
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Service Provider" dropdown
4. Select a specific provider
5. Click "Apply Filters"
6. Assert table data updates to reflect the selected provider
7. Click "Reset Filters"
8. Assert filters return to defaults (All Providers)

### Flow 17: Sales Report — Filter by Category
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Categories" dropdown
4. Select a specific category
5. Click "Apply Filters"
6. Assert table data updates

### Flow 18: Sales Report — Filter by Service
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Services" dropdown
4. Select a specific service
5. Click "Apply Filters"
6. Assert table data updates

### Flow 19: Sales Report — Filter by Date Range
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Set Start Date to a past date (e.g., "01/01/2026")
4. Set End Date to today's date
5. Click "Apply Filters"
6. Assert table data updates to show only orders within that range

### Flow 20: Sales Report — Combined Filters
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Select a specific Service Provider
4. Select a specific Category
5. Set Start Date and End Date
6. Click "Apply Filters"
7. Assert table data reflects all combined filter criteria
8. Click "Reset Filters"
9. Assert all dropdowns reset to "All" and dates are cleared

### Flow 21: Sales Report — Export
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Export" button
4. Assert file download initiates (check download response or network request)

### Flow 22: Sales Report — Refresh
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Refresh" button
4. Assert table data reloads (network request fires)

### Flow 23: Sales Report — Back to Bookings
1. Login as admin
2. Navigate to `/en/admin/bookings/sales-report`
3. Click "Back to bookings" link
4. Assert URL returns to `/admin/bookings`

### Flow 24: Bookings Table — Verify Status Color Coding
1. Login as admin
2. Navigate to `/en/admin/bookings`
3. Assert "Admin Accepted" badges have green color
4. Assert "Admin Rejected" badges have red color
5. Assert "Artist Accepted" badges have distinct color
6. Assert "Artist Rejected" badges have red-toned color
7. Assert "Pending" payment badges and "Paid" badges are visually distinct

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Admin Email | Required, valid email format | "Email is required" |
| Admin Password | Required, min 6 characters | "Password is required" |
| Login Credentials | Must match valid admin account | "Invalid credentials" or "Please check your credentials" |
| Search Bar | Accepts numeric/text; filters dynamically | — |
| Status Filter | Must select from dropdown options | — |
| Reject Reason Input | Required when rejecting a booking | "Rejection reason is required" |
| Assign Provider | Must select a valid provider | "Please select a provider" |
| Delete Confirmation | Must click confirm in modal | — |
| Sales Start Date | Must be before End Date | "Start date must be before end date" |
| Sales End Date | Must be after Start Date | "End date must be after start date" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Filter by status with no matching bookings | Empty state message or "No bookings found" |
| EC-02 | Search with non-existent ID (e.g. "99999") | Empty table, no crash |
| EC-03 | Access bookings URL without login | Redirect to /admin-login with session_expired param |
| EC-04 | Delete last remaining booking | Bookings table shows empty state |
| EC-05 | Assign booking to same provider | Should show error or no-op |
| EC-06 | Search with special characters (<script>alert(1)</script>) | No XSS execution, input sanitized |
| EC-07 | Filter by status then search — combined filtering | Both filters work together |
| EC-08 | Navigate directly to /admin/bookings/999999 (non-existent) | 404 page or error message |
| EC-09 | Sales Report with no data in date range | Empty table with zero values |
| EC-10 | Sales Export with no data | Export generates empty/minimal file |
| EC-11 | Rapid clicking on action menu | Menu opens/closes without duplicates |
| EC-12 | Login with wrong password | Error message shown, stays on login page |
| EC-13 | Login with empty fields | Validation error messages shown |
| EC-14 | Double-click Delete on same booking | Only one delete request, no 500 error |
| EC-15 | Switch between status filters rapidly | Table updates correctly without stale data |
| EC-16 | Pagination — navigate to next/previous page | Table shows correct page data |

---

## Test Data
| Category | Value |
|---|---|
| Admin Email | amrmuhamed9@gmail.com |
| Admin Password | 123456 |
| Valid Booking ID | 801 |
| Valid Booking ID 2 | 9 |
| Search - User ID | 80 |
| Search - Non-existent | 99999 |
| Status - Admin Accepted | Admin Accepted |
| Status - Admin Rejected | Admin Rejected |
| Status - Artist Accepted | Artist Accepted |
| Status - Artist Rejected | Artist Rejected |
| Status - Artist on the way | Artist on the way |
| Status - In Cart | In Cart |
| Status - On Hold | On Hold |
| Status - Cancelled by User | Cancelled by User |
| XSS Payload | <script>alert(1)</script> |
| SQL Injection Payload | ' OR 1=1 -- |
| Start Date | 01/01/2026 |
| End Date | 12/31/2026 |
| Currency - SAR | SAR |
| Currency - Unknown | Unknown |

---

## Don't Test
- Do NOT test browser-use autonomous walk (QA-19) — admin pages are behind auth
- Do NOT actually delete production bookings without restore
