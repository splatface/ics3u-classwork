while True:

    phrase = input()

    b_index1 = 0
    b_found = False
    found = False
    bbb_case = 0

    for i in range(len(phrase)):
        if phrase[i] == "b" and b_found == False:
            b_index1 = i
            b_found = True
        
        elif phrase[i] == "b" and b_found == True:
            if b_index1 + 2 == i:
                found = True
            
            elif b_index1 + 1 == i and bbb_case + 2 == i:
                found = True
        
            else:
                bbb_case = b_index1
                b_index1 = i

    if found == True:
        print("True")
    
    else:
        print("False")