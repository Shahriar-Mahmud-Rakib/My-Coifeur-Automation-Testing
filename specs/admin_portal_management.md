# Page: My Coifeur — Super Admin Web Management Portal
**URL:** `https://dev.mycoifeur.com.sa/en/admin/overview` (and `/settings`, `/salons`, `/users`, `/admins`, `/financial`, `/banks`, `/categories`, `/orders`)
**Type:** Internal Operations & Marketplace Administration
**Priority:** P0 — Core platform governance; allows Super Admins to monitor platform vitals, manage general/connection/mail settings, approve prospective salon partners, manage registered users, and oversee financial settlements.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

The central command and control center for platform Administrators. Enables high-level marketplace governance: configuring app settings (maintenance mode, SMS/SMTP gateways), reviewing commercial registrations (CR) for new salon partners, managing user accounts, auditing platform orders, configuring global service categories, and managing financial commissions & bank settlements.

---

## UI Elements — Admin Portal Sidebar Navigation

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Dashboard Overview Link | `a[href="/en/admin/overview"]` | Anchor | Always | Platform metrics, revenue, active bookings |
| App Settings Link | `a[href="/en/admin/settings"]` | Anchor | Always | General, connection, contacts, mail settings |
| Salon Management Link | `a[href="/en/admin/salons"]` | Anchor | Always | Review CR, approve/suspend partner salons |
| User Management Link | `a[href="/en/admin/users"]` | Anchor | Always | Manage clients, inspect profiles, ban/unban |
| Admin Hierarchy Link | `a[href="/en/admin/admins"]` | Anchor | Always | Manage Super Admins, Managers, Support staff |
| Global Categories Link | `a[href="/en/admin/categories"]`| Anchor | Always | Master service categories & tags |
| Platform Orders Link | `a[href="/en/admin/orders"]` | Anchor | Always | Master ledger of all marketplace bookings |
| Financial & Commission | `a[href="/en/admin/financial"]` | Anchor | Always | Commission splits, platform fees, payouts |
| Supported Banks Link | `a[href="/en/admin/banks"]` | Anchor | Always | Bank accounts and settlement gateways |
| Content & Blogs Link | `a[href="/en/admin/content"]` | Anchor | Always | Manage FAQ, Terms, Privacy, Marketing blogs |

---

## UI Elements — Admin Settings Form (`/en/admin/settings`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| General Settings Tab | `button[data-slot="tab-general"]` | Tab | Always | App name, maintenance toggle |
| Connection Settings Tab| `button[data-slot="tab-connection"]`| Tab | Always | SMS provider (Twilio, Unifonic, etc.) |
| Contact Settings Tab | `button[data-slot="tab-contacts"]` | Tab | Always | Support email & hotline phone |
| Mail Provider Settings Tab| `button[data-slot="tab-mail"]` | Tab | Always | SMTP host, port, encryption |
| App Name Input | `input[name="appName"]` | Text Input | Yes | E.g. "MyCoifeur" |
| Maintenance Mode Toggle| `input[name="maintenanceMode"]` | Toggle | Yes | Toggles entire platform maintenance banner |
| Support Email Input | `input[name="supportEmail"]` | Email Input| Yes | E.g. "support@mycoifeur.com" |
| Support Phone Input | `input[name="supportPhone"]` | Tel Input | Yes | E.g. "966920000000" |
| SMS Provider Select | `select[name="smsProvider"]` | Select | Yes | Twilio, Unifonic, Infobip |
| SMTP Host Input | `input[name="smtpHost"]` | Text Input | Yes | E.g. "smtp.mycoifeur.com" |
| SMTP Port Input | `input[name="smtpPort"]`, `type="number"`| Number Input| Yes | E.g. 587, 465 |
| Save Settings Button | `button[type="submit"]`, `text="Save Settings"`| Submit Button| Yes | Commits configuration changes |

---

## UI Elements — Salon Approval & Management (`/en/admin/salons`)

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Salon Partner Table | `table[data-slot="salons-table"]` | Table | Always | Paginated list of registered salons |
| Status Badge | `span[data-slot="salon-status"]` | Badge | Always | Pending (Orange), Active (Green), Suspended (Red) |
| Inspect Salon Profile CTA| `button[data-slot="inspect-salon"]` | Action Button| Always | Opens detailed audit sheet for salon |
| Approve Partner CTA | `button[data-slot="approve-salon"]` | Action Button| Pending | Verifies CR and activates salon profile |
| Suspend Salon CTA | `button[data-slot="suspend-salon"]` | Action Button| Active | Halts public booking and removes from grid |

---

