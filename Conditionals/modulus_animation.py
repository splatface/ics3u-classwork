import time
import os


for i in range(80):
    os.system("cls")

    if i % 10 == 0:
        print("o" + "-"*9)
    elif i % 10 == 1:
        print("-" + "o" + "-"*8)
    elif i % 10 == 2:
        print("-"*2 + "o" + "-"*7)
    elif i % 10 == 3:
        print("-"*3 + "o" + "-"*6)
    elif i % 10 == 4:
        print("-"*4 + "o" + "-"*5)
    elif i % 10 == 5:
        print("-"*5 + "o" + "-"*4)
    elif i % 10 == 6:
        print("-"*6 + "o"  + "-"*3)
    elif i % 10 == 7:
        print("-"*7 + "o" + "-"*2)
    elif i % 10 == 8:
        print("-"*8 + "o" + "-"*1)
    if i % 10 == 9:
        print("-"*9 + "o" + "-"*0)
    
    
    time.sleep(0.1)
