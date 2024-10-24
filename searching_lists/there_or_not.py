import random

nums = []
found = False

for i in range(10):
    nums.append(random.randint(1, 50))

print(nums)

wanted = int(input("Number: "))

for a in nums:
    if a == wanted:
        found = True

if found == False:
    print(f"{wanted} is not in the list.")
else:
    print(f"{wanted} is in the list.")