from menu_of_coffee import menu
from resources_list import resources
earnings = 0

profit = 0


def check_if_enough_resources(drink_ingredients):
    """Check to see if the machine has enough ingredients for the coffee"""
    for drink_ingredient_key in drink_ingredients:
        if resources[drink_ingredient_key] < drink_ingredients[drink_ingredient_key]:
            print(f"Sorry there is not enough: {drink_ingredient_key}")
            return False
    return True


def report():
    """Return information on resources"""
    for key in resources:
        print(f"{key}: {resources[key]}")

    global profit
    print(f"money: ${profit}")
    return


def update_resources(money_given, drink_ingredients):
    for drink_ingredient_key in drink_ingredients:
        resources[drink_ingredient_key] -=  drink_ingredients[drink_ingredient_key]

    global profit
    profit += money_given


def transaction_checker(cost):
    """"Insert number of coins and return bool"""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    coins_inserted = quarters + dimes + nickles + pennies

    if coins_inserted < cost:
        print("Not enough money has been input. Returning coins.")
        return False
    if coins_inserted > cost:
        change = round(coins_inserted - cost, 2)
        print(f"Returning your change of ${change}")
    return True


def get_coffee():
    machine_on = True
    while machine_on:
        requested_drink_key = input("“What would you like? (espresso/latte/cappuccino): ")
        if requested_drink_key == 'off':
            machine_on = False
        elif requested_drink_key == 'report':
            report()
        else:
            requested_drink = menu[requested_drink_key]

            if check_if_enough_resources(requested_drink['ingredients']):
                cost = requested_drink['cost']
                print(f"{requested_drink_key} costs ${cost}")
                if transaction_checker(cost):
                    update_resources(cost, requested_drink['ingredients'])
                    print(f"Here is your {requested_drink_key}. Enjoy")


get_coffee()
