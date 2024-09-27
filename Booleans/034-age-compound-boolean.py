age = int(input("How old are you?\n"))

if age < 16:
    print("You can't drive.")

if age <= 17 and age >= 16:
    print("You can drive but not vote.")

if age <= 24 and age >= 18:
    print("You can vote but not rent a car.")

if age >= 25:
    print("You can do pretty much anything.")