print("Let's play TWO QUESTIONS! Think of soemthing and I'll try to guess it.")
location = str(input("Does it stay inside, outside, or both?"))
living = str(input("Is it living?"))

if location == "inside" and living == "yes":
    print("I think your object is a houseplant.")

if location == "inside" and living == "no":
    print("I think your object is a shower curtain.")

if location == "outside" and living == "yes":
    print("I think your object is a bison.")

if location == "outside" and living == "no":
    print("I think your object is a billboard.")

if location == "both" and living == "yes":
    print("I think your object is a dog.")

if location == "both" and living == "no":
    print("I think your object is a cell phone.")