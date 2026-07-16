# 1. What the error message said:
# Traceback (most recent call last):
# 23  File "warmup4.py", line 12, in <module>
#     next_year = age + 1
# TypeError: can only concatenate str (not "int") to str

# 2. What caused it:
# The input() function saves the user's answer as a string (text). 
# I tried to add the number 1 to a string, which Python doesn't allow.

# 3. How I fixed it:
# I used the int() function to convert the 'age' string into an integer 
# before doing the math.

# The fixed code:
age = input("How old are you? ")
next_year = int(age) + 1
print(f"Next year you will be {next_year}.")