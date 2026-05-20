# Page: My Coifeur — Admin Categories (Categories Management CRUD)
**URL:** `https://dev.mycoifeur.com.sa/en/admin-login`
**Admin Panel URL:** `https://dev.mycoifeur.com.sa/en/admin/categories`
**Type:** E2E Admin Categories Flow
**Priority:** P0

---

## Page Purpose
Comprehensive E2E test for the Admin Categories module. Admins manage service categories with localization support (English + Arabic), toggle status, and organize parent-child hierarchies.

**API Endpoints:**
- `GET /api/v1/web/admin/categories` — list all categories
- `POST /api/v1/web/admin/categories` — create category
- `PUT /api/v1/web/admin/categories/{id}` — edit category
- `DELETE /api/v1/web/admin/categories/{id}` — delete category

---

## UI Elements

### Categories List Page
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Page Title | `h1:has-text("Categories")` | Heading | Yes | Title "Categories" |
| Search Input | `input[placeholder*="Search categories..."]` | Text Input | Yes | Filters list |
| Add Category Btn | `button:has-text("Add Category")` | Button | Yes | Open create category form |
| Categories Table | `table` | Table | Yes | Categories grid |
| Table Columns | `th` | Header | Yes | Columns: CATEGORY NAME (EN), CATEGORY NAME (AR), STATUS, PARENT, ACTIONS |
| Actions Menu | `button:has-text("...")` | Button | Yes | 3-dot actions dropdown |

### Actions Dropdown Menu
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Edit Category | `[role="menuitem"]:has-text("Edit Category")` | Menu Item | Yes | Opens edit modal |
| Delete Category | `[role="menuitem"]:has-text("Delete Category")` | Menu Item | Yes | Deletes category |

### Add / Edit Category Modal
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Category Name (English) * | `input[name="name_en"]` | Text Input | Yes | English localization name |
| Category Name (Arabic) * | `input[name="name_ar"]` | Text Input | Yes | Arabic localization name |
| Status * | `select[name="status"]` | Select | Yes | Dropdown: Show, Hide |
| Save Changes | `button:has-text("Save Changes")` | Button | Yes | Submit |
| Cancel | `button:has-text("Cancel")` | Button | Yes | Close |

---

## User Flows

### Flow 1: Verify Columns on Categories Table
1. Login as admin (amrmuhamed9@gmail.com / 123456)
2. Navigate to `/en/admin/categories`
3. Assert page title "Categories" is visible
4. Assert table columns exist: CATEGORY NAME (EN), CATEGORY NAME (AR), STATUS, PARENT, ACTIONS

### Flow 2: Create a New Service Category
1. Login as admin
2. Navigate to `/en/admin/categories`
3. Click "Add Category" button
4. Fill English name "Makeup", Arabic name "مكياج", and set status to "Show"
5. Click "Save Changes"
6. Assert success toast is shown and new category is in table

### Flow 3: Edit Category and Toggle Status
1. Login as admin
2. Navigate to `/en/admin/categories`
3. Click 3-dot Actions menu on a category row
4. Select "Edit Category"
5. Assert Edit modal appears
6. Change Arabic name or select status to "Hide"
7. Click "Save Changes"
8. Assert success toast and table updates

### Flow 4: Delete Service Category
1. Login as admin
2. Navigate to `/en/admin/categories`
3. Click Actions -> Delete Category on a row
4. Confirm delete action in dialog
5. Assert success toast is shown and category is removed from table

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Category Name (English) * | Required | "English name is required" |
| Category Name (Arabic) * | Required | "Arabic name is required" |
| Status * | Required | "Please select status" |

---

## Edge Cases
- EC-01: Create category with duplicate localized names (validation warning or handled)
- EC-02: Delete category that has active child services (should warn or restrict deletion)
- EC-03: Access without authentication (redirect to login)
