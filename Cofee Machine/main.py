# Importing necessary dictionaries for the coffee machine's menu and resources
from menu import items_menu
from menu import resources
from menu import display_welcome
from menu import display_latte
from menu import display_cappuccino
from menu import display_espresso
from menu import display_report

# Function to get coins from the user and calculate the total money added
def get_coins():
    global user_prompt, coffee_cost, money_added, pennies, nickels, dimes, quarter

    # Get the cost of the selected coffee from the menu
    coffee_cost = items_menu[user_prompt]["cost"]
    print(f"\nCost of {user_prompt} is ${coffee_cost}")

    # Prompt user to input the number of each type of coin
    quarter = int(input("\nEnter Quarters: "))
    dimes = int(input("\nEnter Dimes: "))
    nickels = int(input("\nEnter Nickels: "))
    pennies = int(input("\nEnter Pennies: "))

    # Calculate the total amount of money added
    money_added = (quarter * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    print(f"\nMoney Added in Machine: ${money_added}")


def display_coffee():
    global user_prompt
    if user_prompt == "latter":
        display_latte()
    elif user_prompt == "cappuccino":
        display_cappuccino()
    elif user_prompt == "espresso":
        display_espresso()


# Function to check if the user has provided enough money and handle change or refund
def price_checker():
    global coffee_cost, money_added
    # Calculate the amount of change to give back
    if money_added - coffee_cost > 0:
        # If there's extra money, provide the change and register the sale as profit
        print(f"\nHere is your ${round(money_added - coffee_cost)} change!")
        resources["profit"] = coffee_cost
        return True
    elif money_added < coffee_cost:
        # If the user hasn't provided enough money, refund the money and cancel the transaction
        print(f"\nSorry that's not enough money. Money refunded: ${money_added}\n\n")
        return False
    elif money_added == coffee_cost:
        # If the exact amount was given, register the sale as profit
        resources["profit"] = coffee_cost
        return True

# Function to dispense the coffee and deduct the used resources from the machine
def give_coffee_deduct_resources():
    global user_prompt, water_in_machine, milk_in_machine, coffee_in_machine
    display_coffee()

    # Access the ingredients using the value of the user_prompt variable IMP:Don't use "user_prompt" because it is
    # already a string
    water_to_deduct = items_menu[user_prompt]["ingredients"]["water"]
    milk_to_deduct = items_menu[user_prompt]["ingredients"]["milk"]
    coffee_to_deduct = items_menu[user_prompt]["ingredients"]["coffee"]

    # Deduct the required resources from the machine's resources
    resources["water"] = water_in_machine - water_to_deduct
    resources["milk"] = milk_in_machine - milk_to_deduct
    resources["coffee"] = coffee_in_machine - coffee_to_deduct

# Function to initialize the machine's resource levels
def creating_variables():
    global water_in_machine, user_prompt, milk_in_machine, coffee_in_machine
    water_in_machine = resources["water"]
    milk_in_machine = resources["milk"]
    coffee_in_machine = resources["coffee"]

# Function to check if enough resources are available to make the selected coffee
def check_resources():
    global water_in_machine, user_prompt, milk_in_machine, coffee_in_machine

    # Check resources based on the type of coffee requested
    if user_prompt == "espresso":
        if water_in_machine >= 50:
            if coffee_in_machine >= 18:
                return True
            else:
                return False
    elif user_prompt == "latte":
        if water_in_machine >= 200:
            if coffee_in_machine >= 24:
                return True
            else:
                return False
    elif user_prompt == "cappuccino":
        if water_in_machine >= 250:
            if coffee_in_machine >= 24:
                if milk_in_machine >= 100:
                    return True
                else:
                    return False


# Initialize the machine's resource levels and the financial variables
water_in_machine, milk_in_machine, coffee_in_machine= 0,0,0
coffee_cost, money_added, pennies, nickels, dimes, quarter = 0,0,0,0,0,0


#<------------------------------|||          From Here Program Starts          |||------------------------------>
# Main program loop that runs the coffee machine
while 2 > 0:
    display_welcome()
    # Handle invalid input
    while 2 > 0:
        print("\nCoffee Menu: (espresso/latte/cappuccino)\nGet the info about resources available: (report)\nTurn Off the Machine: (off)")
        user_prompt = input("\nWhat would you like:  ").lower()
        if user_prompt == "latte" or user_prompt == "espresso" or user_prompt == "cappuccino" or user_prompt == "report" or user_prompt == "off":
            break
        else:
            print("\nWrong Input")
            continue
    creating_variables()
    while 2 > 0:
        # Display the remaining resources if the user asks for a report
        if user_prompt == "report":
            display_report(water_in_machine, milk_in_machine, coffee_in_machine)
            break
        # Check if the user selected "latte", and if so, check if enough resources are available
        elif user_prompt == "espresso":
            if check_resources():
                get_coins()
                if price_checker():
                    give_coffee_deduct_resources()
                    break
                else:
                    break
            # Check if the user selected "cappuccino", and if so, check if enough resources are available
            else:
                print(f"\nSorry! Not Enough Resources for {user_prompt}")
                break
        # Check if the user selected "latte", and if so, check if enough resources are available
        elif user_prompt == "latte":
            if check_resources():
                get_coins()
                if price_checker():
                    give_coffee_deduct_resources()
                    break
                else:
                    break
            # Check if the user selected "cappuccino", and if so, check if enough resources are available
            else:
                print(f"\nSorry! Not Enough Resources for {user_prompt}")
                break
        elif user_prompt == "cappuccino":
            if check_resources():
                get_coins()
                if price_checker():
                    give_coffee_deduct_resources()
                    break
                else:
                    break
            else:
                print(f"\nSorry! Not Enough Resources for {user_prompt}")
                break
        # Turn off the machine if the user enters "off"
        elif user_prompt == "off":
            break


    # Exit the main loop and turn off the machine if the user enters "off"
    if user_prompt == "off":
        print("\nPowering off... Goodbye! Have Nice Time")
        break