x = -10
y = 0
print("x \t y")
print("-"*15)

for i in range(41):
    print(x, "\t", end=" ")
    y = x**2
    x += 0.5
    print(y)