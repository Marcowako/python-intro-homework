import csv
import os
from datetime import datetime

file_path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(file_path):
    print(f"Error: '{file_path}' does not exist.")
    exit()

expenses = []
with open(file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = float(row["amount"])
        expenses.append(row)

food_expenses = [item for item in expenses if item["category"] == "Food"]
total_food = sum(item["amount"] for item in food_expenses)
today_str = datetime.now().strftime("%B %d, %Y")

with open("food_report.txt", "w") as report:
    report.write(f"Food Expense Report — generated {today_str}\n")
    for item in food_expenses:
        report.write(f"{item['date']}: ${item['amount']:.2f}\n")
    report.write(f"Total: ${total_food:.2f}\n")