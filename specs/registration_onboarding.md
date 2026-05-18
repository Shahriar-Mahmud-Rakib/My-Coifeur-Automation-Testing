# Page: My Coifeur — Registration & Account Onboarding
**URL:** `https://dev.mycoifeur.com.sa/en/register`
**Type:** User & Partner Acquisition Entry Point
**Priority:** P0 — Core growth funnel; allows new clients and salon partners to register and verify their accounts.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

Facilitates secure account creation for new Clients and prospective Salon Partners. Enforces phone number and email OTP verification, captures mandatory profile details (Name, Gender, City, Password), and guides users through initial onboarding.

---

## UI Elements — Registration Mode Selection

| Element | Identifier Hint | Type | Visible |
|---|---|---|---|
| Register as Client Tab | `data-slot="tab-client"`, `role="tab"` | Tab Button | Always | Default active tab |
| Register as Salon Partner Tab| `data-slot="tab-salon"`, `role="tab"` | Tab Button | Always | Switches to partner application form |
| Already have an account? | `href="/en/login"`, `text="Log In"` | Anchor | Always | Redirects to login modal/page |

---

## UI Elements — Client Registration Form

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| First Name Input | `input[name="firstName"]`, `maxlength="50"` | Text Input | Yes | Letters and spaces only |
| Last Name Input | `input[name="lastName"]`, `maxlength="50"` | Text Input | Yes | Letters and spaces only |
| Phone Country Code | `data-slot="country-code-select"` | Dropdown | Yes | Default: +966 (Saudi Arabia) |
| Phone Number Input | `input[name="phone"]`, `type="tel"` | Tel Input | Yes | 7-12 digits numeric |
| Email Address Input | `input[name="email"]`, `type="email"` | Email Input | Yes | Unique email address |
| Gender Dropdown | `select[name="gender"]` | Select | Yes | Options: Male, Female |
| Password Input | `input[name="password"]`, `type="password"`| Password | Yes | Minimum 8 chars |
| Confirm Password Input | `input[name="confirmPassword"]`, `type="password"` | Password | Yes | Must match Password precisely |
| Terms & Conditions Checkbox | `input[name="agreeTerms"]`, `type="checkbox"` | Checkbox | Yes | Must be checked to submit |
| Submit Registration Button| `button[type="submit"]`, `text="Create Account"` | Submit Button | Yes | Dispatches OTP verification |
| OTP Verification Modal | `role="dialog"`, `data-modal="verify-otp"` | Dialog | — | Opens automatically post-submit |
| 6-Digit OTP Code Input | `input[name="otp"]`, `maxlength="6"` | OTP Input | Yes | Verifies mobile/email |
| Complete Registration Button| `data-slot="complete-registration"` | Submit Button | Yes | Finalizes account activation |

---

## UI Elements — Salon Partner Application Form

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Salon Brand Name (English) | `input[name="salonNameEn"]` | Text Input | Yes | Legal/Brand name |
| Salon Brand Name (Arabic) | `input[name="salonNameAr"]` | Text Input | Yes | Arabic localized name |
| Commercial Registration (CR)| `input[name="crNumber"]`, `maxlength="10"` | Text Input | Yes | Saudi CR number (10 digits) |
| Owner Representative Name | `input[name="ownerName"]` | Text Input | Yes | Primary point of contact |
| Salon Business Email | `input[name="businessEmail"]` | Email Input| Yes | Official business communication |
| Salon Phone / Mobile | `input[name="businessPhone"]`, `type="tel"` | Tel Input | Yes | Mobile number for notifications |
| City Dropdown | `select[name="cityId"]` | Select | Yes | Riyadh, Jeddah, Dammam, etc. |
| Submit Application Button | `button[type="submit"]`, `text="Apply as Partner"`| Submit Button| Yes | Submits partner request to Admin |

---

## User Flows

