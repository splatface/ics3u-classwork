message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

vowels_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter == 'a' or letter == "A" or letter == "e" or letter == "E" or letter == "i" or letter == "I" or letter == "o" or letter == "O" or letter == "u" or letter == "U":
        vowels_count += 1

print(f"\nYour message contains {vowels_count} vowels.")

print(range(7)) # prints out "range(0, 7)"
print(list(range(7))) # prints out "[0, 1, 2, 3, 4, 5, 6]"
# if it was range(len("Hello")), it would be range(5) so 0, 1, 2, 3, 4
# "box" has length 3, the index pos of x is 2