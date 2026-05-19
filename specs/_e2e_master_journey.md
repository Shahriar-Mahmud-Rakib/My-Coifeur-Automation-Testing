# Page: My Coifeur — E2E Master Integration Journey
**URL:** `https://dev.mycoifeur.com.sa/en/register`
**Type:** E2E Integration Flow
**Priority:** P0
**Locale:** English (`/en`)

---

## Page Purpose
End-to-End integration test covering the entire business lifecycle. It spans client registration, salon registration, admin approval, salon service creation, client booking/checkout, and salon order confirmation.

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Register as Salon Partner Tab| `data-slot="tab-salon"` | Tab Button | Always | Switches to partner application form |
| Salon Brand Name (English) | `input[name="salonNameEn"]` | Text Input | Yes | Legal/Brand name |
| Salon Brand Name (Arabic) | `input[name="salonNameAr"]` | Text Input | Yes | Arabic localized name |
| Commercial Registration (CR)| `input[name="crNumber"]` | Text Input | Yes | Saudi CR number (10 digits) |
| Owner Representative Name | `input[name="ownerName"]` | Text Input | Yes | Primary point of contact |
| Salon Business Email | `input[name="businessEmail"]` | Email Input| Yes | Official business communication |
| Salon Phone / Mobile | `input[name="businessPhone"]`| Tel Input | Yes | Mobile number for notifications |
| City Dropdown | `select[name="cityId"]` | Select | Yes | Riyadh, Jeddah, Dammam, etc. |
| Submit Application Button | `button[type="submit"]` | Submit Button| Yes | Submits partner request to Admin |
| Register as Client Tab | `data-slot="tab-client"` | Tab Button | Always | Default active tab |
| First Name Input | `input[name="firstName"]` | Text Input | Yes | Letters and spaces only |
| Last Name Input | `input[name="lastName"]` | Text Input | Yes | Letters and spaces only |
| Phone Number Input | `input[name="phone"]` | Tel Input | Yes | 7-12 digits numeric |
| Email Address Input | `input[name="email"]` | Email Input | Yes | Unique email address |
| Gender Dropdown | `select[name="gender"]` | Select | Yes | Options: Male, Female |
| Password Input | `input[name="password"]` | Password | Yes | Minimum 8 chars |
| Confirm Password Input | `input[name="confirmPassword"]` | Password | Yes | Must match Password precisely |
| Terms & Conditions Checkbox | `input[name="agreeTerms"]` | Checkbox | Yes | Must be checked to submit |
| Client Create Account Btn | `button[type="submit"]` | Submit Button| Yes | Dispatches OTP verification |
| 6-Digit OTP Code Input | `input[name="otp"]` | OTP Input | Yes | Verifies mobile/email |
| Complete Registration Btn | `data-slot="complete-registration"`| Submit Button| Yes | Finalizes account activation |
| Login Email | `input[name="email"]` | Email Input | Yes | General login |
| Login Password | `input[name="password"]` | Password | Yes | General login |
| Login Button | `button[type="submit"]` | Button | Yes | General login |
| Salon Management Link | `a[href="/en/admin/salons"]` | Anchor | Yes | Admin portal |
| Inspect Salon Profile CTA| `button[data-slot="inspect-salon"]`| Action Button| Yes | Inspects pending salon |
| Approve Partner CTA | `button[data-slot="approve-salon"]`| Action Button| Yes | Approves salon |
| Confirm Activation Btn | `button[text="Confirm Activation"]`| Action Button| Yes | Confirms modal |
| Service Create Btn | `button[data-slot="create-service-trigger"]`| Button| Yes | Opens modal |
| Service Name (English) | `input[name="serviceNameEn"]` | Text Input| Yes | E.g. Haircut |
| Service Name (Arabic) | `input[name="serviceNameAr"]` | Text Input| Yes | E.g. قصة شعر |
| Service Category | `select[name="categoryId"]` | Select | Yes | Hair |
| Price (SAR) Input | `input[name="price"]` | Number | Yes | 150 |
| Duration Input | `input[name="duration"]` | Number | Yes | 30 |
| Save Service Button | `button[type="submit"]` | Submit | Yes | Save |
| Add to Cart Btn | `button[data-slot="add-to-cart"]`| Button | Yes | Add service to cart |
| Cart Proceed Checkout | `button[data-slot="checkout-btn"]`| Button | Yes | Checkout |
| Booking Date | `div[data-slot="booking-date-picker"]`| Calendar | Yes | Select date |
| Timeslot Chip | `button[data-slot="timeslot-chip"]`| Radio | Yes | E.g. 04:00 PM |
| Pay at Salon Method | `input[id="pay-cash"]` | Radio | Yes | Cash on service delivery |
| Confirm Booking Btn | `button[data-slot="confirm-payment-btn"]`| Button | Yes | Processes transaction |
| Salon Order Tab | `a[href="/en/salon/orders"]` | Anchor | Yes | Orders page |
| Confirm Order CTA | `button[data-slot="confirm-order"]`| Button | Yes | Accept order |
| Logout Button | `button[data-slot="logout-btn"]` | Button | Yes | Log out |

