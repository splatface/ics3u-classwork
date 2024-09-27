gender = str(input("What is your gender? (M/F)"))
first_name = str(input("What is your first name?"))
last_name = str(input("What is your last name?"))
age = int(input("What is your age?"))

if age >= 20 and gender == "F":
    married = str(input("Are you married? (Y/N)"))

    if married.lower() == "y" and gender == "F":
        print(f"Then I will call you Mrs. {last_name}")
    
    else:
        print(f"Then I will call you Ms. {last_name}")

elif age >= 20 and gender == "M":
    print(f"Then I will call you Mr. {last_name}.")

elif age < 20:
    print(f"Then I will call you {first_name} {last_name}.")