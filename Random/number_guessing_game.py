import random

print("I'm thinking of a number from 1 to 10.")

number = random.randint(1, 11) # 1-10

guess = float(input("Your guess: "))

if guess == number:
    print(f"You got it! My number was {number}!")
else:
    print(f"Sorry but I was thinking of {number}.")