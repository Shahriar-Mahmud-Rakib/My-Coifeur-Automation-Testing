# Page: My Coifeur — Admin Settings (System Configuration)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/settings`
**Type:** E2E Admin Settings Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Settings module. Admins configure general system values (localized titles, contact details, maps keys), email provider (SMTP details), connection integration, loyalty settings, and roles & permissions cards.

**API Endpoints:**
- `GET /api/v1/web/admin/settings` — list current configuration values
- `PUT /api/v1/web/admin/settings` — save new settings values
- `GET /api/v1/web/admin/settings/roles` — get user roles and permissions list
- `PUT /api/v1/web/admin/settings/roles/{id}` — configure permissions for a role

---

## UI Elements

### Settings Page Tabs Left Panel
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| General Settings Tab | `[role="tab"]:has-text("General Settings")` | Tab | Yes | Edit localized titles, contacts |
| Email Provider Tab | `[role="tab"]:has-text("Email Provider")` | Tab | Yes | SMTP configuration |
| Connection Settings Tab | `[role="tab"]:has-text("Connection Settings")` | Tab | Yes | App connections, external tokens |
| App Versions Tab | `[role="tab"]:has-text("App Versions")` | Tab | Yes | Version controls |
| Version Analytics Tab | `[role="tab"]:has-text("Version Analytics")` | Tab | Yes | Usage stats |
| Roles & Permissions Tab | `[role="tab"]:has-text("Roles & Permissions")` | Tab | Yes | RBAC access settings |

### General Settings Form
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Title in Arabic | `input[name="title_ar"]` | Text Input | Yes | Arabic localized title |
| Title in English | `input[name="title_en"]` | Text Input | Yes | English localized title |
| Content in Arabic | `textarea[name="content_ar"]` | Text Area | Yes | Localization content |
| Content in English | `textarea[name="content_en"]` | Text Area | Yes | Localization content |
| Google Maps API Key | `input[name="google_maps"]` | Text Input | Yes | Map integration key |
| Keywords | `input[name="keywords"]` | Text Input | Yes | Comma-separated SEO tags |
| Cash Payment Tax | `input[name="cash_tax"]` | Number Input | Yes | Tax rate for cash payments |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit general configuration |

### Roles & Permissions Tab Layout
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Super Admin Role Card | `div:has-text("Super Admin")` | Card | Yes | Full system rights description |
| Support Role Card | `div:has-text("Support")` | Card | Yes | Support rights description |
| Configure Role Button | `.role-card button:has-text("Configure")` | Button | Yes | Open role permissions modal |

### Configure Role Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Role Name * | `input[name="role_name"]` | Text Input | Yes | Edit role label |
| Enable All Switch | `.switch:has-text("Enable All")` | Toggle | Yes | Toggle all permissions |
| Accordion Group Header | `button:has-text("Settings & System")` | Button | Yes | Accordion list panel trigger |
| Permission Checkbox | `input[type="checkbox"]` | Checkbox | Yes | Toggle single permission |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit RBAC updates |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Dismiss |

---

## User Flows

### Flow 1: Navigate Tabs and Verify Layout
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/settings`
3. Click through Settings tabs: General Settings, Email Provider, Connection Settings, Roles & Permissions
4. Assert each form panel displays without crashing

### Flow 2: Update General Settings SEO & Content
1. Login as admin
2. Navigate to General Settings tab
3. Fill Title in English with "My Coifeur Salon Marketplace"
4. Fill Keywords with "salons, booking, grooming, hair care"
5. Click "Save Changes"
6. Assert success toast is shown and values persist

### Flow 3: Configure Roles & Permissions
1. Login as admin
2. Navigate to Roles & Permissions tab
3. Click "Configure" button on the "Support" card
4. Assert Configuration modal appears
5. Open "Settings & System" accordion group
6. Toggle "View settings" checkbox permission
7. Click "Save Changes"
8. Assert success toast is shown

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Title in English | Required | "English title is required" |
| Cash Payment Tax | Positive number >= 0 | "Tax must be greater than or equal to 0" |

---

## Edge Cases
- EC-01: Update Map API Key with invalid format (validates or saves as is)
- EC-02: Disable all permissions for Super Admin (should block to prevent lockout)
- EC-03: Access settings page without logged in session (redirects to admin login)
