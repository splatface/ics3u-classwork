print("Think of an object. \nI will ask you two questions and try to guess it correctly!")

answer_1 = str(input("Question 1) Is it an animal, vegetable, or mineral?\n"))
answer_2 = str(input("Is it bigger than a breadbox?\n"))

if answer_1.lower() == "animal":
    if answer_2.lower() == "no":
        print("I think you are thinking of a squirrel.")
    elif answer_2.lower() == "yes":
        print("I think you are thinking of a moose.")

elif answer_1.lower() == "vegetable":
    if answer_2.lower() == "no":
        print("I think you are thinking of a carrot.")
    elif answer_2.lower() == "yes":
        print("I think you are thinking of a watermelon.")

elif answer_1.lower() == "mineral":
    if answer_2.lower() == "no":
        print("I think you are thinking of a paper clip.")
    elif answer_2.lower() == "yes":
        print("I think you are thinking of a Camaro.")