name = "Marcos"  #stores the value marcos as a string
age = 39  #store value the value of age as an integer
height = 5.2  #stores the value of height in feet as an a float
is_student = True  #stores bool value
print("----------------")
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
age = 39
name = input("What is your name? ")
print(f"Hi, {name}! you are approximately {age} years old")
number1 = input("enter the first number here. ")
number2 = input("enter the second number here. ")
number1 = float(number1)
number2 = float(number2)
result = number1 * number2
print(f"{number1} * {number2} = {result}")
print()
print("=========RECEIPT=========")
item = "How to score like Messi"
price = 20
quantity = 2
print("-----------------------")
total = price * quantity
print(f"Item:     {item}")
print(f"price:    ${price:.2f}")
print(f"Quantity:  {quantity}")
print("-------------------------")
print(f"total:     ${total:.2f}")
print("=========================")
print()
print("===PROFILE: MARCOS MSISKA===")
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
hobby = input("Enter your favorite hobby: ")
fun_fact = input("Enter one fun fact about yourself: ")
birth_year = input("Enter the year you were born:")
birth_year = int(birth_year) # convert from string to integer
from datetime import date
current_year = date.today().year # compute the age automatically using the current year.
age = current_year - birth_year
print("\n================================")
print("         USER PROFILE           ")
print("================================")
print(f"Name:       {name}")
print(f"Age:        {age} years old")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun Fact:   {fun_fact}")
print("================================")




