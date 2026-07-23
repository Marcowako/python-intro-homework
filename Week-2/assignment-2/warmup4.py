# Error message:
# TypeError: can only concatenate str (not "int") to str

# What caused it:
# I tried to concatenate a string with an integer without converting
# the integer to a string first.

# How I fixed it:
# I converted the integer to a string using str(), so both values
# were strings before concatenating them.
age = input("How old are you? ")
next_year = int(age) + 1
print(f"Next year you will be {next_year}.")
