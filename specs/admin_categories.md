# Page: My Coifeur — Admin Categories (Categories & Services)
**URL:** `https://dev.mycoifeur.com.sa/en/admin/login`
**Type:** E2E Admin Categories Flow
**Priority:** P0

---

## Page Purpose
End-to-End comprehensive test for the Admin Categories and Services module covering:
- Creating new categories (with English/Arabic names and sorting order)
- Editing, deleting, and restoring categories
- Viewing and toggling active status of services

---

## UI Elements
| Element | Identifier Hint | Type | Required | Notes |
|---|---|---|---|---|
| Admin Email | `input[name="email"]` | Email Input | Yes | Admin login email |
| Admin Password | `input[name="password"]` | Password | Yes | Admin login password |
| Login Button | `button[type="submit"]` | Submit Button| Yes | Submits admin login |
| Categories Link | `a[href*="/categories"]` | Anchor | Yes | Sidebar categories link |
| Add Category Btn | `button[data-action="add-category"], button:has-text("Add Category")` | Button | Yes | Opens Add Category form/modal |
| Category Name EN | `input[name="name"], input[name="name_en"]` | Text Input | Yes | Category Name in English |
| Category Name AR | `input[name="name_ar"]` | Text Input | Yes | Category Name in Arabic |
| Sort Order Input | `input[name="order"], input[type="number"]` | Number Input | Yes | Numeric sort order (e.g. 1, 2) |
| Save Category Btn | `button[data-action="save-category"], button:has-text("Save Category")` | Button | Yes | Submits category creation/edit |
| First Edit Category Btn | `(.edit-cat, button[data-action="edit"])[0]` | Button | Yes | Opens category edit modal |
| First Delete Category Btn | `(.delete-cat, button[data-action="delete"])[0]` | Button | Yes | Soft deletes selected category |
| First Restore Category Btn | `(.restore-cat, button[data-action="restore"])[0]` | Button | No | Restores soft deleted category |
| Export Categories Btn | `button[data-action="export"], button:has-text("Export")` | Button | No | Exports category lists to CSV/Excel |
| Services Tab | `[data-tab="services"], button:has-text("Services")` | Tab/Button | Yes | Navigates to Services sub-management |
| Toggle Service Status Btn | `(.toggle-service, button[data-action="toggle-status"])[0]` | Button | Yes | Toggles service status (active/inactive) |
| Success Toast | `.toast-success, .success-message, [role="alert"]` | Element | Yes | Confirms actions success |

---

## User Flows

### Flow 1: Create Category with English & Arabic Name
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Categories Link"
6. Click "Add Category Btn"
7. Enter Category Name EN: "Premium Hair Care"
8. Enter Category Name AR: "العناية الفائقة بالشعر"
9. Enter Sort Order Input: "1"
10. Click "Save Category Btn"
11. Assert "Success Toast" is visible

### Flow 2: Edit Category and Export
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Categories Link"
6. Click "First Edit Category Btn"
7. Enter Category Name EN: "Premium Hair Care Updated"
8. Click "Save Category Btn"
9. Assert "Success Toast" is visible
10. Click "Export Categories Btn" (if available) to test export downloads

### Flow 3: Delete & Restore Category
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Categories Link"
6. Click "First Delete Category Btn"
7. Assert "Success Toast" is visible
8. Click "First Restore Category Btn" (if available) to restore deletion
9. Assert "Success Toast" is visible

### Flow 4: Toggle Service Active Status
1. Navigate to `https://dev.mycoifeur.com.sa/en/admin/login`
2. Enter Admin Email: "amrmuhamed9@gmail.com"
3. Enter Admin Password: "123456"
4. Click "Login Button"
5. Click "Categories Link"
6. Click "Services Tab"
7. Click "Toggle Service Status Btn" on the first listed service
8. Assert "Success Toast" is visible (Status toggled successfully)

---

## Validation Rules
| Field | Rule | Error Message |
|---|---|---|
| Category Name EN | Required | "English name is required" |
| Sort Order Input | Must be positive | "Order must be greater than or equal to 0" |

---

## Edge Cases
| ID | Scenario | Expected |
|---|---|---|
| EC-01 | Create Category with duplicate EN name | Displays validation duplicate alert |
| EC-02 | Set negative number for sort order | Form validation blocks submittal |
