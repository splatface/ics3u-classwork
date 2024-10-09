print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 21, 2): # n is like a counter variable. n is less-intuitive but is generally easy to understand and could stand for number
    # e.g. (0, 5, 1) = start at 0, end at 4 (5-1), increase by 1
    print(f"{n}. {message}")

# if range is called with one number, it starts at 0 and doesn't include the last number
# with two numbers, it includes the first but excludes the second, increasing by 1