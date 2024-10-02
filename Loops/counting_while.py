print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

times = int(input("How many times should it be outputted? "))

n = 1

while n <= times:
    print(f"{n*10}. {message}")
    n += 1 # a counter so that the message doesn't print infinitely

print()
print()
print()



# counting in intervals:

number = 491

while number <= 586:
    print(number)
    number += 5