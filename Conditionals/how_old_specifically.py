age = int(input("What is your age?"))

if age < 0:
    print("??? Try again.")
elif age < 16:
    print("You can't drive.")

elif age <= 17 and age >= 16:
    print("You can drive but not vote.")

elif age <= 20 and age >= 18:
    print("You can vote but not rent a car.")

else:
    print("You can do pretty much anything.")
