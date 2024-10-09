end = int(input("Number: "))

sum = 0

for i in range(end+1):
    print(i, end=" ")
    sum += i

print("\nThe sum is", sum)