while True:
    a = input()
    b = input()
    final_str = ""
    saved_str = ""
    moved = False

    if len(a) < len(b):
        saved_str = a
        a = b
        b = saved_str
        moved = True

    for i in range(len(a)):

        if i <= len(b) - 1 and moved == False:
            final_str += a[i]
            final_str += b[i]
        
        elif i <= len(b) - 1 and moved == True:
            final_str += b[i]
            final_str += a[i]
        
        else:
            final_str += a[i:]
            break

    print(final_str)