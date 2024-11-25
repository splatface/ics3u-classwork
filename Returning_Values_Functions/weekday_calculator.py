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

def month_offset(month: int) -> int:
    if month == 1 or month == 10:
        return 1
    
    elif month == 2 or month == 3 or month == 11:
        return 4
    
    elif month == 4 or month == 7:
        return 0

    elif month == 5:
        return 2
    
    elif month == 6:
        return 5
    
    elif month == 8:
        return 3

    elif month == 9 or month == 12:
        return 6
    
    else:
        return -1



def weekday(mm: int, dd: int, yyyy: int) -> str:
    years_since_1900 = yyyy - 1900  # step 1
    total = years_since_1900 // 4  # step 2

    # steps 3-7 go here
    total += years_since_1900
    total += dd-1
    total += month_offset(mm)

    if (mm == 1 or mm == 2) and is_leap(yyyy) == True:
        total -= 1
    
    remainder = total % 7
    weekday = weekday_name(remainder)

    date_string = f"{weekday}, {month_name(mm)} {dd}, {yyyy}"  # step 8

    return date_string


# paste your functions from month_name, weekday_name, and month_offset here

def weekday_name(num):
    if num == 1:
        return "Monday"

    elif num == 2:
        return "Tuesday"
    
    elif num == 3:
        return "Wednesday"

    elif num == 4:
        return "Thursday"

    elif num == 5:
        return "Friday"

    elif num == 6:
        return "Saturday"

    elif num == 0:
        return "Sunday"
    
    else:
        return "error"

def is_leap(year: int) -> bool:
    # years which are evenly divisible by 4 are leap years,
    # but years divisible by 100 are not leap years,
    # though years divisible by 400 are leap years

    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    
    return result

def main():
    print("Welcome to Mr. Gallo's fantastic birth-o-meter!")
    print()
    print("All you have to do is enter your birthday, and it will tell you")
    print("the day of the week on which you were born.")
    print()
    print("Some automatic tests....")
    print(f"12 10 2003 => {weekday(12, 10, 2003)}")  # Wednesday, December 10, 2003
    print(f"2 13 1976 => {weekday(2, 13, 1976)}")  # Friday, February 13, 1976
    print(f"2 13 1977 => {weekday(2, 13, 1977)}")  # Sunday, February 13, 1977
    print(f"7 2 1974 => {weekday(7, 2, 1974)}")  # Tuesday, July 2, 1974
    print(f"1 15 2003 => {weekday(1, 15, 2003)}")  # Wednesday, January 15, 2003
    print(f"10 13 2000 => {weekday(10, 13, 2000)}")  # Friday, October 13, 2000

    print("Now it's your turn!  What's your birthday?")
    print("Birth date (mm dd yyyy): ")
    mm = int(input("mm: "))
    dd = int(input("dd: "))
    yyyy = int(input("yyyy: "))
    
    # put a function call for weekday() here
    print(f"\nYou were born on {weekday(mm, dd, yyyy)}")


if __name__ == "__main__":
    main()