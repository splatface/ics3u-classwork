import random

number = random.randint(1, 101)

guess = float(input("I'm thinking of a number between 1-100. Try to guess it.\n"))

if number > guess:
    print("Too low.")
elif number < guess:
    print("Too high.")
else:
    print("You got it!")