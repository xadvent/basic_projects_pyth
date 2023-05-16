import os
def get_price():
    while True:
        price = input("Please enter the price: $")
        try:
            price = float(price)
            if price > 0:
                break
            else: print("Number must be above 0")
        except ValueError:
            print("Please enter a numerical value.")
    return round(price, 2)

def get_tip():
    while True:
        tip = input("Please enter the desired tip amount: ")
        try: 
            tip = float(tip)
            if tip > 0:
                tip = tip / 100
                break
            else: print("Tip must be positive number.")
        except ValueError: 
            print("Tip must be a number.")
    return tip


def get_all():
    all_prices = []
    while True:
        os.system('clr' if os.name == 'nt' else 'clear')
        print(f"All payments are as follows: {all_prices}")
        price = get_price()                                         #could make code look cleaner
        tip = get_tip()
        tip_amount = round(price * tip, 2)
        total_price = round(price + tip_amount, 2)
        all_prices.append(total_price)
        
        print(f"\nThe tip amount of {tip*100}% comes out to {tip_amount}.\nThe new price is ${total_price}.\n")
        play_again = input("\nIf you have more amounts, please press enter.\nIf not, press q to quit. ")
        if play_again == 'q':
            os.system('clr' if os.name == 'nt' else 'clear')
            print(f"${sum(all_prices)} is the total cost.")
            print("Thank you for using my program. :)")
            break
        else:
            print("")

get_all()

