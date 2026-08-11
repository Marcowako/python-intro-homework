# Loop through numbers from 1 to 30
for num in range(1, 31):
    # Check the combined case first (divisible by both 3 and 5)
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)