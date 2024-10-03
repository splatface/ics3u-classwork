# 1- 10
print("1 - 10")
count = 1
total = 0

while count <= 10:
    total += count
    count +=1

print("total", total)


# 100 - 200
print()
print("100 - 200")

count = 100
total = 0

while count <= 200:
    total += count
    count += 1

print("total", total)


# (sum 100 - 200) - (sum 200 - 300)
print()
print("difference between sum from 100 to 200 and 200 to 300")
count2 = 200
total2 = 0

while count2 <= 300:
    total2 += count2
    count2 += 1

difference = total - total2
print("difference", difference)

# sum of multiples of 5 from 1000 to 10000
print()
print("sum of multiples of 5 from 1000 to 10000")

count = 1000
total = 0

while count <= 10000:
    total += count
    count += 5

print("total", total)

# sum of multiples of 5 from 1 to 100 without multiples of 3
print()
print("sum of multiples of 5 from 1 to 100 but not multiples of 3")

count = 1
total = 0

while count <= 100 and count % 3 != 0:
    total += count
    count += 5

print("total", total)