import random

l = []
l2 = []

for i in range(10):
    l.append(random.randint(1, 100))

for a in range(len(l)):
    l2.append(l[a])

l[-1] = -7

print("List 1:", l) 
print("List 2:", l2)


# cannot copy lists like below bc it'll change the value for both lists
# l2 = l
# l2[0] = -100
# print(l2, l)