### Flow 1: Complete E2E Client Registration & Verification
```
1. Navigate to https://dev.mycoifeur.com.sa/en/register
2. Ensure "Client" tab is selected
3. Enter First Name: "Fatima" and Last Name: "Al-Zahra"
4. Select +966 and enter Phone Number: "509876543"
5. Enter valid unique Email: "fatima.client@mycoifeur.com"
6. Select Gender: "Female"
7. Enter secure Password: "Password123!" and confirm it in Confirm Password
8. Check "I agree to the Terms & Conditions and Privacy Policy"
9. Click "Create Account" button
10. Registration form submits; OTP verification modal appears
11. "OTP code sent to +966 509876543" notice displayed
12. Enter 6-digit OTP code: "123456"
13. Click "Complete Account Activation" button
14. Modal successfully closes; redirection to client home dashboard (/en/dashboard)
```

### Flow 2: Salon Partner Application Submission
```
1. Navigate to /en/register
2. Click "Register as Salon Partner" tab (`data-slot="tab-salon"`)
3. Form updates to Partner Application fields
4. Enter Salon Name (EN): "Glamour Beauty Salon"
5. Enter Salon Name (AR): "صالون جلامور للتجميل"
6. Enter 10-digit Saudi CR Number: "1010123456"
7. Enter Owner Name: "Sara Al-Faisal" and Business Email: "sara@glamoursalon.sa"
8. Select City: "Riyadh"
9. Click "Apply as Partner" button
10. Success modal appears: "Your partnership application has been submitted successfully! Our onboarding team will review your CR and contact you within 24 hours."
```

### Flow 3: Handling Duplicate / Existing Accounts
```
1. Fill registration form with an existing phone: 501234567 or email: user@mycoifeur.com
2. Click "Create Account"
3. Instant validation error appears under the field: "This phone number / email is already registered. Please log in."
4. "Log In" CTA button highlights
```

---

## Validation Rules

| Field | Validation Rule | Failure Message |
|---|---|---|
| First & Last Name | 2-50 characters, letters only, no special symbols | "Please enter a valid name (letters only)" |
| Phone Number | Must match Saudi mobile pattern `^5[0-9]{8}$` when +966 | "Please enter a valid Saudi mobile number" |
| Email Address | Standard email validation, unique across database | "Email address already registered" |
| Password Matching | Confirm Password must exactly match Password | "Passwords do not match" |
| CR Number (Salon) | Exactly 10 numeric digits | "Commercial Registration number must be 10 digits" |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-REG-01 | Submit form without checking Terms box | Submission blocked, validation warning displayed |
| EC-REG-02 | Enter password < 8 characters | Instant field error: "Password must be at least 8 characters long" |
| EC-REG-03 | XSS payload in First Name: `<img src=x onerror=alert(1)>`| Input sanitized/encoded before submission, no script execution |
| EC-REG-04 | SQL Injection in CR Number: `1010101' OR 1=1--` | Rejected gracefully by backend validation, no DB crash |
| EC-REG-05 | Resend OTP clicked multiple times during verification | Rate-limited to 1 request per 60 seconds |
| EC-REG-06 | Closing OTP modal before verification | Account remains unverified (Inactive), login triggers verification prompt |
| EC-REG-07 | Registering with Arabic localized characters in First/Last name | Fully supported, stored as UTF-8 in database |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/auth/register` | Creates unverified user record and triggers OTP |
| POST | `/api/v1/auth/verify-code` | Activates user account upon successful OTP match |
| POST | `/api/v1/web/salon/apply` | Submits prospective salon application for review |

### Example Payload: Client Registration
```json
{
  "firstName": "Fatima",
  "lastName": "Al-Zahra",
  "phone": "+966509876543",
  "email": "fatima.client@mycoifeur.com",
  "gender": "female",
  "password": "Password123!",
  "agreeTerms": true
}
```

### Example Payload: Verification OTP
```json
{
  "phone": "+966509876543",
  "code": "123456"
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid New Phone | `+966509876543` | Dynamic test generator prefix |
| Valid New Email | `test.client.gen@mycoifeur.com` | Dynamic test email |
| Valid Saudi CR | `1010123456` | 10-digit commercial registration |
| Existing Phone | `+966501234567` | Expected to fail (duplicate) |
| Weak Password | `12345` | Expected to fail (minimum length) |
