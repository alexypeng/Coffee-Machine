# Simple coffee machine created by Alexander Peng on 2024/07/29. First project created using PyCharm.

from data import MENU, COFFEE_EMOJI

# List that keeps track of the store's resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(item_name):
    """Checks if there are enough resources to make the chosen coffee."""
    missing_ingredient = ""
    has_enough = False
    if resources["water"] < MENU[item_name]["ingredients"]["water"]:
        missing_ingredient = "water"
    elif resources["milk"] < MENU[item_name]["ingredients"]["milk"]:
        missing_ingredient = "milk"
    elif resources["coffee"] < MENU[item_name]["ingredients"]["coffee"]:
        missing_ingredient = "coffee"
    else:
        has_enough = True

    if has_enough:
        return "enough"
    return f"Sorry, there is not enough {missing_ingredient}."


def make_drink(item_name):
    """Subtracts the used resources from the resource tracking list. Returns a string which includes the coffee chosen
    by the user"""
    for ingredient in resources:
        resources[ingredient] -= MENU[item_name]["ingredients"][ingredient]
    return f"Here is your {item_name} {COFFEE_EMOJI}. Enjoy!"

def report(money):
    """Returns a formatted string with all the resources."""
    final_report = ""
    for resource in resources:
        final_report += f"{resource}: {resources[resource]}"
        if resource != "coffee":
            final_report += "ml\n"
        else:
            final_report += "g\n"
    final_report += f"money: ${money:.2f}"
    return final_report

def check_money(item, money_in):
    """Checks if enough money was made to purchase the chosen coffee."""
    if money_in >= MENU[item]["cost"]:
        money_in -= MENU[item]["cost"]
        return money_in
    return -1

def collect_money():
    """Asks for how much money the user paid. Returns the dollar value."""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def coffee_machine():
    """Main driver function"""
    choice = ""
    money = 0
    while choice != "off":
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        choice = choice.lower()
        if choice == "report":
            print(report(money))
        elif choice == "off":
            print()
        else:
            resource_update = check_resources(choice)
            if resource_update != "enough":
                print(resource_update)
            else:
                print("Please insert coins.")
                money_in = collect_money()
                change = check_money(choice, money_in)
                if change == -1:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    money += MENU[choice]["cost"]
                    print(f"Here is ${change:.2f} in change.")
                    print(make_drink(choice))

coffee_machine()