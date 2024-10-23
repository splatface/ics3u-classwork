import random

l = []

for i in range(10):
    l.append(random.randint(1, 100))

for i in range(len(l)):
    print(f"Slot {i} contains a {l[i]}")