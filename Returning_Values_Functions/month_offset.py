def main():
    print(f"Offset for month 1: {month_offset(1)}")
    print(f"Offset for month 2: {month_offset(2)}")
    print(f"Offset for month 3: {month_offset(3)}")
    print(f"Offset for month 4: {month_offset(4)}")
    print(f"Offset for month 5: {month_offset(5)}")
    print(f"Offset for month 6: {month_offset(6)}")
    print(f"Offset for month 7: {month_offset(7)}")
    print(f"Offset for month 8: {month_offset(8)}")
    print(f"Offset for month 9: {month_offset(9)}")
    print(f"Offset for month 10: {month_offset(10)}")
    print(f"Offset for month 11: {month_offset(11)}")
    print(f"Offset for month 12: {month_offset(12)}")
    print(f"Offset for month 43: {month_offset(43)}")


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


if __name__ == "__main__":
    main()
