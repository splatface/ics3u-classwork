import random

nums = []
times = 0

for i in range(10):
    nums.append(random.randint(1, 50))

print(nums)
wanted = int(input("Number: "))

for a in nums:
    if a == wanted:
        times += 1

print(f"{wanted} was found {times} times.")