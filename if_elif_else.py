team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

# as team a has more points, they win and get 16 total wins, tying with team b
if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points: # will test this if the condition in the if statement above is not met
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
if team_b_wins > team_a_wins: # doesn't do much just takes a bit more time to run (like negligible rn tho)
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")