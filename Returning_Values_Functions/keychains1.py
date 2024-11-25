running = True

def add_keychains():
    return "ADD KEYCHAINS"

def remove_keychains():
    return "REMOVE KEYCHAINS"

def view_order():
    return "VIEW ORDER"

def checkout():
    return "CHECKOUT"

def main():
    global running
    print(" (1) Add Keychains \n (2) Remove Keychains from Order \n (3) View Current Order \n (4) Checkout \n")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        print(add_keychains())
    
    elif choice == 2:
        print(remove_keychains())
    
    elif choice == 3:
        print(view_order())
    
    elif choice == 4:
        print(checkout())
        running = False
    
    print("\n\n")
    
while running == True:
    if __name__ == "__main__":
        main()