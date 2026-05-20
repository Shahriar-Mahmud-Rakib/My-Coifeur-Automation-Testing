import os
from pathlib import Path

specs_dir = Path("specs")

# Mapping of screenshot items to their corresponding spec files
admin_specs = [
    "admin_bookings.md",
    "admin_categories.md",
    "admin_contact_requests.md",
    "admin_finance.md",
    "admin_full_dashboard.md",
    "admin_management.md",
    "admin_promocode.md",
    "admin_providers.md",
    "admin_settings.md",
]

print("Starting spec renaming...")

for spec in admin_specs:
    src = specs_dir / f"_{spec}"
    dst = specs_dir / spec
    if src.exists():
        src.rename(dst)
        print(f"Renamed: {src.name} -> {dst.name}")
    elif dst.exists():
        print(f"Already renamed: {dst.name}")
    else:
        print(f"Not found: {src.name}")

print("Spec renaming complete!")
