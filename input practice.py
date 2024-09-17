# User Input:

print("Enter the following information about an item you wish to purchase..")
print()

name = input("The name of the item:")
# string input

# float input (number) - prices have decimals, with int instead of float, will cause an error
price = float(input("The price: $"))

# int input (number) - cannot have half of an item, so integer
quantity = int(input(("How many do you want?")))

subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")

# name = input()
# print("Enter the name of the item:")
# if coded like above, the user will become very confused 
# as the prompt will come after they have already typed 
# in the name of the item (plus they will not know TO 
# type in the name in the input)


print("""***************************
***************************
***************************
***************************
***************************
***************************""")


# The Forgetful Machine:
int(input("What's your favourite number?"))
str(input("What about word?"))
float(input("Value?"))

print("""***************************
***************************
***************************
***************************
***************************
***************************""")

# Name, Age, and Salary

name = str(input("Welcome, what's your name?"))
age = int(input(f"Nice name {name}. How old are you?"))
salary = float(input("Hmm. What do you make?"))
print(f"Wow {name}! That's a pretty good salary! {salary} huh")

print("""***************************
***************************
***************************
***************************
***************************
***************************""")

# More User Input of Data
first_name = str(input("First Name:"))
last_name = str(input("Last Name:"))
grade = int(input("Grade:"))
ID_num = int(input("Student ID Number:"))
login_name = str(input("Login Name:"))
average = float(input("Average:"))

print("Your information:")
print(f"""
      Login: {login_name}
      ID: {ID_num}
      Name: {last_name}, {first_name}
      Average: {average} %
      Grade: {grade}""")

print("""***************************
***************************
***************************
***************************
***************************
***************************""")

# Age in Five Years:

name = str(input("Hi. What's your name? "))
age = int(input(f"How old are you {name}? "))

print(f"""Wow! You'll be {age+5} in five years!
And five years ago, you were {age-5}!""")

print("""***************************
***************************
***************************
***************************
***************************
***************************""")

# A Silly Calculator:

num1 = float(input("What is your first number? "))
num2 = float(input("What is your second number? "))
num3 = float(input("What is your third number? "))

calculator = (num1 + num2 + num3)/2
print(f"... {calculator}")


print("""***************************
***************************
***************************
***************************
***************************
***************************""")


# BMI Calculator:
system = int(input("Type: 1 for imperial, 2 for metric measurements: "))

if system == 1:
    height = float(input("Height in inches: "))
    weight = float(input("Weight in pounds: "))
    bmi = (0.453592*weight) / ((0.0254*height)**2)
    print("Your BMI is: ", round(bmi,2))


if system == 2:
    height = float(input("Height in meters: "))
    weight = float(input("Weight in kg: "))
    bmi = weight/(height**2)
    print("Your BMI is: ", round(bmi,2))
