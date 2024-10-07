import random

print("I'm thinking of a number from 1 to 10.")

number = random.randint(1, 10)

guess = float(input("Your guess: "))

while guess != number:
    print(f"Sorry that's not the correct number. Try again.")
    guess = float(input("Your guess: "))

print(f"You got it! My number was {number}!")
    