import random

print("I'm thinking of a number from 1 to 10.")

number = random.randint(1, 10)

guess = float(input("Your guess: "))
tries = 0

while guess != number:
    print(f"Sorry that's not the correct number. Try again.")
    guess = float(input("Your guess: "))
    tries += 1

print(f"You got it! My number was {number}!")
print(f"It took you {tries} tries.")