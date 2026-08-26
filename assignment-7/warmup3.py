import os

# 1. Print current working directory
print(os.getcwd())

# 2. Check if ../data/expenses.csv exists
file_path = "../data/expenses.csv"
if os.path.exists(file_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

# 3. Use os.path.join() to build the path from its parts and print it
built_path = os.path.join("..", "data", "expenses.csv")
print(built_path)