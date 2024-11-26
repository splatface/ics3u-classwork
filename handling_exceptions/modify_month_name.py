def month_name(month_num):

    if month_num == 1:
        return "January"
    
    elif month_num == 2:
        return "February"
    
    elif month_num == 3:
        return "March"

    elif month_num == 4:
        return "April"
    
    elif month_num == 5:
        return "May"
    
    elif month_num == 6:
        return "June"
    
    elif month_num == 7:
        return "July"
    
    elif month_num == 8:
        return "August"

    elif month_num == 9:
        return "September"
    
    elif month_num == 10:
        return "October"
    
    elif month_num == 11:
        return "November"
    
    elif month_num == 12:
        return "December"

def main():
    while True:
        convertible = True
        try:
            try: 
                month = int(input("What month? "))

            except ValueError:
                print("Please enter an integer.")
                convertible = False

            if convertible == True:
                if month > 0 and month <= 12:
                    print(month_name(month))
                    break
                else:
                    raise ValueError
            
        except ValueError:
            print("Month out of range. Pick a number from 1-12.")
        

if __name__ == "__main__":
    main()