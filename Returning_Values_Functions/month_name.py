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

    else:
        return "error"

def main():
    print("Month 1: " + month_name(1))
    print("Month 2: " + month_name(2))
    print("Month 3: " + month_name(3))
    print("Month 4: " + month_name(4))
    print("Month 5: " + month_name(5))
    print("Month 6: " + month_name(6))
    print("Month 7: " + month_name(7))
    print("Month 8: " + month_name(8))
    print("Month 9: " + month_name(9))
    print("Month 10: " + month_name(10))
    print("Month 11: " + month_name(11))
    print("Month 12: " + month_name(12))
    print("Month 43: " + month_name(43))

if __name__ == "__main__":
    main()