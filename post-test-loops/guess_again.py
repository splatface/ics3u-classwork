import random

print("I'm thinking of a number from 1 to 10. Try to guess it.")
number = random.randint(1,10)

tries = 0

while True:
    guess = int(input("Your guess: "))
    tries += 1

    if guess == number:
        break

    print(f"Sorry that's not the correct number. Try again.")

print(f"You got it! My number was {number}!")
print(f"It took you {tries} tries.")