# --- Part 1: Demonstrating Local Scope and NameError ---
def create_secret():
    secret_message = "I love coding!"


create_secret()

# Trying to access secret_message outside the function causes a NameError:
# print(secret_message)
# NameError: name 'secret_message' is not defined


# --- Part 2: Solving Scope with return ---
def get_secret():
    secret_message = "I love coding!"
    return secret_message


# Call the function and assign the returned value to a variable in the outer scope
my_message = get_secret()

# Print to confirm it works
print(my_message)