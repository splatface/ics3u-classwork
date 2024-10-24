import random

nums = []
max = 0

for i in range(10):
    nums.append(random.randint(1, 100))

print(nums)

for a in nums:
    if a > max:
        max = a

print(f"The largest value is {max}.")