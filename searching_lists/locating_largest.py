import random

nums = []
max = 0
max_pos = 0

for i in range(10):
    nums.append(random.randint(1, 100))

print(nums)

for index, number in enumerate(nums):
    if number > max:
        max = number
        max_pos = index

print(f"The largest value is {max} at index {max_pos}.")