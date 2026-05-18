# Page: My Coifeur — Salon Owner Web Management Portal
**URL:** `https://dev.mycoifeur.com.sa/en/salon/dashboard` (and sub-routes `/services`, `/offers`, `/orders`, `/calendar`)
**Type:** B2B Service Provider Control Center
**Priority:** P0 — Core supplier portal; allows salon owners and managers to control inventory (services, offers, packages), manage staff working hours, and fulfill customer bookings.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

The dedicated web application dashboard for authenticated Salon Owners. Provides comprehensive control over the salon's public profile, service catalog, active promotional offers, bundled packages, staff members, working calendar, financial commissions, and incoming customer appointments.

---

## UI Elements — Salon Portal Sidebar Navigation

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Dashboard Overview Link | `a[href="/en/salon/dashboard"]` | Anchor | Always | Key metrics & today's appointments |
| Manage Services Link | `a[href="/en/salon/services"]` | Anchor | Always | Create, edit, delete web services |
| Manage Offers Link | `a[href="/en/salon/offers"]` | Anchor | Always | Create promotional discounts |
| Manage Packages Link | `a[href="/en/salon/packages"]` | Anchor | Always | Bundled service packages |
| Appointment Calendar | `a[href="/en/salon/calendar"]` | Anchor | Always | Day, week, month schedule view |
| Incoming Orders Link | `a[href="/en/salon/orders"]` | Anchor | Always | Booking orders management |
| Staff / Stylists Link | `a[href="/en/salon/staff"]` | Anchor | Always | Employees & commission splits |
| Salon Profile & Settings| `a[href="/en/salon/profile"]` | Anchor | Always | Cover photo, working days, location |

---

## UI Elements — Service Management Modal (`/en/salon/services/create`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Create Service Button | `button[data-slot="create-service-trigger"]`| Button | Always | Opens service creation modal/form |
| Service Name (English) | `input[name="serviceNameEn"]` | Text Input | Yes | E.g. "Keratin Hair Treatment" |
| Service Name (Arabic) | `input[name="serviceNameAr"]` | Text Input | Yes | E.g. "علاج الكيراتين للشعر" |
| Category Dropdown | `select[name="categoryId"]` | Select | Yes | Hair, Nails, Spa, Facial |
| Service Description | `textarea[name="description"]` | Textarea | No | Details about the procedure |
| Price (SAR) Input | `input[name="price"]`, `type="number"` | Number Input| Yes | E.g. 350.00 |
| Duration (Minutes) Input| `input[name="duration"]`, `type="number"`| Number Input| Yes | E.g. 60, 90, 120 |
| Specialist Assignment Chips| `data-slot="stylist-assignment"`| Checkbox | Yes | Assign which staff perform this |
| Save Service Button | `button[type="submit"]`, `text="Save Service"`| Submit Button| Yes | Submits multipart form |

---

## UI Elements — Offer Management Modal (`/en/salon/offers/create`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Create Offer Button | `button[data-slot="create-offer-trigger"]` | Button | Always | Opens offer creation modal |
| Offer Title (EN & AR) | `input[name="offerNameEn"]` | Text Input | Yes | Promotional campaign title |
| Discount Percentage / SAR | `input[name="discountValue"]`, `type="number"`| Number | Yes | E.g. 25% or SAR 50 off |
| Valid Services Select | `select[name="applicableServices"]` | Multi-select| Yes | Services eligible for this offer |
| Start Date Picker | `input[name="startDate"]`, `type="date"` | Date Input | Yes | Campaign launch date |
| End Date Picker | `input[name="endDate"]`, `type="date"` | Date Input | Yes | Campaign expiration date |
| Save Offer Button | `button[type="submit"]` | Submit Button| Yes | Activates offer |

---

## UI Elements — Order Management & Status Workflow (`/en/salon/orders`)

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Order Status Tabs | `role="tablist"`, `data-slot="order-tabs"` | Tabs | Always | Pending, Confirmed, Completed, Cancelled |
| Order Row / Card | `div[data-order-id]` | Row Card | On Orders | Client name, date, time, total SAR |
| Accept / Confirm Order CTA| `button[data-slot="confirm-order"]` | Action Button| Pending | Transitions order to Confirmed state |
| Reject / Cancel Order CTA| `button[data-slot="cancel-order"]` | Action Button| Pending | Opens cancellation reason modal |
| Mark Completed CTA | `button[data-slot="complete-order"]`| Action Button| Confirmed | Customer arrived and service delivered |
| Client WhatsApp Quicklink| `a[href^="https://wa.me/"]` | Anchor | Confirmed | Instant messaging with booked client |

