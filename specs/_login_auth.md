# Page: My Coifeur — Authentication & Login Modal
**URL:** `https://dev.mycoifeur.com.sa`
**Type:** Authentication Entry Point & Identity Management
**Priority:** P0 — Critical path; authentication is required for client bookings, salon management, and administration.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

Primary entry point for authentication on My Coifeur. Connects Clients, Salon Owners, and Administrators to their respective dashboards. Supports Phone/OTP and Email/Password authentication modes, Role Selection, and Password Reset workflows.

---

## UI Elements — Header & Auth Navigation

| Element | Identifier Hint | Type | Visible |
|---|---|---|---|
| My Coifeur logo | `aria-label="My Coifeur homepage"`, `href="/en"` | Image link | Always |
| Explore Salons link | `href="/en/salons"` | Anchor | Desktop |
| Partner with Us link | `href="/en/partner"` | Anchor | Desktop |
| Language: AR button | `aria-label="العربية"`, `data-lang="ar"` | Toggle button | Always |
| Language: EN button | `aria-label="English"`, `data-lang="en"` | Toggle button | Always |
| Log In button | `data-slot="login-modal-trigger"`, `text="Log In"` | Button → opens modal | Unauthenticated |
| Register link | `href="/en/register"`, `text="Register"` | Button/Anchor | Unauthenticated |
| User profile dropdown | `data-slot="user-menu"`, avatar image | Menu button | Authenticated |

---

## UI Elements — Login Modal

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Modal Container | `role="dialog"`, `aria-modal="true"`, `data-modal="auth"` | Dialog | — | Centered modal on desktop, bottom sheet on mobile |
| Close button | `aria-label="Close modal"`, `data-slot="dialog-close"` | Button | — | Top-right corner |
| Modal Title | `text="Welcome to My Coifeur"` | Heading H2 | — | Static |
| Role Tab: Client | `data-role="client"`, `role="tab"` | Tab Button | Yes | Default active tab |
| Role Tab: Salon Owner | `data-role="salon"`, `role="tab"` | Tab Button | Yes | Switches to Salon login view |
| Role Tab: Admin | `data-role="admin"`, `role="tab"` | Tab Button | Yes | Switches to Admin portal login |
| Auth Mode: Phone / Email | `data-slot="auth-toggle"` | Toggle | No | Toggle between Phone/OTP and Email/Password |
| Country Code Selector | `aria-label="Country code"`, `data-slot="country-code"` | Dropdown | Yes | Default: 🇸🇦 +966 |
| Phone Number Input | `input[type="tel"]`, `name="phone"`, `maxlength="12"` | Tel Input | Required for Phone mode | Format: 50xxxxxxx |
| Email Input | `input[type="email"]`, `name="email"` | Email Input | Required for Email mode | Standard email format |
| Password Input | `input[type="password"]`, `name="password"` | Password Input | Required for Email mode | Password masking |
| Password Visibility Toggle| `aria-label="Toggle password visibility"` | Icon Button | No | Toggles password input type text/password |
| Forgot Password Link | `href="/en/forgot-password"`, `text="Forgot Password?"` | Anchor | No | Opens reset password modal |
| Log In Submit Button | `button[type="submit"]`, `text="Log In"` | Submit Button | Yes | Triggers authentication API |
| OTP Verification Input | `input[type="text"]`, `maxlength="6"`, `autocomplete="one-time-code"` | OTP Input | Required for OTP mode | Visible after OTP code dispatched |
| Resend OTP Timer | `data-slot="resend-timer"`, "Resend in 60s" | Text / Button | No | 60s countdown |

---

## User Flows

### Flow 1: Client Login via Phone & OTP
```
1. Navigate to https://dev.mycoifeur.com.sa/en
2. Click "Log In" button in header → Auth modal opens
3. Verify "Client" tab is active by default
4. Select Phone OTP mode (if not default)
5. Select +966 country code from dropdown
6. Enter phone number: 501234567
7. Click "Send OTP" button
8. Modal transitions to OTP entry screen; "Resend in 60s" timer begins
9. Enter 6-digit OTP: 123456
10. Click "Verify & Login" button
11. Success toast appears: "Welcome back to My Coifeur!"
12. Modal closes; header updates to display User Avatar and client navigation
```

