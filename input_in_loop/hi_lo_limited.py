import random

number = random.randint(1,10)
number = 10

tries = 1

guess = int(input("Guess: "))

while guess != number and tries < 7:
    if guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
    guess = int(input("Guess: "))
    tries += 1

if guess == number:
    print(f"You got it, and in {tries} tries.")

if tries == 7:
    print("You are out of guesses. Try again next time.")