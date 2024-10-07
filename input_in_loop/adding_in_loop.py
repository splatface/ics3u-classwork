print("I will add up the numbers you give me. I will stop when you enter 0.")

number = int(input("Number: "))
sum = 0

while number != 0:
    sum += number
    print(f"The total so far is {sum}.")
    number = int(input("Number: "))

if number == 0:
    print(f"The total is {sum}.")