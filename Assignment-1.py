name = "Marcos"  #stores the value marcos as a string
age = 39  #store value the value of age as an integer
height = 5.2  #stores the value of height as an a float
is_student = True  #stores bool value
print("----------------")
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student,type(is_student))

name = input("What is your name? ")
print(f"Hi, Marcos! you are approximatly {age} years old")
number1 = input("enter the first number here. ")
number2 = input("enter the second number here. ")
number1 = float(number1)
number2 = float(number2)
result = number1 * number2
print(f"{number1} x {number2} = {result}")
print()
print("=========RECEIPT=========")
item = "How to score like Messie Book"
price = 20
Quantity = 2
print("-----------------------")
total = price * Quantity
print(f"Item:     {item}")
print(f"price:    ${price:.2f}")
print(f"Quantity:  {Quantity}")
print("-------------------------")
print(f"total:     ${total:.2f}")
print("=========================")
print("")
print("===PROFILE: MARCOS MSISKA===")
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
hobby = input("Enter your fevorite hobby: ")
fun_fact = input("Enter one fun fact about yourself: ")
birth_year = input("Enter the year you were born:")
birth_year = int(birth_year) # convert from string to integer
current_year = 2026 # compute the age automatically using the current year.
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




