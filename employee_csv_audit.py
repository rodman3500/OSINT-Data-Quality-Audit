import csv
from collections import Counter

# CSV file to analyze
filename = "employees.csv"

# Read employee records
with open(filename, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    employees = list(reader)
    columns = reader.fieldnames or []


# Check whether a value is unavailable
def is_unavailable(value):
    if value is None:
        return True

    value = value.strip()
    return value == "" or value.lower() == "not listed"


# Display total records
print("COLLECTED OSINT DATA QUALITY AUDIT")
print("Records processed:", len(employees))


# Count unavailable values
fields = ["Name", "Title", "Department", "Email"]

print("Unavailable values:")

for field in fields:
    # Find the matching CSV column, ignoring capitalization
    actual_column = next(
        (column for column in columns
         if column.strip().lower() == field.lower()),
        None
    )

    if actual_column is None:
        print(f"  {field.lower()}: Not available (column missing)")
        continue

    missing_count = 0

    for employee in employees:
        if is_unavailable(employee.get(actual_column)):
            missing_count += 1

    print(f"  {field.lower()}: {missing_count}")


# Find repeated available email addresses
print("Repeated available email values:")

email_column = next(
    (column for column in columns
     if column.strip().lower() == "email"),
    None
)

if email_column is None:
    print("  Cannot analyze emails (Email column missing).")

else:
    email_counts = Counter()

    for employee in employees:
        email = employee.get(email_column)

        if not is_unavailable(email):
            normalized_email = email.strip().lower()
            email_counts[normalized_email] += 1

    repeated_emails = {
        email: count
        for email, count in email_counts.items()
        if count > 1
    }

    if repeated_emails:
        for email, count in sorted(repeated_emails.items()):
            print(f"  {email}: {count}")
    else:
        print("  No repeated available emails found.")