---

## User Flows

### Flow 1: Create New Web Salon Service
```
1. Authenticated Salon Owner navigates to https://dev.mycoifeur.com.sa/en/salon/services
2. Click "Add New Service" button → Service creation modal opens
3. Enter Service Name (EN): "Gold Facial Glow"
4. Enter Service Name (AR): "نضارة الوجه الذهبية"
5. Select Category: "Facial & Skin Care"
6. Enter Description: "Deep cleansing facial with 24k gold mask."
7. Enter Price: "250.00" and Duration: "60" minutes
8. Select Assigned Specialists: "Mona", "Layla"
9. Click "Save Service" submit button
10. API returns 201 Created; modal closes successfully
11. Success notification: "Service created successfully! It is now live on your catalog."
12. Verify new service row appears at the top of the services data table
```

### Flow 2: Edit & Soft-Delete Salon Service
```
1. Under Manage Services table, click the "Edit" icon next to "Gold Facial Glow"
2. Modal populates with existing service data
3. Update Price to "300.00" and click "Update Service"
4. Success toast appears; table reflects updated price
5. Click the "Trash/Delete" icon next to the service
6. Confirmation prompt: "Are you sure you want to delete this service?"
7. Click "Confirm Delete" → API soft-deletes service; row disappears from active tab
8. (Optional) Switch to "Archived Services" tab and click "Restore" icon
```

### Flow 3: Incoming Order Confirmation & Completion Flow
```
1. Salon Owner is on /en/salon/orders dashboard
2. Under "Pending Appointments" tab, verify incoming booking #MC-10101 for Client Fatima
3. Click "Confirm Booking" button (`data-slot="confirm-order"`)
4. Order transitions instantly to "Confirmed" status; automated SMS sent to client
5. On the day of appointment, after service delivery, click "Mark Completed" button
6. Commission split calculated automatically; financial ledger updates
```

### Flow 4: Managing Salon Working Calendar & Off-Days
```
1. Navigate to /en/salon/profile (Working Days tab)
2. Toggle "Friday" switch from Active to Inactive (Closed)
3. Set Saturday - Thursday working hours: "10:00 AM" to "10:00 PM"
4. Click "Save Working Calendar"
5. Verify on client discovery portal that Friday timeslots are completely blocked
```

---

## Validation Rules

| Field / Component | Rule | Error / Fallback State |
|---|---|---|
| Service Price | Must be positive number > 0 | Form validation blocks zero or negative |
| Service Duration | Must be in increments of 15 mins (15, 30, 45, 60...) | Dropdown or number step validation |
| Offer Dates | End Date must be strictly after Start Date | Date picker prevents logical conflicts |
| Order Action | Only Pending orders can be Confirmed or Rejected | Buttons disabled on finalized orders |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-SALON-01 | SQL Injection in Service Name: `Keratin' UNION SELECT--` | Payload sanitized and stored safely, no DB crash |
| EC-SALON-02 | XSS in Service Description: `<iframe src=javascript:alert(1)>`| Escaped/stripped by framework before rendering on public page |
| EC-SALON-03 | Deleting a service that has active upcoming bookings | API blocks deletion or flags warning: "Cannot delete service with active appointments. Please archive instead." |
| EC-SALON-04 | Attempting to update another salon's service (IDOR check) | Backend enforces authorization check; returns 403 Forbidden |
| EC-SALON-05 | Uploading an oversized cover photo (>10 MB) | Client-side and server validation returns 413 Payload Too Large / warning |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/web/salon/services` | Retrieves all services owned by authenticated salon |
| POST | `/api/v1/web/salon/services/create` | Creates new service with multipart form data |
| POST | `/api/v1/web/salon/services/{id}/edit`| Updates existing service properties |
| DELETE | `/api/v1/web/salon/services/{id}` | Soft-deletes service from active catalog |
| PATCH | `/api/v1/web/salon/orders/{id}/status`| Updates incoming customer appointment state |

### Example Payload: Create Service
```json
{
  "name": "Gold Facial Glow",
  "name_ar": "نضارة الوجه الذهبية",
  "description": "Deep cleansing facial with 24k gold mask.",
  "price": "250.00",
  "duration": "60",
  "category_id": 12
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid Salon Token | `Bearer <jwt_token>` | Salon Owner session |
| Valid Service Name| `Gold Facial Glow` | Standard test service |
| Valid Price SAR | `250.00` | Standard pricing |
| SQLi String | `' OR 1=1--` | Input sanitization test |
