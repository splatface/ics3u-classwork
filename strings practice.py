#Variables and Names:

# names the team name
team = "Toronto Blue Jays"

# names the date
current_date = "July 18, 2021"

# names the player
player = "Vladimir Guerrero Jr."

# stores # of home runs, games played, all season games, and record respectively
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73

# separate the variable assignments from variable calculation assignments

# calculates the amount of games not played yet; 74; for Q4, it logically makes sense (total - played = not played)
games_remaining = total_season_games - games_played

# calculates the average number of home runs per game; 0.35227272727... (repeating)
home_runs_per_game = home_runs_to_date / games_played

# predicts the future home runs; 57.0681818181... (repeating)
projected_home_runs = home_runs_per_game * total_season_games

# sees if future home runs are greater than current; no - approx: 57 < 73
can_break_record = projected_home_runs > home_run_record

# separate the print functions from the variable calculation assignments

print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game,2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")


print("""***************************
***************************
***************************
***************************
***************************
***************************""")


# More Variables and Printing:

store = "No Frills"
item = "Apples"
price = 0.5
quantity = 7
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

# f string
print(f"At {store} I bought some {item}.")
# concatenation
print("They sold for $" + str(price) + " each.")
# dot format
print("I wanted to purchase {} of them.".format(quantity))
print(f"The subtotal was {subtotal}, and the tax was {tax}.")
# f string
print(f"The total price, with tax included, was ${total}.")


print("""***************************
***************************
***************************
***************************
***************************
***************************""")



# Using Variables:
room_number = 113
e_math = 2.71828
subject = "Computer Science"

print(f"""This is room {room_number}.
e is close to {e_math}.
I am learning a bit about {subject}.""")



print("""***************************
***************************
***************************
***************************
***************************
***************************""")


# Still Using Variables:
name = "Tiffany Shao"
grad_year = 2026

print(f"My name is {name}, and I will graduate in {grad_year}.")

print("""***************************
***************************
***************************
***************************
***************************
***************************""")

# Your Schedule:

# all courses and teachers for them
course1 = "Adv Func"
teacher1 = "Ms. Wood"

course2 = "Comp Sci"
teacher2 = "Mr. Gallo"

course3 = "Christ and Culture"
teacher3 = "Ms. Nagy-Bakos"

course4 = "English NBE"
teacher4 = "Ms. Sgouros-Kalantzis"

# first row
print("+--------------------------------------------------+")

# courses
print(f"| 1 | {course1:>20} | {teacher1}")
print(f"| 2 | {course2:>20} | {teacher2}")
print(f"| 3 | {course3:>20} | {teacher3}")
print(f"| 4 | {course4:>20} | {teacher4}")

# last row
print("+--------------------------------------------------+")