import random

nums = []
found = False

for i in range(10):
    nums.append(random.randint(1, 50))

print(nums)

wanted = int(input("Number: "))

for a in range(len(nums)):
    if nums[a] == wanted:
        print(f"{wanted} is at index {a}.")
        found = True

if found == False:
    print(f"{wanted} is not in the list.")

