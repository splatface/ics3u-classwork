import random

name = input("Name (first last): ")
file = input("Filename: ")
grades2 = ""

grades = []

print("Here are your randomly-selected grades:")

for i in range(5):
    grades.append(random.randint(1, 100))

for a in range(len(grades)):
    print(f"Grade {a+1}: {grades[a]}")

for b in grades:
    grades2 += str(b) + "  "

with open(file, "w") as f:
    f.write(name)
    f.write("\n")
    f.write(grades2)
    f.close()