## UI Elements — Financial Settlements & Banks (`/en/admin/banks`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Add Bank Button | `button[data-slot="add-bank-trigger"]` | Button | Always | Opens bank gateway creation modal |
| Bank Name Input | `input[name="bankName"]` | Text Input | Yes | E.g. "Al Rajhi Bank", "SNB" |
| IBAN Code Input | `input[name="iban"]`, `maxlength="34"` | Text Input | Yes | Standard Saudi IBAN (`SAxxxxxxxx`) |
| Save Bank Gateway Button| `button[type="submit"]` | Submit Button| Yes | Adds bank to financial ledger |

---

## User Flows

### Flow 1: Update Platform General Settings & Maintenance Mode
```
1. Authenticated Super Admin navigates to https://dev.mycoifeur.com.sa/en/admin/settings
2. Under "General Settings" tab, verify App Name is "MyCoifeur"
3. Toggle "Maintenance Mode" from Inactive to Active
4. Update Support Email to "support.lead@mycoifeur.com"
5. Click "Save Settings" button
6. Success toast appears: "Configuration updated successfully!"
7. Open new guest incognito tab to https://dev.mycoifeur.com.sa
8. Verify platform displays elegant Maintenance Mode banner / lock screen
9. Return to Admin portal and toggle Maintenance Mode back to Inactive
```

### Flow 2: Review & Approve Prospective Salon Partner Application
```
1. Navigate to /en/admin/salons (Pending Salons tab)
2. Locate partner application row for "Glamour Beauty Salon" (CR: 1010123456)
3. Click "Inspect" button → Audit drawer opens displaying commercial registration details
4. Click "Approve Partner" button (`data-slot="approve-salon"`)
5. Confirmation prompt: "Are you sure you want to approve this salon? An activation email will be sent to the owner."
6. Click "Confirm Activation"
7. Status badge transitions instantly to "Active" (Green); salon becomes discoverable on marketplace
```

### Flow 3: Inspect Platform Financial Overview & Add Settlement Bank
```
1. Navigate to /en/admin/banks dashboard
2. Click "Add New Bank Gateway" button → Modal opens
3. Enter Bank Name: "Saudi National Bank (SNB)"
4. Enter valid Saudi IBAN: "SA1210000012345678901234"
5. Select Currency: "SAR"
6. Click "Save Bank Gateway" button
7. Success toast appears; new bank account rendered in active settlement accounts table
```

### Flow 4: User Profile Audit & Temporary Suspension
```
1. Navigate to /en/admin/users
2. Search for client phone: "501234567"
3. Click row to open audit history (bookings, cancellations, device logs)
4. Click "Suspend Account" trigger → Select reason: "Fraudulent bookings"
5. Account status transitions to "Suspended"; client active sessions terminated
```

---

## Validation Rules

| Field / Component | Rule | Error / Fallback State |
|---|---|---|
| SMTP Port | Must be valid integer between 1 - 65535 | "Please enter a valid network port" |
| Support Phone | Standard phone format, digits only | "Invalid telephone number" |
| IBAN Code | Must start with country prefix (e.g., SA) and match checksum | "Invalid IBAN format" |
| Admin Role Check | Actions require Super Admin role JWT claims | "403 Forbidden. Insufficient administrative privileges." |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-ADM-01 | SQL Injection in App Name: `MyCoifeur' OR 1=1--` | Sanitized securely, stored as literal string, no DB error |
| EC-ADM-02 | XSS payload in Bank Name: `<script>alert('bank')</script>`| HTML escaped during storage, no script execution in table view |
| EC-ADM-03 | Submitting SMTP port as string (e.g., `not-a-port`) | Rejected by numeric input constraint or backend schema |
| EC-ADM-04 | Client or Salon Owner attempting to access Admin portal | Blocked immediately with 401/403 Forbidden; redirected to home |
| EC-ADM-05 | Super Admin attempting to delete their own account | Action blocked: "Cannot self-delete active Super Admin session." |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/web/admin/settings` | Retrieves master platform configuration keys |
| PATCH | `/api/v1/web/admin/settings` | Updates general, connection, contacts, or mail settings |
| GET | `/api/v1/web/admin/salons` | Retrieves paginated master list of partner salons |
| PATCH | `/api/v1/web/admin/salons/{id}/status`| Updates salon operational status (Approve, Suspend) |
| POST | `/api/v1/web/admin/banks` | Adds new bank settlement account |

### Example Payload: Update Admin Settings
```json
{
  "app_name": "MyCoifeur",
  "maintenance_mode": false,
  "support_email": "support.lead@mycoifeur.com",
  "support_phone": "966920000000"
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid Admin Token | `Bearer <jwt_token>` | Super Admin session JWT |
| Valid App Name | `MyCoifeur` | Standard platform name |
| Valid Support Email| `support@mycoifeur.com` | Standard contact |
| Valid SMTP Port | `587` | Standard mail port |
| Invalid Port | `-1` or `99999` | Boundary negative test |
| SQLi String | `' OR 1=1--` | Security probe |
