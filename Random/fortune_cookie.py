import random

number = random.randint(1,7) #1-6
fortune_num = [random.randint(1,55) for i in range(6)]

if number == 1:
    print("You will be happy today.")
elif number == 2:
    print("You will get a raise soon.")
elif number == 3:
    print("You will encounter your future pet in the next month.")
elif number == 4:
    print("You will encounter misfortune today; watch your back!")
elif number == 5:
    print("Do not go outside today!")
else:
    print("You will be very unhappy today.")

print(f"{fortune_num[0]} - {fortune_num[1]} - {fortune_num[2]} - {fortune_num[3]} - {fortune_num[4]} - {fortune_num[5]}")