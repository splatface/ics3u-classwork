print("Enter three integers:")

num1 = int(input("Side 1: "))

while True:
    num2 = int(input("Side 2: "))

    if num2 < num1:
        print(f"{num2} is less than {num1}. Try again.")
        continue
    
    break

while True:
    num3 = int(input("Side 3: "))

    if num3 < num2:
        print(f"{num3} is less than {num2}. Try again.")
        continue
    
    break

if num1**2 + num2**2 == num3**2:
    print("Yes! It is a right triangle!")

else:
    print("No! It is not a right triangle!")
