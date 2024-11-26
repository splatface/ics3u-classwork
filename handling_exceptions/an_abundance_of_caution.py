def percent(decimal: float) -> int:
    if type(decimal) != float and type(decimal) != int:
        raise TypeError("Value not a decimal or integer.")
    
    if decimal < 0.0 or decimal > 1.0:
        raise ValueError("Value out of range")

        
    percentage = round(decimal * 100)

    return percentage

def main():
    num = percent(0.5)
    print(num)

if __name__ == "__main__":
    main()