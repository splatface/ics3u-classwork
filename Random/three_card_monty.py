import random

print("You slide up to Fast Eddie's card table and plop down your cash.")
print("He glances at you out of the corner of his eye and starts shuffling.")
print("He lays down three cards.")

ace = random.randint(1,4)

print("## ## ##")
print("## ## ##")
print("1  2  3")

guess = int(input("Which one is the ace?"))

if ace == guess:
    print("You nailed it! Fast Eddie reluctantly hands over your winnings, scowling.")
else:
    print(f"Fast Eddie wins again! The ace was number {ace}.")

if ace == 1:
    print("AA ## ##")
    print("AA ## ##")
    print("1  2  3")

elif ace == 2:
    print("## AA ##")
    print("## AA ##")
    print("1  2  3")

else:
    print("## ## AA")
    print("## ## AA")
    print("1  2  3")