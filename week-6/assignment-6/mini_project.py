# Pull a copy of the numbers list from week-5/data/numbers.py
numbers = [64, 34, 25, 12, 22, 11, 90, 88, 45, 50]


def find_min(numbers):
    """Returns the minimum value in the list using a loop."""
    if not numbers:
        return None
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val


def find_max(numbers):
    """Returns the maximum value in the list using a loop."""
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val


def search(numbers, target):
    """Returns the index of target, or -1 if not found."""
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def bubble_sort(numbers):
    """Returns a new sorted list without modifying the original list."""
    arr = numbers.copy()  # Create a copy so original remains unchanged
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def show_menu():
    """Prints the menu options and returns the user's choice as a string."""
    print("\n--- Number Cruncher Menu ---")
    print("1. Find Minimum")
    print("2. Find Maximum")
    print("3. Search for a Number")
    print("4. Display Sorted List")
    print("5. Exit")
    return input("Enter your choice (1-5): ")


def main():
    """Main loop that calls show_menu() and dispatches to the right function."""
    while True:
        choice = show_menu()

        if choice == "1":
            minimum = find_min(numbers)
            print(f"Minimum value: {minimum}")

        elif choice == "2":
            maximum = find_max(numbers)
            print(f"Maximum value: {maximum}")

        elif choice == "3":
            try:
                target = int(input("Enter target number to search for: "))
                index = search(numbers, target)
                if index != -1:
                    print(f"Found at index {index}")
                else:
                    print("Not found")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        elif choice == "4":
            sorted_list = bubble_sort(numbers)
            print(f"Sorted list: {sorted_list}")
            print(f"Original list remains: {numbers}")

        elif choice == "5":
            print("Exiting Number Cruncher. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")


# Call main() at the bottom of the file
if __name__ == "__main__":
    main()