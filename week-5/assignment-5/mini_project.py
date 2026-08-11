# Copy of the numbers list (from week-5/data/numbers.py)
numbers = [42, 17, 89, 3, 56, 94, 23, 71, 8, 65]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        # Find minimum without using min()
        if not numbers:
            print("The list is empty.")
        else:
            smallest = numbers[0]
            for num in numbers:
                if num < smallest:
                    smallest = num
            print(f"The minimum value is: {smallest}")

    elif choice == "2":
        # Find maximum without using max()
        if not numbers:
            print("The list is empty.")
        else:
            largest = numbers[0]
            for num in numbers:
                if num > largest:
                    largest = num
            print(f"The maximum value is: {largest}")

    elif choice == "3":
        # Linear search without using .index() or 'in'
        target_input = input("Enter a number to search for: ")

        try:
            target = int(target_input)
            found = False
            found_index = -1

            for i in range(len(numbers)):
                if numbers[i] == target:
                    found = True
                    found_index = i
                    break

            if found:
                print(f"Found {target} at index {found_index}.")
            else:
                print(f"{target} was not found in the list.")
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == "4":
        # Bubble sort algorithm without using .sort() or sorted()
        # Work on a copy of numbers if you don't want to modify the original permanently, 
        # or sort numbers in place:
        n = len(numbers)

        while True:
            swapped = False
            for i in range(n - 1):
                if numbers[i] > numbers[i + 1]:
                    # Swap adjacent elements
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

            # If no two elements were swapped in the inner loop, the list is sorted
            if not swapped:
                break

        print(f"Sorted list: {numbers}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")