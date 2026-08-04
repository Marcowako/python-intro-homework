# Create a hardcoded dictionary representing a student
student = {
    "name": "Alex",
    "grade": 11,
    "subjects": ["Math", "Science", "History"]
}

# 1. Print each key-value pair using .items() in a for loop
print("Student details:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n--- Updating Dictionary ---")

# 2. Add a new key "graduated" with the value False
student["graduated"] = False

# 3. Print the updated dictionary
print("Updated student dictionary:")
print(student)