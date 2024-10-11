while True:

    phrase = input()

    x_index = 0
    x_iteration = False
    y_found = False
    z_found = False

    for i in range(len(phrase)):
        if phrase[i] == "x":
            if i == 0:
                x_index = i
                x_iteration = True
            elif phrase[i-1] != ".":
                x_index = i
                x_iteration = True
        
        elif phrase[i] == "y" and i != x_index + 1:
            x_iteration = False
        
        elif phrase[i] == "z" and i != x_index + 2:
            x_iteration = False

        elif phrase[i] == "y" and i == x_index + 1:
            y_found = True
        
        elif phrase[i] == "z" and i == x_index + 2 and y_found == True:
            z_found = True

    if x_iteration == True and y_found == True and z_found == True:
        print("True")

    else:
        print("False")