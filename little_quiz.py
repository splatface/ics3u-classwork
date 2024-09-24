start = str(input("Enter Y to start:"))
score = 0
if start.upper() == "Y":
    # question 1
    print("What is the capital of Alaska? \n (1) Melbourne \n (2) Anchorage \n (3) Juneau")
    a_1 = int(input())

    if a_1 == 3:
        print("That's correct!")
        score += 1
    else:
        print("Whoops. It's actually Juneau. Good try.")

    # question 2
    print("In Python, the way you get keyboard input is the keyboard_input function. \n (1) true \n (2) false")
    a_2 = int(input())

    if a_2 == 2:
        print("That's correct.")
        score += 1
    else:
        print("Nope. Sorry, it's false.")

    # question 3
    print("What is the result of 9+6/3? (Input your answer)")
    a_3 = float(input())

    if a_3 == 11:
        print("Yep. That's correct.")
        score += 1
    else: 
        print("Not quite.")

    print(f"Your final score is {score} out of 3 correct at an accuracy of {round(score*100/3)}%. Hope it was fun!")

else:
    print("Too bad.")
    quit()