### Flow 2: Salon Owner Login via Email & Password
```
1. Click "Log In" button in header → Auth modal opens
2. Click "Salon Owner" tab (`data-role="salon"`)
3. Form updates to require Email and Password
4. Enter salon email: aalih.aaa986@gmail.com
5. Enter password: 123456
6. Click "Log In" submit button
7. Success redirection to Salon Management portal (/en/salon/dashboard)
```

### Flow 3: Admin Login & Role Verification
```
1. Navigate to https://dev.mycoifeur.com.sa/en/admin-login
3. Enter admin email: amrmuhamed9@gmail.com and credentials
4. Click "Log In"
5. Success redirection to Super Admin control center (/en/admin/overview)
```

### Flow 4: Forgot Password Journey
```
1. In login modal (Email mode), click "Forgot Password?" link
2. Modal view updates to "Reset Password"
3. Enter registered email address
4. Click "Send Reset Link" or "Send OTP"
5. Receive password reset email/SMS with 6-digit verification code
6. Enter OTP and new secure password
7. Click "Confirm New Password" → Password successfully updated
```

### Flow 5: Bilingual Language Switch (EN ↔ AR)
```
1. Click "العربية" button in top navigation bar
2. Page and modal dynamically reload in Arabic layout (/ar)
3. HTML attributes update: lang="ar", dir="rtl"
4. All UI text transitions to Arabic localized strings
```

---

## Validation Rules

| Field | Validation Rule | Failure Message |
|---|---|---|
| Phone Number | Numeric digits only, length 7-12, pattern `^[0-9]{7,12}$` | "Please enter a valid phone number" |
| Email | RFC standard email format, must contain `@` and domain | "Please enter a valid email address" |
| Password | Minimum 8 characters | "Password must be at least 8 characters" |
| OTP Code | Exactly 6 numeric digits | "Invalid verification code" |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-AUTH-01 | Submit login with empty phone/email | Submit blocked, required field highlighted |
| EC-AUTH-02 | SQL Injection attempt in email: `' OR 1=1--` | Rejected gracefully, no 500 error, sanitization enforced |
| EC-AUTH-03 | XSS payload in password: `<script>alert(1)</script>` | Payload stripped/escaped, secure authentication rejection |
| EC-AUTH-04 | Entering invalid OTP 3 times consecutively | Account verification rate-limited / locked temporarily |
| EC-AUTH-05 | Resend OTP clicked before 60s timer expires | Button disabled, no multiple OTP dispatches |
| EC-AUTH-06 | Client token attempting to access Admin portal | Forbidden (403), redirected to client home |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/auth/login` | Authenticates User/Salon/Admin and returns JWT |
| POST | `/api/v1/auth/verify-code` | Verifies OTP code for phone login or password reset |
| POST | `/api/v1/auth/forgot-password` | Initiates password recovery process |
| POST | `/api/v1/auth/refresh-token` | Obtains fresh access token upon expiry |

### Example Payload: Login (Email)
```json
{
  "email": "user1@gmail.com",
  "password": "Password123!",
  "role": "client"
}
```

### Example Payload: Verify OTP
```json
{
  "phone": "+966501234567",
  "code": "123456"
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid Client Phone | `+966501234567` | Staging test client |
| Valid OTP Code | `from helpers.db_helper import get_otp` | MUST fetch real OTP via `get_otp(phone_number)` instead of using static 123456. |
| Valid Salon Email | `aalih.aaa986@gmail.com` | Staging salon owner account |
| Valid Admin Email | `amrmuhamed9@gmail.com` | Staging super admin account |
| Invalid Email | `invalid-email-string` | Triggers client-side validation |
| SQLi Payload | `' UNION SELECT 1,2,3--` | Security probe payload |
