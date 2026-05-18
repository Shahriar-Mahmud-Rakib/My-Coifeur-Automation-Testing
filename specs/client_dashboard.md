# Page: My Coifeur — Client Profile & Account Dashboard
**URL:** `https://dev.mycoifeur.com.sa/en/profile/settings` (and `/en/profile/bookings`, `/en/profile/favorites`, `/en/profile/addresses`)
**Type:** Client Identity & Account Management Hub
**Priority:** P0 — Core retention & account hub; enables registered clients to manage personal data, track upcoming and historical bookings, manage saved addresses, and change passwords.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

Dedicated personal control center for authenticated Clients. Allows updating personal identity details (First Name, Last Name, Avatar Photo), inspecting upcoming and past salon appointments, managing multiple delivery addresses (for home salon services), inspecting favorite saved salons, and performing account security updates (Password Change, Logout).

---

## UI Elements — Dashboard Sidebar Navigation

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Profile Settings Tab | `a[href="/en/profile/settings"]` | Tab Link | Always | Personal details & avatar photo |
| My Bookings Tab | `a[href="/en/profile/bookings"]` | Tab Link | Always | Upcoming, Completed, and Cancelled orders |
| Favorite Salons Tab | `a[href="/en/profile/favorites"]`| Tab Link | Always | Saved salon cards |
| Saved Addresses Tab | `a[href="/en/profile/addresses"]`| Tab Link | Always | Location coordinates & delivery pins |
| Security & Password Tab | `a[href="/en/profile/security"]` | Tab Link | Always | Update password form |
| Log Out Button | `button[data-slot="logout-trigger"]` | Button | Always | Clears session token and redirects to Home |

---

## UI Elements — Profile Settings Form (`/en/profile/settings`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| User Avatar Preview | `img[data-slot="user-avatar-image"]`| Image | Always | Displays current profile picture |
| Upload New Photo Trigger| `input[type="file"]`, `name="avatar"` | File Input | No | Accepts JPG, PNG up to 5MB |
| First Name Input | `input[name="firstName"]` | Text Input | Yes | Editable text |
| Last Name Input | `input[name="lastName"]` | Text Input | Yes | Editable text |
| Phone Number Display | `input[name="phone"]`, `disabled` | Input | Always | Verified phone number (readonly/disabled) |
| Email Input | `input[name="email"]` | Email Input| Yes | Verified email address |
| Save Changes Button | `button[type="submit"]`, `text="Save Profile"`| Submit Button| Yes | Submits profile update API |

---

## UI Elements — My Bookings Ledger (`/en/profile/bookings`)

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Booking Filter Chips | `data-slot="booking-filters"` | Radio Group | Always | Upcoming, Completed, Cancelled |
| Appointment Card | `div[data-booking-id]` | Card | Bookings | Salon name, date, time, total SAR, status |
| Status Badge | `span[data-slot="booking-status"]` | Badge | Always | Green (Confirmed), Grey (Completed), Red (Cancelled) |
| Reschedule Booking CTA | `button[data-slot="reschedule-btn"]` | Button | Upcoming | Opens timeslot calendar picker |
| Cancel Appointment CTA | `button[data-slot="cancel-booking"]` | Button | Upcoming | Opens cancellation confirmation dialog |
| Rebook / Book Again CTA | `a[href^="/en/salon/"]` | Anchor | Completed | Instantly navigates to salon profile |
| Rate & Review Service CTA| `button[data-slot="leave-review"]` | Button | Completed | Opens 5-star rating modal |

---

## UI Elements — Saved Addresses Management (`/en/profile/addresses`)

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Add New Address Button | `button[data-slot="add-address-trigger"]`| Button | Always | Opens address creation modal |
| Address Card Item | `div[data-address-id]` | Card | Addresses | Displays Label (Home/Work), Street, City |
| Google Maps Pin Widget | `div[id="google-map-container"]` | Map View | Modal | Interactive map to pin precise coordinates |
| Address Title / Label | `input[name="addressTitle"]` | Text Input | Modal | E.g. "My Home", "Office" |
| Street & Building Input| `input[name="street"]` | Text Input | Modal | E.g. "Al-Olaya Street, Bldg 12" |
| Save Address Button | `button[type="submit"]` | Submit Button| Modal | Saves location to client profile |
| Delete Address Icon | `button[data-slot="delete-address"]` | Icon Button | Addresses | Removes address from saved list |

---

