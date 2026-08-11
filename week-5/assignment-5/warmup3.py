# Hardcoded list of names
names = ["Alice", "Bob", "Charlie", "Marcus", "David", "Emma"]

# Prompt the user for a name
search_name = input("Enter a name to search for: ")

# Tracking variables
found = False
found_index = -1

# Loop through the list using index positions
for i in range(len(names)):
    if names[i] == search_name:
        found = True
        found_index = i
        break  # Exit the loop as soon as the name is found

# Print the result based on whether the name was found
if found:
    print(f'Found "{search_name}" at index {found_index}.')
else:
    print(f'"{search_name}" was not found in the list.')