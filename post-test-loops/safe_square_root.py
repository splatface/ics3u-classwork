import math

while True:
    number = int(input("Number: "))

    if number < 0:
        print("You can't square root a negative number!")
        continue

    print(math.sqrt(number))

