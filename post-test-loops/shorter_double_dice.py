import random

while True:
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    sum = roll_1 + roll_2
    print("HERE COMES THE DICE!")
    print(f"Roll #1: {roll_1}")
    print(f"Roll #2: {roll_2}")
    print(f"The total is {sum}")

    if roll_1 == roll_2:
        break