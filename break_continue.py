##############
print("Program 1")

number = -1

while number < 10:
    number += 1

    if number == 7:
        continue
    print(number)

##############
print("\n\nProgram 2")

number = 4
sum = 0

while number < 20:
    number += 1

    if number % 3 == 0:
        continue
    
    sum += number

print(sum)

##############
print("\n\nProgram 3")

start = int(input("Starting Number: "))
end = int(input("Ending number: "))

number = start - 1
sum = 0

while number < end:
    number += 1
    sum += number

    if number == 13 or number == 31:
        break
    
print(sum)

##############
print("\n\nProgram 4")

while True:
    word = input("What is the word? ")

    if word.lower() == "stop":
        break

    print(f"Your word: {word}")

print("Goodbye!")