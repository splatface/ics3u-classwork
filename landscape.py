import pygame
import random

pygame.init()

# screen sizes
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#time presets
day = False
screen_colour = [224, 181, 110]
midday = False

#moon presets
moon_x = -30
moon_y = 330
last_time_moon = 0
moon_colour = (255, 255, 255)

#tree presets
tree = [120, 90]
last_time_trees = 0

#house presets
house_x = 410

#wind presets
wind_x_set = [-80]
wind_y_set = [100]
last_time_winds = 0

#ghost presets
ghost_head_x = random.randint(100, 500)
ghost = [[ghost_head_x-40, 350], [ghost_head_x+40, 350], [ghost_head_x+40, 410]]
ghost_x = ghost_head_x+40
ghost_hit = False
ghost_colour = (255, 255, 255)
ghost_last_time = 0

#ghost presets for polygon of ghost sheets
while ghost_x >= ghost_head_x-40:
    if len(ghost) % 2:
        ghost.append([ghost_x, 410])
    else:
        ghost.append([ghost_x, 420])
    ghost_x -= 10

#smoke presets
smoke_y = [-25]
smoke_last_time = 0
smoke_x = [random.randint(400, 420)]
time_between = random.randint(100, 400)

#minus symbol
minus_y = [0]
minus_x = [random.randint(ghost_head_x-60, ghost_head_x-30)]
minus_last_time = 0

#plus symbol
plus_y = [0]
plus_x = [random.randint(ghost_head_x-60, ghost_head_x-30)]
plus_last_time = 0


