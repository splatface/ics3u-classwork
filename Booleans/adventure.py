print("WElCOME TO THE NONSENSICAL ADVENTURE!")

print("Currently, you are in your basement. Unfortunately, your basement is unimaginably big and you've gotten lost. You want to leave but can't figure out how.")
print("In front of you, you see two giant cartoon hands. One points to the right at a door saying [EXIT] in big bold letters.")
print("The other points to the left at a well-lit hallway that looks pretty familiar.")
room_1 = str(input("Which direction would you like to go in? Left or right?\n"))

#going left
if room_1.lower() == "left":
    print("\n\nYou decide to move in the direction of the [EXIT] door. However, the space behind the door is seemingly empty.")
    print("As you take a step into the space, the floor suddenly falls out from beneath you! You plummet through the ground and land with a SMACK onto ... soil?")
    print("You gather yourself and look around for a good minute, noting down the fact that the [EXIT] sign probably wasn't an exit to the world you remember considering the strange creatures and the glowing light in front of you.")
    print("As you contemplate your poor decision to enter that door, you realize that perhaps you fell out of that glowing light a few meters in front of you.")
    print("Unfortunately, you seem to be blocked from going back through as while you were lost in thought, the creatures have already surrounded the door.")
    room_2 = str(input("Do you want to make a run for that glowing light despite the fantastical creatures, or would you like to stay behind, giving up on your only chance to leave? stay or run?\n"))

    # running to get through monsters
    if room_2.lower() == "run":
        print("\n\nYou have decided to make a break for it even as those creatures stand in your way.")
        print("As you run like never before, you are suddenly tackled by a creature with a long neck and surrounded on all sides.")
        print("After a not-so-forceful struggle, you succumb to the creatures and will never make it back to your homeland.")
        print("..."*10)
        print("..."*10)
        print("..."*10)
        print("Despite everything, you aren't dead yet! What a miracle!")
        print("You see an opening and make a mad dash for it with the monsters still hot on your heels.")
        room_4 = str(input("Finding a cave to the left, do you go in? Yes or no?\n"))
        
        # ending1
        if room_4.lower() == "yes":
            print("\n\nYou enter and see a small lake with a few giant eggs beside it.")
            print("Although starved, you decide against eating them. You stay in the cave waiting the monsters out, deciding not to eat those suspicious eggs or drink from that possibly unclean pond water.")
            print("After waiting for a few days, the eggs hatch and a large, reddish bird enters the cave. It takes one look at you and offs you, preparing you as food for its young.")
            print("Ending: ")
            quit()
        
        # ending2
        elif room_4.lower() == "no":
            print("\n\nYou do not enter the cave and continue running!")
            print("Just as you are about to run out of stamina, you swiftly come to a decision:")
            print("You throw your strongest kick at a monster to your left who is closing in, shouting, 'How'd you like that, little dude!' However, the moment you let loose that 'insult' (what kind of insult is that???) the nearby monsters look at you and ram you into a tree.")
            print("Ending: Poor language...")
            quit()
            
    # don't go to the glowing light
    elif room_2.lower() == "stay":
        print("\n\nYou have decided to stay! That may have been the best decision to make as just at that moment, the creatures gather in front of the glowing light, making it impossible to go past.")
        print("Your stomach rumbles and you realize that the last time you ate was over 20 hours ago.")
        print("You look around again and see a couple of bright red fruits on a tall tree.")
        room_5 = str(input("Do you climb the tree or stay hungry? Climb or starve?\n"))

        # ded 3
        if room_5.lower() == "climb":
            print("\n\nYou have chosen to climb the tree. Unfortunately, the moment you begin to climb the tree, you are pricked by hundreds of tiny needles in the tree's trunk.")
            print("You give up on climbing the tree, but the world starts to blur and suddenly, you feel as though you are upside-down with all the blood rushing to your head.")
            print("You realize that something is very, very, VERY wrong. Somewhat weirdly, a random humanoid creature appears in front of you (upside-down of course) and hands you a nice, clear bottle of viscous liquid.")
            print("The creature stares down at you, almost like an invitation to drink up!")
            print("Entranced, you do, and immediately, you start to feel even worse. You don't even know why you drank it to begin with, however, you know that you've screwed up and your life is probably over.")
            print("Ending: Kidnapped? Killed? Mugged? Poisoned?")
            quit()
        
        # ded 4
        elif room_5.lower() == "starve":
            print("\n\nYou've quite literally chosen the path of death. You have died. It is fully your fault.")
            print("Ending: It wasn't a joke...")
            quit()
        
        

elif room_1.lower() == "right":
    print("You start walking towards the familiar corridor to the right. As you do, you get jumpscared by a can of paint which falls directly on your head!")
    print("You grumble and find a table has magically appeared in front of you after cleaning the paint off your eyes.")
    room_3 = str(input("On it are two items: an axe and a towel. Which do you pick up? Axe or towel?\n"))

    if room_3 == "axe":
        print("You pick up the axe, or you try to. The axe doesn't actually come off of the table. It is 100% stuck there. You also try to remove your hands from the axe but they are also stuck.")
        print("Just as you're contemplating your life choices, you are approached by someone or something that should NOT be in YOUR HOUSE. It's your best friend with their hand outstretched, a silent offer in the air.")
        room_6 = str(input("Do you accept this offer with a verbal greeting? Or do you ignore him? Accept or ignore?"))

        if room_6.lower() == "accept":
            print("As you open your mouth to greet your friend's silent offer (perhaps and hopefully of help), he draws near and you realize the thing in his hand is a bottle of water. He pours it over your hands and suddenly, you aren't stuck anymore.")
            print("Your friend isn't speaking, an instead, your friend starts to walk to the other side of the corridor, not waiting for you to catch up.")
            print("Ending: ...replaced?")
            quit()
        
        if room_6.lower() == "ignore":
            print("You decide to ignore your best friend thinking that something is wrong with them. Apparently, something is because the moment you turn away, you hear a deafening screech.")
            print("You quickly turn back around but are immediately eaten(?) by a monstrous creature who is most definitely NOT your best friend (after all, your friend probably can't unhinge their jaw to swallow you whole...)")
            print("Ending: uhhh friendly fire?")
            quit()
    
    if room_3 == "towel":
        print("You pick up the towel and wipe the paint off of yourself. After doing so, you drop the towel back onto the table and start walking down the corridor again.")
        print("You hear a noise behind you and look back, seeing nothing.")
        room_7 = str(input("Do you continue on or do you stop in place? Continue or stop?"))

        if room_7.lower() == "continue":
            print("You are suddenly ambushed by a random figure.")
            print("Ending: death by thing")
            quit()
        
        if room_7.lower() == "stop":
            print("You stop in place and see something coming for you. Unfortunately, you are extremely slow.")
            print("Ending: turtlish")
            quit()