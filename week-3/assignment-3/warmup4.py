# Warmup 4: Sign and Parity

number = int(input("Enter a number: ")) # Get number input from  user

# Check the sign
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Block 1 : Sign check (if / elif / else
if number % 2 == 0:
    print(f"{number} is even.")
elif number % 2 !=0:
    print(f"{number}is odd.")
else:
    print("Invalid number.")
