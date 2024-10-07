PIN = "12345" # if this was an integer, then the entry variable would also have to be converted to an integer

print("WELCOME TO THE BANK OF SHAO")
entry = input("ENTER YOUR PIN:")

while entry != PIN: # while loops continuously run when the conditional is True unlike if statements, however, the way they work otherwise is the same (will run if conditional is True)
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ") # this line makes sure you can enter your pin again so it doesn't just print incorrect over and over again

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")