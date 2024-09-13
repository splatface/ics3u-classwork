# declare nums
num1 = 3
num2 = 4
num3 = 5

# sum/subtraction of nums:
sum = num1 + num2 + num3
subtraction = num1 - num2 - num3
print("sum: ", sum)
print("subtraction: ", subtraction)

# takes average of nums:
avg = sum/3
print("average: ", avg)

# percent of sum:
percent = avg/sum * 100
print("average is ", percent, f" % of sum")

# flooring/rounding:
floor = avg//sum * 100
round = round(percent, 2)
print("approximately: ", floor, f"% or: ", round, "%")

# leftover?
remainder = sum % avg
print("Remainder when flipped: ", remainder)

# random story time:

# determine number of birds
print(f"There are {20-10} birds flying in the sky.")

# determine loners
print(f"Of these birds, {20-10-4} are destined to be loners, flying high, yet flying alone.")

# today's date
print("As today is {}-{}-{}, wait no...".format(2100-76, 9, 13))

# random conclusion
print("New" + "Intel" + "Received" + "...") # no spaces intentional
print("No birds, sky clear.")