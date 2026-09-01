# mini_project.py
import csv
import sys

file_path = "../data/messy_data.csv"

# 1. Use try/except FileNotFoundError to check if the file exists before opening
try:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = list(csv.DictReader(file))
except FileNotFoundError:
    print(f'Error: "{file_path}" was not found. Please check the file path and try again.')
    sys.exit(1)

valid_rows = []
skipped_rows = []
total_rows = len(reader)

# 2 & 3. Process each row using enumerate (1-indexed row count to account for header line offset)
for row_num, row in enumerate(reader, start=2):
    # Hint 2: Guard against extra columns stored under None key by csv.DictReader
    if None in row:
        skipped_rows.append(f"  Row {row_num}: extra column detected — skipped")
        continue

    try:
        # Check required keys (raises KeyError if missing)
        name = row["name"]
        category = row["category"]
        raw_amount = row["amount"]

        # Convert amount to float (raises ValueError if invalid)
        amount = float(raw_amount)

        valid_rows.append({
            "name": name,
            "category": category,
            "amount": amount
        })

    except KeyError as e:
        skipped_rows.append(f"  Row {row_num}: KeyError — missing column {e}")
    except ValueError as e:
        skipped_rows.append(f"  Row {row_num}: ValueError — {e}")

# 4 & 5. Output summary report
parsed_count = len(valid_rows)
skipped_count = len(skipped_rows)

print("=== CSV Report ===")
print(f"Rows attempted:  {total_rows}")
print(f"Rows parsed:     {parsed_count}")
print(f"Rows skipped:    {skipped_count}\n")

print("Skipped rows:")
for log in skipped_rows:
    print(log)

print("\nClean data:")
for item in valid_rows:
    print(f"  {item['name']} | {item['category']} | ${item['amount']:.2f}")