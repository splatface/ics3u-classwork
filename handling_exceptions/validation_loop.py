def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break #doesn't break out of the while loop if it goes into the except block as the break is a part of the try
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()