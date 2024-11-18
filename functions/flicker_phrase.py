import random
import os
import time


def main():
    for i in range(100000):
        r = random.randrange(1, 6)

        if r == 1:
            first()
        
        elif r == 2:
            second()

        elif r == 3:
            third()
        
        elif r == 4:
            fourth()
        
        else:
            fifth()
        
        time.sleep(0.05)
        
        # Write five if statements here.
        # If r is 1, then call the function named 'first'.
        # If r is 2, then call the function named 'second', and so on.
        
        # Optional: after the if statements are over, add in a slight delay.
        
        os.system("cls")  # clear console

    print("I pledge allegiance to the flag.")


def first():
    print("I                               ")


def second():
    print("  pledge                        ")


def third():
    print("         allegiance             ")


def fourth():
    print("                    to the      ")


def fifth():
    print("                           flag.")


if __name__ == "__main__":
    main()