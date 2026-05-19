# Page: My Coifeur — Appointment Booking, Cart & Checkout Journey
**URL:** `https://dev.mycoifeur.com.sa/en/checkout` (and `/en/cart`)
**Type:** Core Transaction & Monetization Funnel
**Priority:** P0 — Critical business transaction funnel; handles cart aggregation, appointment scheduling, promo code redemption, and payment processing.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

Facilitates seamless booking and financial checkout for salon services and promotional offers. Supports both Guest Checkout (capturing phone/email on the fly) and Authenticated Client Checkout. Allows scheduling date and timeslot, employee/stylist selection, promo code validation, and multiple payment options (Apple Pay, Mada, Visa, Cash/Pay at Salon).

---

## UI Elements — Floating Cart Drawer / Page (`/en/cart`)

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Cart Drawer Container | `aside[data-slot="cart-drawer"]`, `role="dialog"` | Drawer | On trigger | Slides in from right |
| Cart Item Row | `div[data-cart-item-id]` | Row Card | Items in cart | Displays service name, salon, price |
| Quantity / Item Remove | `button[data-slot="remove-item"]` | Icon Button | Items in cart | Deletes item from cart |
| Cart Subtotal Display | `span[data-slot="cart-subtotal"]` | Text | Always | Sum of item prices (e.g., 350 SAR) |
| VAT Tax Breakdown | `span[data-slot="cart-tax"]` | Text | Always | 15% VAT calculation |
| Proceed to Checkout CTA | `a[href="/en/checkout"]`, `button[data-slot="checkout-btn"]`| CTA Button | Items in cart | Initiates checkout flow |
| Empty Cart State | `div[data-slot="empty-cart"]` | Container | Empty cart | "Your cart is empty" + explore CTA |

---

## UI Elements — Checkout & Scheduling Page (`/en/checkout`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Client Identity Banner | `div[data-slot="checkout-identity"]` | Banner | Always | Shows logged-in user or guest login prompt |
| Guest Phone Input | `input[name="guestPhone"]`, `type="tel"` | Tel Input | Guest | Required if checking out as guest |
| Salon Location Summary | `section[data-slot="checkout-salon"]` | Section | Always | Salon name and address |
| Date Picker Calendar | `div[data-slot="booking-date-picker"]` | Calendar | Yes | Select available appointment date |
| Timeslot Selector Chips | `button[data-slot="timeslot-chip"]` | Radio Group | Yes | E.g. 10:00 AM, 11:30 AM, 02:00 PM |
| Stylist / Specialist Select | `select[name="employeeId"]` | Select | No | "Any Specialist" default or specific staff |
| Home Service Toggle | `input[name="isHomeService"]`, `type="checkbox"`| Toggle | No | Toggles between Salon visit vs Home service |
| Client Address Selector | `data-slot="client-address-select"` | Dropdown | Home Service | Required if Home Service is toggled |
| Promo Code Input | `input[name="promoCode"]` | Text Input | No | Discount voucher entry |
| Apply Promo Code Button | `button[data-slot="apply-promo"]` | Button | If code | Validates and recalculates total |
| Applied Discount Badge | `data-slot="applied-discount"` | Badge | On discount | Shows discount SAR with 'X' to remove |
| Payment Method: Apple Pay| `input[id="pay-apple"]`, `type="radio"` | Radio | Yes | Apple Pay gateway |
| Payment Method: Credit/Mada| `input[id="pay-card"]`, `type="radio"`| Radio | Yes | Visa / Mastercard / Mada debit |
| Payment Method: Pay at Salon| `input[id="pay-cash"]`, `type="radio"` | Radio | Yes | Cash on service delivery |
| Final Total Display | `data-slot="checkout-total"`, "Total: SAR 402.50" | Heading H3 | Always | Grand total including VAT - discounts |
| Confirm & Pay Button | `button[data-slot="confirm-payment-btn"]` | Submit Button | Yes | Processes transaction / booking |
| Booking Confirmation Modal| `role="dialog"`, `data-slot="booking-success"`| Dialog | — | Appears upon successful order creation |

---

## User Flows

