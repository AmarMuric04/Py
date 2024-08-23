MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappucino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 1.7,
    },
}

resources = {"water": 100, "milk": 50, "coffee": 76, "money": 2.5}


def check_resources(drink):
    if "milk" in drink and drink["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk for this drink.")
        return False
    if "coffee" in drink and drink["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee for this drink.")
        return False
    if "water" in drink and drink["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water for this drink.")
        return False
    return True


def enough_money(resources, drink, inserted):
    if inserted < drink["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        if "water" in drink["ingredients"]:
            resources["water"] -= drink["ingredients"]["water"]
        if "milk" in drink["ingredients"]:
            resources["milk"] -= drink["ingredients"]["milk"]
        if "coffee" in drink["ingredients"]:
            resources["coffee"] -= drink["ingredients"]["coffee"]
        resources["money"] += inserted
        print("Enjoy your drink!")
        if inserted > drink["cost"]:
            change = inserted - drink["cost"]
            resources["money"] -= change
            print(f"Here's ${change:.2f} in change.")
    return resources


def insert_money(resources, drink):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    quarters_inserted = int(input("Quarters: ")) * quarters
    dimes_inserted = int(input("Dimes: ")) * dimes
    nickles_inserted = int(input("Nickles: ")) * nickles
    pennies_inserted = int(input("Pennies: ")) * pennies

    total_inserted = (
        quarters_inserted + dimes_inserted + nickles_inserted + pennies_inserted
    )
    return enough_money(resources, drink, total_inserted)


get_drink = True

while get_drink:
    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == "report":
        print(resources)
    elif option == "off":
        get_drink = False
    elif option == "espresso" or option == "latte" or option == "cappuccino":
        if check_resources(MENU[option]):
            resources = insert_money(resources, MENU[option])
    else:
        continue