#MAIN LOOP ********************************** MAIN LOOP#
running = True
while running:
    ghost_minus = random.randint(500, 900)
    current_time = pygame.time.get_ticks()

    house_x = 410
    
    #EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    L, M, R = pygame.mouse.get_pressed()
    

    #GAME UPDATES:

    #moon parabola
    if current_time - last_time_moon >= 1000:
        moon_x += 1
        moon_y = 0.0025*(moon_x-320)**2

    #moon colour settings (turns into sun)
    if moon_x >= 670:
        if day == False:
            day = True
            moon_x = -30
            moon_colour = (255, 255, 0)
        
        else:
            day = False
            moon_x = -30
            moon_colour = (255, 255, 255)
    
    if moon_x > 106 and moon_x < 533:
        midday = True

    #makes the trees sway every 1s (1000ms)
    if current_time - last_time_trees >= 800:
        if tree[0] > 121:
            tree[0] -= 5
        else:
            tree[0] += 5
        last_time_trees = current_time

    #ghost hit walls back and forth
    if day == False or (day == True and midday == False):
        for a in range(len(ghost)):
            for x in range(len(ghost[a])):
                if x == 0 and ghost_hit == False:
                    ghost[a][0] += 3
                    ghost_head_x += 0.25
                elif x == 0 and ghost_hit == True:
                    ghost[a][0] -= 3
                    ghost_head_x -= 0.25
    
    if ghost_head_x > 600:
        ghost_hit = True
    
    if ghost_head_x < 40:
        ghost_hit = False

    #ghost colour changes between day and night
    if (midday == True and day == True) or (day == True and current_time - ghost_last_time > 200) or L == True: #turns red
        ghost_colour = (224, 127, 110)
    elif midday == False and day == True: #turns white
        ghost_colour = (255, 255, 255)
    elif day == False: #turns white
        ghost_colour = (255, 255, 255)
    if R == True: #turns green
        ghost_colour = (50, 220, 100)
        ghost_last_time = current_time
    

    #sets screen colour (gradient)
    if midday == True:
        screen.fill(screen_colour)
    
    if day == False:
        if moon_x <= 106:
            screen.fill(screen_colour)
            if screen_colour[0] > 34:
                screen_colour[0] -= 1.45
            if screen_colour[1] > 36:
                screen_colour[1] -= 1.4
            if screen_colour[2] > 51:
                screen_colour[2] -= 0.75

        elif moon_x >= 533:
            screen.fill(screen_colour)
            if screen_colour[0] < 224:
                screen_colour[0] += 1.45
            if screen_colour[1] < 181:
                screen_colour[1] += 1.4
            if screen_colour[2] < 110:
                screen_colour[2] += 0.75
        
    elif day == True:
        if moon_x <= 106:
            screen.fill(screen_colour)
            if screen_colour[0] > 134:
                screen_colour[0] -= 0.8
            if screen_colour[1] < 240:
                screen_colour[1] += 0.45
            if screen_colour[2] < 219:
                screen_colour[2] += 1.0
    
        if moon_x >= 533:
            screen.fill(screen_colour)
            if screen_colour[0] < 224:
                screen_colour[0] += 0.8
            if screen_colour[1] > 181:
                screen_colour[1] -= 0.45
            if screen_colour[2] > 110:
                screen_colour[2] -= 1.0

    #plus symbol
    if day == False or plus_y[-1] > 275 or R == True:
        if current_time - plus_last_time > ghost_minus and (day == False or R == True):
            plus_x.append(random.randint(ghost_head_x-60, ghost_head_x-30))
            plus_y.append(random.randint(310, 350))
            plus_last_time = current_time

    #minus symbol
    if day == True or minus_y[-1] > 275 or L == True:
        if current_time - minus_last_time > ghost_minus and (day == True or L == True):
            minus_x.append(random.randint(ghost_head_x-60, ghost_head_x-30))
            minus_y.append(random.randint(310, 350))
            minus_last_time = current_time



    #DRAWING:

    #moon/sun drawing
    pygame.draw.circle(screen, (moon_colour), (moon_x, moon_y), 30)

    #ground
    pygame.draw.rect(screen, (82, 66, 57), (0, 300, 640, 180))

    #tree #1 (in front of right house)
    pygame.draw.rect(screen, (18, 31, 41), (485, 100, 30, 200))
    pygame.draw.circle(screen, (55, 94, 62), (tree[0]+380, tree[1]+40), 60)
    pygame.draw.circle(screen, (55, 87, 58), (tree[0]+410, tree[1]+70), 55)
    pygame.draw.circle(screen, (49, 82, 59), (tree[0]+340, tree[1]+90), 68)
    pygame.draw.circle(screen, (55, 87, 58), (tree[0]+430, tree[1]+115), 68)

    #smoke generation
    if day == True:
        if current_time - smoke_last_time > time_between:
            smoke_y.append(125)
            smoke_x.append(random.randint(400, 420))
            smoke_last_time = current_time
            time_between = random.randint(170, 750)

    if day == True or (day == False and smoke_y[-1]>0):
        for a in range(len(smoke_y)):   
            pygame.draw.ellipse(screen, (74, 81, 97), (smoke_x[a], smoke_y[a], 25, 25))

            smoke_y[a] -= 2
            smoke_x[a] += 0.5
    
    #house
    while house_x >= 200:
        #base
        pygame.draw.rect(screen, (40, 40, 92), (house_x, 125, 30, 50))
        pygame.draw.rect(screen, (40, 40, 92), (house_x-90, 220, 150, 100))
        pygame.draw.polygon(screen, (65, 65, 128), ((house_x-100, 220), (house_x+70, 220), (house_x-15, 120)))

        #windows
        pygame.draw.rect(screen, (207, 207, 78), (house_x-70, 240, 30, 30))
        pygame.draw.rect(screen, (207, 207, 78), (house_x+10, 240, 30, 30))

        house_x -= 200


    #tree #2 (in front of left house)
    pygame.draw.rect(screen, (18, 31, 41), (105, 100, 30, 240))
    pygame.draw.circle(screen, (55, 94, 62), (tree), 60)
    pygame.draw.circle(screen, (55, 87, 58), (tree[0]+30, tree[1]+30), 55)
    pygame.draw.circle(screen, (49, 82, 59), (tree[0]-40, tree[1]+50), 68)
    pygame.draw.circle(screen, (55, 87, 58), (tree[0]+50, tree[1]+75), 68)



    #wind
    if current_time - last_time_winds >= 3000: #makes new wind after 3s
        wind_x_set.append(-80) #adds new wind's x value to the list of them all
        wind_y_set.append(random.randint(0, 270)) #adds new wind's y value to the list of them all
        last_time_winds = current_time
    
    for a in range(len(wind_x_set)): #updates all wind drawings
        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a], wind_y_set[a], 80, 30), 3, 0.5)
        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a]+40, wind_y_set[a], 40, 30), 1, 3)

        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a]-30, wind_y_set[a]-50, 80, 30), 3, 0.5)
        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a]-30 + 40, wind_y_set[a]-50, 40, 30), 1, 3)

        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a]-40, wind_y_set[a]+50, 80, 30), 3, 0.5)
        pygame.draw.arc(screen, (255, 255, 255), (wind_x_set[a]-40 + 40, wind_y_set[a]+50, 40, 30), 1, 3)

        wind_x_set[a] += 3


    #ghost
    pygame.draw.circle(screen, (ghost_colour), (ghost_head_x, 350), 40)
    pygame.draw.polygon(screen, (ghost_colour), ghost)
    pygame.draw.circle(screen, (0, 0, 0), (ghost_head_x-17, 355), 10)
    pygame.draw.circle(screen, (0, 0, 0), (ghost_head_x+17, 355), 10)
    pygame.draw.ellipse(screen, (0, 0, 0), (ghost_head_x-10, 360, 20, 30))


    #minus symbol
    for i in range(len(minus_x)):
        if minus_y[i] >= 250:
            pygame.draw.rect(screen, (255, 0, 0), (minus_x[i], minus_y[i], 15, 5))
            minus_y[i]-= 2
        
        if ghost_hit == False and (midday == False or day == False):
            minus_x[i] += 3
        
        elif ghost_hit == True and (midday == False or day == False):
            minus_x[i] -= 3

    #plus symbol
    for i in range(len(plus_x)):
        if plus_y[i] >= 250:
            pygame.draw.rect(screen, (0, 255, 0), (plus_x[i], plus_y[i], 15, 5))
            pygame.draw.rect(screen, (0, 255, 0), (plus_x[i]+5, plus_y[i]-5, 5, 15))
            plus_y[i]-= 2
        
        if ghost_hit == False:
            if (day == True and midday == False) or day == False:
                plus_x[i] += 3
        
        elif ghost_hit == True:
            if (day == True and midday == False) or day == False:
                plus_x[i] -= 3

    #shows screen and sets framerate/refresh rate
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
