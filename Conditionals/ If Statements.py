# If Intro:

#  if statements will run the code indented in it if the condition is true
# by indenting the if statement, the computer will know to run that indented code only if the condition is met
# += ____ is like doing variable = variable + ____
# -= ____ is like doing variable = variable - ____

robot_location = 20
ball_location = 30
goal_location = 10
have_ball = False

if robot_location < ball_location:
    print("Almost at the ball")

if robot_location > goal_location:
    print("You are beyond the goal.")

if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 10
print("Moving forward 5.")

if robot_location == goal_location:
    print("At the goal.")

if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 20
print("Moving back 15.")

if robot_location < goal_location:
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    print("You reached the goal and scored!")
    have_ball = False



# How Old Are You?

age = int(input("How old are you?"))

if age < 16:
    print("You can't drive.")

if age < 18:
    print("You can't vote.")

if age < 21:
    print("You can't rent a car.")

if age >= 21:
    print("You can do anything legal.")