---

## User Flows

### Flow 1: Complete Cross-Role Journey
1. Navigate to /en/register
2. Click "Register as Salon Partner Tab"
3. Enter Salon Brand Name (English): "Test E2E Salon"
4. Enter Salon Brand Name (Arabic): "صالون"
5. Enter Commercial Registration (CR): "1010123456"
6. Enter Owner Representative Name: "E2E Owner"
7. Enter Salon Business Email: "salon.e2e@mycoifeur.com"
8. Enter Salon Phone / Mobile: "501112222"
9. Select City Dropdown: "Riyadh"
10. Click "Submit Application Button"
11. Navigate to /en/admin/login
12. Enter Login Email: "admin@mycoifeur.com" and Login Password: "AdminPassword123!"
13. Click "Login Button"
14. Click "Salon Management Link"
15. Click "Inspect Salon Profile CTA"
16. Click "Approve Partner CTA"
17. Click "Confirm Activation Btn"
18. Click "Logout Button"
19. Navigate to /en/salon/login
20. Enter Login Email: "salon.e2e@mycoifeur.com" and Login Password: "Password123!"
21. Click "Login Button"
22. Navigate to /en/salon/services
23. Click "Service Create Btn"
24. Enter Service Name (English): "E2E Haircut"
25. Enter Service Name (Arabic): "E2E Haircut AR"
26. Select Service Category: "Hair"
27. Enter Price (SAR) Input: "150"
28. Enter Duration Input: "30"
29. Click "Save Service Button"
30. Click "Logout Button"
31. Navigate to /en/register
32. Click "Register as Client Tab"
33. Enter First Name Input: "Client"
34. Enter Last Name Input: "Test"
35. Enter Phone Number Input: "509998888"
36. Enter Email Address Input: "client.e2e@mycoifeur.com"
37. Select Gender Dropdown: "Male"
38. Enter Password Input: "Password123!"
39. Enter Confirm Password Input: "Password123!"
40. Check "Terms & Conditions Checkbox"
41. Click "Client Create Account Btn"
42. Enter 6-Digit OTP Code Input: "123456"
43. Click "Complete Registration Btn"
44. Navigate to /en/salon/1010123456
45. Click "Add to Cart Btn"
46. Click "Cart Proceed Checkout"
47. Select "Booking Date" and "Timeslot Chip"
48. Select "Pay at Salon Method"
49. Click "Confirm Booking Btn"
50. Click "Logout Button"
51. Navigate to /en/salon/login
52. Enter Login Email: "salon.e2e@mycoifeur.com" and Login Password: "Password123!"
53. Click "Login Button"
54. Click "Salon Order Tab"
55. Click "Confirm Order CTA"
56. Expect redirect to success or success visible

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Admin Email | Must be admin | Invalid |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| E2E-01 | E2E successful journey | No errors |

---

## API Contract
| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/user/checkout/promo` | Validates promo |

---

## Test Data
| Category | Value |
|---|---|
| valid email | test@test.com |