### Flow 1: E2E Authenticated Client Appointment Booking (Salon Visit)
```
1. Authenticated client adds "Royal Manicure" & "Hair Styling" to cart from Royal Elegance Salon
2. Open Cart drawer → Verify items and subtotal (e.g., 300 SAR + 45 SAR VAT = 345 SAR)
3. Click "Proceed to Checkout" button
4. Browser navigates to https://dev.mycoifeur.com.sa/en/checkout
5. Select appointment date: Tomorrow's date from calendar
6. Select timeslot chip: "04:00 PM"
7. Select Specialist: "Amira" (or leave default "Any Specialist")
8. Under Payment Method, select "Pay at Salon" (Cash/POS)
9. Click "Confirm Booking" button
10. Booking API completes successfully; order reference #MC-987654 generated
11. Confirmation screen appears: "Booking Confirmed! An SMS confirmation has been sent."
12. Buttons available: "Add to Google/Apple Calendar" and "View My Bookings"
```

### Flow 2: Guest Checkout & Promo Code Validation
```
1. Unauthenticated guest adds "Swedish Massage" to cart and clicks Checkout
2. Checkout identity section prompts for mobile number
3. Guest enters phone: +966 501234567 and receives OTP to verify identity on the fly
4. Enter Promo Code: "BEAUTY20" in the voucher input and click "Apply"
5. API validates code → Subtotal drops by 20% (e.g., -60 SAR discount applied)
6. Select date and timeslot: "07:30 PM"
7. Select Payment Method: "Credit / Debit Card" (Mada/Visa)
8. Click "Pay & Confirm" → Gateway iframe loads; complete payment simulation
9. Success redirection to /en/order-confirmation with invoice details
```

### Flow 3: Home Service Booking & Address Selection
```
1. On checkout page, toggle "Request Home Service (Mobile Salon)" switch
2. Address section expands; user clicks "Add New Address"
3. Enter street name, building number, and pin location on Google Maps widget
4. Service fee updates to include Home Delivery Surcharge (e.g., +50 SAR)
5. Select Date, Timeslot, and complete payment
```

### Flow 4: Cart Item Removal & Empty State Handling
```
1. In cart drawer with 1 item, click the trash icon next to the item
2. Item smoothly animates out; subtotal resets to SAR 0.00
3. Empty state UI renders: "Your cart is feeling light! Discover premium salons around you."
4. "Proceed to Checkout" CTA button becomes disabled
```

---

## Validation Rules

| Field / Component | Rule | Error / Fallback State |
|---|---|---|
| Appointment Date | Cannot be in the past, must be within salon working calendar | Past dates disabled in picker |
| Timeslot | Must be available (not fully booked) | Unavailable slots greyed out |
| Promo Code | Must be active, within expiry date, and meet min cart value | "Promo code expired or invalid" |
| Payment Selection | Exactly one payment option must be selected | "Please select a payment method" |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-BOOK-01 | Timeslot gets booked by another user right before clicking Confirm | API returns 409 Conflict: "Timeslot no longer available." Page refreshes timeslot chips. |
| EC-BOOK-02 | Enter SQLi in Promo input: `DISC' OR 1=1--` | Gracefully rejected by validation, no SQL execution |
| EC-BOOK-03 | Enter XSS in Address field: `<script>alert('hack')</script>`| Input sanitized and HTML escaped before saving |
| EC-BOOK-04 | User navigates away or closes tab during card payment processing | Webhook reconciles payment state in background; order marked pending/abandoned |
| EC-BOOK-05 | Adding items from two different salons to cart | Display alert: "Cart can only contain items from one salon. Replace existing cart?" |
| EC-BOOK-06 | Checkout total exceeds maximum transaction limit (e.g., >15,000 SAR) | Gateway check blocks transaction or requires partial deposit |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/user/cart` | Retrieves current session cart items and financial summary |
| POST | `/api/v1/user/cart/add` | Adds service, offer, or package to cart |
| POST | `/api/v1/user/checkout/promo` | Validates promotional discount voucher |
| POST | `/api/v1/user/orders/create` | Creates final booking order and initiates payment gateway |
| POST | `/api/v1/payments/webhook` | Asynchronous payment gateway status notification (Apple Pay/Mada) |

### Example Payload: Create Order / Booking
```json
{
  "salonId": 101,
  "cartItems": [
    { "serviceId": 501, "quantity": 1, "price": 150.00 }
  ],
  "bookingDate": "2026-06-01",
  "timeslot": "16:00",
  "employeeId": 12,
  "isHomeService": false,
  "promoCode": "BEAUTY20",
  "paymentMethod": "pay_at_salon",
  "totalAmount": 138.00
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid Salon ID | `101` | Royal Elegance Salon |
| Valid Service ID | `501` | Standard service ID |
| Valid Promo Code | `BEAUTY20` | Active 20% discount code |
| Expired Promo Code| `OLDCODE2024` | Triggers error validation |
| Valid Booking Date| `2026-06-01` | Future test date |
| Valid Timeslot | `16:00` | Standard afternoon slot |
