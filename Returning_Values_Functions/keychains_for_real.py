running = True
num_chains = 0
price_per_chain = 10
sales_tax = 1.13
shipping_cost = 5
extra_shipping = 1

def add_keychains(add):
    global num_chains
    num_chains += add
    return num_chains

def remove_keychains(remove):
    global num_chains
    if num_chains > 0 and num_chains - remove >= 0: 
        num_chains -= remove
    
    elif num_chains - remove < 0:
        num_chains = 0
    return num_chains

def view_order(num_chains: int, price_per_chain: float, sales_tax: float, shipping_fee: int, extra_shipping: int):
    print(f"You have {num_chains} keychains.")
    print(f" The price per keychain is ${price_per_chain}.")
    print(f"Total cost is ${(price_per_chain * num_chains * sales_tax) + shipping_fee + extra_shipping*num_chains}.")

def checkout(name, info):
    print(f"Name of receiver: {name}")
    print(f"Address to deliver to: {info}")
    print(f"Thank you for ordering {name}")

def main():
    global running
    print(" (1) Add Keychains \n (2) Remove Keychains from Order \n (3) View Current Order \n (4) Checkout \n")

    try:
        choice  = int(input("Please enter your choice: "))
        
        if choice == 1:
            add = int(input((f"You have {num_chains} keychains. How many to add? ")))
            print(f"You now have {add_keychains(add)} keychains.")
        
        elif choice == 2:
            remove = int(input(f"You have {num_chains} key_chains. How many to remove? "))
            print(f"You now have {remove_keychains(remove)} keychains.")
        
        elif choice == 3:
            view_order(num_chains, price_per_chain, sales_tax, shipping_cost, extra_shipping)
        
        elif choice == 4:
            name = input("Name: ")
            info = input("Delivery Information: ")
            checkout(name, info)
            running = False
        
    except ValueError:
        print("error")
    
    print("\n")
    
while running == True:
    if __name__ == "__main__":
        main()