## UI Elements — Security & Password Update (`/en/profile/security`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Current Password Input | `input[name="currentPassword"]`, `type="password"`| Password | Yes | Verifies current account access |
| New Password Input | `input[name="newPassword"]`, `type="password"`| Password | Yes | Minimum 8 characters |
| Confirm New Password | `input[name="confirmNewPassword"]`| Password | Yes | Must exactly match New Password |
| Update Password Button | `button[type="submit"]` | Submit Button| Yes | Submits password change request |

---

## User Flows

### Flow 1: Update Profile Details & Avatar Photo
```
1. Authenticated Client navigates to https://dev.mycoifeur.com.sa/en/profile/settings
2. Click "Upload New Photo" trigger → Select test image (e.g. avatar.png)
3. Update First Name to "Fatima Updated"
4. Click "Save Profile" submit button
5. Success toast appears: "Profile updated successfully!"
6. Header user avatar and displayed name transition instantly to reflect updated values
```

### Flow 2: Inspect Upcoming Bookings & Cancel Appointment
```
1. Click "My Bookings" tab (`a[href="/en/profile/bookings"]`)
2. Verify appointment card for "Royal Elegance Salon" is under "Upcoming" tab
3. Click "Cancel Appointment" button (`data-slot="cancel-booking"`)
4. Confirmation modal opens: "Are you sure you want to cancel this booking? Free cancellation is allowed up to 4 hours before service."
5. Select cancellation reason and click "Confirm Cancellation"
6. Status badge transitions to "Cancelled" (Red); appointment row moves to Cancelled tab
```

### Flow 3: Create New Saved Address via Map Pin
```
1. Click "Saved Addresses" tab (`a[href="/en/profile/addresses"]`)
2. Click "Add New Address" button → Modal opens
3. Enter Address Label: "Home Oasis"
4. Click and drag Google Maps pin to precise Riyadh coordinate (24.7136, 46.6753)
5. Enter Street: "King Fahd Road, Villa 88"
6. Click "Save Address" button
7. Success toast appears; new address card rendered in saved addresses grid
```

### Flow 4: Secure Password Update Journey
```
1. Click "Security" tab (`a[href="/en/profile/security"]`)
2. Enter Current Password: "Password123!"
3. Enter New Secure Password: "NewSecurePassword456!" and confirm it
4. Click "Update Password" button
5. Success notification: "Your password has been successfully updated. All other active sessions have been secured."
```

### Flow 5: Client Logout
```
1. In sidebar navigation, click "Log Out" button
2. Confirmation prompt or instant logout execution
3. Session tokens (Cookies/LocalStorage) successfully cleared
4. Application redirects smoothly to public homepage (/en)
```

---

## Validation Rules

| Field / Component | Rule | Error / Fallback State |
|---|---|---|
| Avatar Photo | Max size 5MB, format JPG/PNG | "File too large. Maximum size is 5MB." |
| First Name | Mandatory, letters and spaces only | "First name cannot be empty" |
| New Password | Must be different from Current Password | "New password cannot be identical to current password" |
| Address Coordinates | Must be within serviceable Saudi boundaries | "Location is outside our current service coverage" |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-PROF-01 | SQL Injection in Address Title: `' UNION SELECT 1,2--` | Sanitized safely, stored as plain string, no SQL execution |
| EC-PROF-02 | XSS payload in First Name: `<script>alert('xss')</script>`| Stripped/escaped by backend API before returning in JSON |
| EC-PROF-03 | Submitting password change with incorrect Current Password | Rejected with 401 Unauthorized: "Incorrect current password." |
| EC-PROF-04 | Deleting the last remaining saved address | Allowed; renders clean empty state: "No saved addresses yet." |
| EC-PROF-05 | Attempting to update profile while session token is expired | Redirected automatically to Authentication / Login modal |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/user/profile` | Fetches complete account profile data for logged-in user |
| PATCH | `/api/v1/user/profile` | Updates personal identity details (First/Last name, avatar) |
| GET | `/api/v1/user/orders` | Retrieves upcoming and historical booking ledger |
| GET | `/api/v1/user/addresses` | Retrieves saved delivery location coordinates |
| POST | `/api/v1/user/addresses` | Creates new saved address record |
| POST | `/api/v1/user/update-password` | Updates account authentication password |

### Example Payload: Update Profile
```json
{
  "firstName": "Fatima Updated",
  "lastName": "Al-Zahra",
  "email": "fatima.client@mycoifeur.com"
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid Client Token | `Bearer <jwt_token>` | Authenticated user session |
| Valid First Name | `Fatima Updated` | Standard test string |
| Current Password | `Password123!` | Test account password |
| New Password | `NewSecurePassword456!` | Secure replacement string |
| SQLi String | `' OR 1=1--` | Security probe payload |
