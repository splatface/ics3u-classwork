import random

l = []

for i in range(1000):
    l.append(random.randint(10, 99))

for i in l:
    print(i, end="  ")