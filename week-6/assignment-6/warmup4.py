def is_valid_score(score):
    # Check if the score is an integer and between 0 and 100 inclusive
    if isinstance(score, int) and 0 <= score <= 100:
        return True
    return False


# Ask the user for input
user_input = input("Enter a score: ")

# Safely attempt to convert input to an integer
try:
    user_score = int(user_input)
except ValueError:
    user_score = None  # If user types letters/decimals, pass None so validation returns False

# Call the function inside an if statement
if is_valid_score(user_score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")