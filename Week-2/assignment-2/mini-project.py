#Ask the user for the temperature in Fahrenheit
temp_input = input("Enter a temperature in Fahrenheit: ")

# Convert the input string into a float so we can do math with it
fahrenheit = float(temp_input)

# Convert to Celsius using the required formula
celsius = (fahrenheit - 32) * 5 / 9

# Print the result using an f-string
# The :.1f formats the numbers to exactly one decimal place
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")