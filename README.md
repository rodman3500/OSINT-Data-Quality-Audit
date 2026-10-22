# Collected OSINT Data Quality Audit

## Project Description
This Python program analyzes an existing employee directory CSV file to identify unavailable information and repeated email addresses. The program uses Python's built-in `csv` module and `collections.Counter` to process the data.

## Dataset
The original `employees.csv` contains 422 employee records with three columns: Name, Title, and Department. The original CSV file was not modified.

## How to Run
1. Open the project folder in Visual Studio Code.
2. Make sure `employees.csv` and `employee_csv_audit.py` are in the same folder.
3. Open the terminal in VS Code.
4. Run the following command:

`python3 employee_csv_audit.py`

No additional Python packages are required because the program uses only standard-library modules.

## Program Results

**Original employees.csv**

```text
COLLECTED OSINT DATA QUALITY AUDIT
Records processed: 422
Unavailable values:
  name: 0
  title: 2
  department: 5
  email: Not available (column missing)
Repeated available email values:
  Cannot analyze emails (Email column missing).
```

## Testing

### Test 1: Original Practice CSV
**Input:** `directory_practice.csv`

**Expected Results:**
- 6 records processed
- 0 unavailable names
- 2 unavailable titles
- 1 unavailable department
- 2 unavailable emails
- shared@example.invalid appears twice

**Actual Results:** All counts matched the expected results.

**Status:** PASS

### Test 2: Modified Practice CSV
**Input:** `directory_practice_modified.csv`

**Changes Made:**
- Changed Jordan's title to `nOt LiStEd`.
- Changed Morgan's email capitalization and added surrounding spaces.

**Expected Results:** The unavailable-value counts and repeated-email count should remain unchanged.

**Actual Results:** All counts remained unchanged, and the shared email address was still identified twice.

**Status:** PASS

### Test 3: Original Employee CSV
**Input:** `employees.csv`

**Expected Results:** The program should process the existing employee records, count unavailable information in the available columns, and identify any missing required columns.

**Actual Results:**
- 422 records processed
- 0 unavailable names
- 2 unavailable titles
- 5 unavailable departments
- Email column missing
- Repeated emails could not be analyzed

**Status:** PASS for available-field analysis; email analysis unavailable.

### Test 4: Unique Email Test
**Expected Results:** When all available email addresses are unique, the program should display a message indicating that no repeated emails were found.

**Actual Results:** pass.

**Status:** completed

## Interpretation
The results show that two employee records have unavailable titles and five have unavailable departments, meaning the dataset does not contain complete information for every employee. These missing values do not establish a security vulnerability, and the absence of an Email column prevents conclusions about repeated email addresses. Before drawing stronger conclusions, I would compare the affected records with the saved employee directory HTML to determine whether the information was missing from the original source or was not captured during collection.

## AI Assistance
I used the AI coding assistant in Visual Studio Code to help develop and understand portions of the Python program. I tested the code in VS Code and compared the results against the expected outputs provided in the assignment. 

## Files
- `employee_csv_audit.py` — Python program that analyzes CSV data.
- `employees.csv` — Original collected employee dataset.
- `directory_practice.csv` — Practice dataset provided for testing.
- `directory_practice_modified.csv` — Modified practice dataset used to test capitalization and whitespace handling.
- `.gitignore` — Excludes unnecessary Python environment files.
- `README.md` — Project documentation, results, and testing information.