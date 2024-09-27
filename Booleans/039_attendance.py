# all of the last names
boss = "boss"
carson = "carson"
gum = "gum"
lackey = "lackey"
melo = "melo"

# user last name
user_name = str(input("What is your last name? "))


# start comparing them for alphabetical order, <= as a few letters doesn't matter too much:

if user_name < boss:
    print("You're first! Why are you even here?")

elif boss <= user_name and carson > user_name:
    print("You barely have to wait.")

elif carson <= user_name and gum > user_name:
    print("You have to wait a little while.")

elif gum <= user_name and lackey > user_name:
    print("You have to wait a long time.")

elif lackey <= user_name and melo > user_name:
    print("You might as well be last.")

elif melo <= user_name:
    print("You might be dead by the time your name is called.")