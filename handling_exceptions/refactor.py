print("1 - Option One")
print("2 - Option Two")
print("3 - Option Three")
print()
while True:
    try:
        choice = int(input("> "))
        break
    except ValueError:
        print("Invalid option.")

if choice == 1:
    print("You chose OPTION ONE.")
elif choice == 2:
    print("You chose OPTION TWO.")
elif choice == 3:
    print("You chose OPTION THREE.")
else:
    print("Invalid option.")