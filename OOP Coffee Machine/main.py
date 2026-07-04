from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cost_of_coffee = 0
menu = Menu()
coffee_machine  = CoffeeMaker()
coffee_money_machine = MoneyMachine()

is_on = True
while is_on:
    print(f"\nCoffee Items: {menu.get_items()}\nGet Report of Resources: (report)\nTurn Off the Machine: (off)")
    user_order = input("\nWhat would You Like: ").lower()

    if user_order == "report":
        print("\n")
        coffee_machine.report()
        coffee_money_machine.report()
    elif user_order == "off":
        print("\nPowering Off.... Goodbye, Have Nice Time!")
        is_on = False
    else:
        chosen_drink = menu.find_drink(user_order)
        if coffee_machine.is_resource_sufficient(chosen_drink):
            print(f"Cost of {user_order}: ${chosen_drink.cost}")
            if coffee_money_machine.make_payment(chosen_drink.cost):  #cost_of_coffee = chosen_drink.cost
                coffee_machine.make_coffee(chosen_drink)