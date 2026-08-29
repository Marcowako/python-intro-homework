numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    result = numerator / denominator
    print(f"{numerator} ÷ {denominator} = {result}")
except ZeroDivisionError:
    print("Can't divide by zero — please try a non-zero denominator.")