# Page: My Coifeur — Salon Discovery, Services & Offers
**URL:** `https://dev.mycoifeur.com.sa/en/salons`
**Type:** Core Marketplace Discovery & Catalog
**Priority:** P0 — High user engagement; main discovery portal where clients search and filter salons, view services/offers, and initiate bookings.
**Platform:** My Coifeur — Premium Salon & Beauty Services Booking Marketplace
**Locale:** English (`/en`) | Arabic (`/ar`) — bilingual, RTL/LTR toggle

---

## Page Purpose

The central marketplace catalog allowing users (guests or authenticated clients) to discover premium beauty salons. Features advanced filtering (city, location radius, gender category, ratings, price range), real-time search, pagination, and detailed salon profile inspection (services, offers, packages, working hours, and reviews).

---

## UI Elements — Search & Filtering Toolbar

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Search Bar Input | `input[name="search"]`, `placeholder="Search salon, service..."` | Text Input | Always | Real-time debounced search |
| City / Location Selector | `data-slot="location-selector"`, `aria-label="Select City"` | Dropdown | Always | Riyadh, Jeddah, Dammam |
| Gender Category Filter | `data-slot="gender-filter"` | Toggle / Tabs | Always | All, Women's Salons, Men's Barbers |
| Service Category Chips | `data-slot="service-category-chips"` | Horiz. Scroll | Always | Hair Styling, Makeup, Nails, Spa, Massage |
| Rating Filter Dropdown | `select[name="rating"]` | Select | Always | 4.0+ Stars, 4.5+ Stars |
| Price Range Slider | `input[type="range"]`, `name="priceRange"` | Range Slider | Always | 0 SAR to 2000+ SAR |
| Sort By Dropdown | `select[name="sortBy"]` | Select | Always | Distance, Rating, Price: Low-High, Popularity |
| Reset Filters Button | `button[data-slot="reset-filters"]`, `text="Reset"` | Button | When filtered | Clears all applied filter states |

---

## UI Elements — Salon Grid & Catalog Listing

| Element | Identifier Hint | Type | Visible | Notes |
|---|---|---|---|---|
| Active Filter Badges | `data-slot="active-filters"` | Badge Chips | When filtered | Shows applied filters with 'X' to remove |
| Salon Card Container | `article[data-salon-id]`, `role="listitem"` | Card | Always | Grid item representing a salon |
| Salon Thumbnail Image | `img[data-slot="salon-image"]` | Image | Always | Premium cover photo / gallery preview |
| Favorite Bookmark Icon | `button[data-slot="favorite-toggle"]` | Icon Button | Always | Toggles saved salon status (auth required) |
| Salon Brand Title | `h3[data-slot="salon-name"]` | Heading H3 | Always | E.g. "Royal Elegance Salon" |
| Star Rating & Reviews | `data-slot="salon-rating"`, "4.8 (120 reviews)" | Badge/Text | Always | Aggregate customer rating |
| Salon Distance / Address| `data-slot="salon-distance"`, "2.5 km • Al-Olaya, Riyadh" | Text | Always | Distance calculated from user location |
| Services Snippet | "Hair Care • Nails • Bridal Makeup" | Text | Always | Top categories offered |
| View Salon Details CTA | `a[href^="/en/salon/"]`, `text="View Salon"` | Anchor | Always | Opens complete salon profile |
| Pagination Controls | `nav[aria-label="Pagination"]`, `data-slot="pagination"` | Nav Toolbar | Pagination | Page 1, 2, 3, Next, Previous |
| Empty State Container | `data-slot="empty-state"`, "No salons found" | Container | No results | Displays when filter yields 0 matches |

---

## UI Elements — Detailed Salon Profile View (`/en/salon/{id}`)

| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Salon Header Hero | `section[data-slot="salon-hero"]` | Hero Section | Always | Cover photo, title, verified badge |
| Navigation Tabs | `role="tablist"` | Tabs | Always | Services, Offers, Packages, Reviews, About |
| Services Tab Container | `div[id="tab-services"]` | Container | Tab Active | Categorized service list |
| Service Item Row | `div[data-service-id]` | Row Card | Always | Name, duration, price, "Book Now" CTA |
| Add Service to Cart CTA | `button[data-slot="add-service-cta"]` | Button | Always | "Add to Cart" or "Book Now" |
| Offers Tab Container | `div[id="tab-offers"]` | Container | Tab Active | Active promotional discounts |
| Offer Item Card | `div[data-offer-id]` | Card | Always | Original price vs discounted price |
| Packages Tab Container | `div[id="tab-packages"]` | Container | Tab Active | Multi-session / bundled services |
| Working Hours Modal / Info| `data-slot="working-hours"` | Accordion | Always | Saturday-Thursday: 10 AM - 10 PM |
| Location Map Preview | `iframe[data-slot="salon-map"]` | Map View | Always | Embedded Google Maps location |

