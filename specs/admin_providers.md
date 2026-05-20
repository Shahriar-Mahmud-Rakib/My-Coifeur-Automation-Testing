# Page: My Coifeur — Admin Providers (Salon Management CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/providers`
**Type:** E2E Admin Providers Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Providers (Salons) module. Admins manage service providers, view detail tabs (Gallery, Working Days), edit salon profiles, ban/restore accounts, set VIP status, and manage listings.

**API Endpoints:**
- `GET /api/v1/web/admin/salons` — list all salons
- `GET /api/v1/web/admin/salons?status={status}` — filter by status
- `PUT /api/v1/web/admin/salons/{id}` — edit salon details
- `POST /api/v1/web/admin/salons/{id}/ban` — ban provider
- `POST /api/v1/web/admin/salons/{id}/restore` — restore banned provider
- `POST /api/v1/web/admin/salons/{id}/vip` — toggle VIP status
- `GET /api/v1/web/admin/salons/{id}/working-days` — list salon schedule
- `DELETE /api/v1/web/admin/salons/gallery/{imgId}` — delete gallery image

---

## UI Elements

### Providers List Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Providers")` | Heading | Yes | Title "Providers" |
| Search Input | `input[placeholder*="Search by provider ID or name"]` | Text Input | Yes | Filters providers list |
| Status Tabs | `[role="tab"]` | Tab | Yes | Tabs: All, Approved, Pending, Rejected |
| Providers Table | `table` | Table | Yes | List of providers |
| Table Columns | `th` | Header | Yes | Columns: PROVIDER, EMAIL, PHONE, STATUS, VIP, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| View Details | `[role="menuitem"]:has-text("View Details")` | Menu Item | Yes | Open provider details |
| Edit Provider | `[role="menuitem"]:has-text("Edit Provider")` | Menu Item | Yes | Opens edit modal |
| Ban Provider | `[role="menuitem"]:has-text("Ban Provider")` | Menu Item | Yes | Opens ban dialog |
| Restore Provider | `[role="menuitem"]:has-text("Restore Provider")` | Menu Item | No | Only for banned providers |

### Edit Provider Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Salon Name Input | `input[name="name"]` | Text Input | Yes | Edit salon name |
| Salon Phone Input | `input[name="phone"]` | Text Input | Yes | Edit phone |
| VIP Toggle | `input[name="is_vip"]` | Checkbox | Yes | Toggle VIP badge |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit edit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close modal |

---

## User Flows

### Flow 1: List Providers and Verify Table
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/providers`
3. Assert page heading "Providers" is visible
4. Assert table columns exist: PROVIDER, EMAIL, PHONE, STATUS, VIP, ACTIONS

### Flow 2: Search Provider by Name
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Type a known provider name in search input
4. Assert only matching provider rows are displayed
5. Clear search input and assert all rows reappear

### Flow 3: Filter Providers by Status Tab — Pending
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click "Pending" status tab
4. Assert only pending status providers are displayed

### Flow 4: Filter Providers by Status Tab — Approved
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click "Approved" status tab
4. Assert only approved providers are listed

### Flow 5: Edit Provider Info via Modal
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click 3-dot Actions menu on a provider row
4. Select "Edit Provider"
5. Assert Edit modal appears
6. Change salon name to "QA Updated Salon"
7. Click "Save Changes"
8. Assert success toast is shown and table updates

### Flow 6: Toggle VIP Status in Modal
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click Actions -> Edit Provider
4. Toggle the "VIP Toggle" checkbox
5. Save changes and verify VIP pill is updated in table

### Flow 7: Ban Provider with Reason
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click Actions -> Ban Provider
4. Fill "Ban Reason Input" with "Violation of terms"
5. Click "Confirm Ban"
6. Assert success toast and status badge changes to "Banned"

### Flow 8: Restore Banned Provider
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Filter by "Rejected" or "Banned" status
4. Click Actions -> Restore Provider
5. Assert success toast and status badge updates to "Approved"

### Flow 9: View Salon Details Page
1. Login as admin
2. Navigate to `/en/admin/providers`
3. Click Actions -> View Details
4. Assert URL contains `/admin/providers/`
5. Assert detail cards (Overview, Services, Gallery, Working Days) exist

### Flow 10: View Provider Schedule (Working Days)
1. Login as admin
2. Navigate to provider details page
3. Click "Working Days" tab
4. Assert schedule table (Monday-Sunday, timeslots) is visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Salon Name Input | Required | "Salon name is required" |
| Ban Reason Input | Required on ban | "Reason is required" |

---

## Edge Cases
- EC-01: Ban already banned provider (should not be allowed/visible)
- EC-02: Search with special characters (sanitized, empty state)
- EC-03: Access without authentication (redirect to login)
