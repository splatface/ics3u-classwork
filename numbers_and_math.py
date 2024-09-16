print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# calculates the number of boys: total students - # of girls
print("there are " + str(33 - 11) + " boys.")
print()
# calculates the percent of girls: # of girls/total students
print(f"That means {round(11 * 100/ 33, 2)} % are girls...")
# calculates the percent of boys: # of boys/total students
print(f"and {round((33 - 11) * 100/ 33, 2)} % are boys.")
print()
print("If we made groups of six...")
# calculates how many groups of six there would be: total students/6
print(f"There would be {33 // 6} groups of six.")
# calculates the remaining people that would not be in a group of 6: 33 mod 6
print(f"And then a smaller group of {33 % 6} people.")
# prints 30 "-"s
print("-" * 30)
print("If we had 17 apples and 3 people...")
# calculates the number of apples each person would get: total apples/total people
print(f"Each person would get {17 // 3} whole apples.")
# calculates the number of apples left over: 17 mod 3
print("There would be " + str(17 % 3) + " apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# calculates how much each person would pay: number of apples per person * $5
print(f"they would each pay ${2 * 5}.")