---

## User Flows

### Flow 1: Search & Filter Salons by City & Category
```
1. Navigate to https://dev.mycoifeur.com.sa/en/salons
2. Verify default grid view loads initial salons list (200 OK)
3. Select City: "Riyadh" from the top location dropdown
4. Select Gender Filter: "Women's Salons"
5. Click Service Category Chip: "Hair Care"
6. Verify salon grid updates instantly (or via API) to display only matching salons
7. Ensure pagination controls reflect correct page count
8. Click "Reset" button → Verify all filters clear and default full catalog restores
```

### Flow 2: Explore Salon Profile & View Service Categories
```
1. In the salon grid, click on "Royal Elegance Salon" card
2. Browser navigates to /en/salon/101
3. Salon hero section loads with correct cover image and star rating
4. Under "Services" tab, click category filter "Nail Care"
5. Verify list displays Manicure and Pedicure services with prices (e.g., 150 SAR)
6. Click "Add to Cart" next to Royal Manicure
7. Cart floating drawer or badge updates to reflect 1 item added
```

### Flow 3: Toggle Favorite Salon Bookmark
```
1. User is authenticated on the salon discovery page
2. Click the heart icon on "Glamour Beauty Lounge" card
3. Heart icon fills red; success toast: "Salon added to your favorites!"
4. Navigate to user profile favorites tab (/en/profile/favorites)
5. Verify "Glamour Beauty Lounge" appears in saved list
```

### Flow 4: Pagination & Infinite Scroll Handling
```
1. User is on salon catalog page with >20 results
2. Scroll to bottom of page 1
3. Click "Next Page" or page number "2" in pagination bar
4. URL updates to ?page=2
5. Catalog renders next batch of 12 salon cards without full page reload
```

---

## Validation Rules

| Field / Component | Rule | Error / Fallback State |
|---|---|---|
| Search Bar | Minimum 2 characters to trigger query | Stays idle for single characters |
| Distance Calculation | Requires user location permission | Fallback to default city center coordinate |
| Price Filter | Max price must be >= Min price | Slider enforces boundary constraints |
| Pagination | Page number must be positive integer | Invalid page number defaults to page 1 |

---

## Edge Cases

| ID | Scenario | Expected Behavior |
|---|---|---|
| EC-DISC-01 | Search term matches zero salons | Display elegant empty state: "No salons match your search criteria" with reset CTA |
| EC-DISC-02 | SQL Injection in search input: `' UNION SELECT 1,2--` | Query sanitized, returns safe empty state or normal search, no 500 error |
| EC-DISC-03 | XSS payload in URL param: `?city=<script>alert(1)</script>`| Escaped/stripped by framework, does not execute script |
| EC-DISC-04 | Network disconnection during catalog filter | Display offline banner or graceful error message, no app freeze |
| EC-DISC-05 | Rapid clicking between service category tabs | Requests debounced/aborted cleanly, UI reflects latest selected tab |
| EC-DISC-06 | Unauthenticated user clicks "Favorite" bookmark | Opens Authentication/Login modal instantly |

---

## API Contract

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/guest/salons` | Fetches paginated salon catalog with query filters |
| GET | `/api/v1/guest/salon/{id}` | Fetches complete public profile of a single salon |
| GET | `/api/v1/guest/salon/{id}/services` | Fetches salon services grouped by category |
| GET | `/api/v1/guest/salon/{id}/offers` | Fetches active promotional offers for salon |
| POST | `/api/v1/user/favorite/{id}` | Toggles favorite status (requires Auth token) |

### Example Request Params: Filter Salons
```
GET /api/v1/guest/salons?city=Riyadh&gender=female&category=hair&page=1&limit=12
```

### Example Response: Salon Profile (200 OK)
```json
{
  "success": true,
  "data": {
    "id": 101,
    "nameEn": "Royal Elegance Salon",
    "nameAr": "صالون الأناقة الملكية",
    "rating": 4.85,
    "city": "Riyadh",
    "address": "Al-Olaya Street, Building 45",
    "workingHours": "10:00 - 22:00"
  }
}
```

---

## Test Data

| Category | Data Value | Notes |
|---|---|---|
| Valid City | `Riyadh` | Primary testing hub |
| Valid Search Query | `Royal` | Matches Royal Elegance Salon |
| Zero Result Search | `NonExistentSalonXYZ999` | Triggers empty state verification |
| Valid Salon ID | `101` | Staging salon profile ID |
| SQLi Query | `' OR 1=1--` | URL / Search payload |
