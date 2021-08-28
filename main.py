from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


def get_coffee():
    menu_obj = Menu()
    coffee_machine = CoffeeMaker()
    money_machine_obj = MoneyMachine()
    machine_on = True
    while machine_on:
        requested_drink_key = input(f"“What would you like? {menu_obj.get_items()}: ")
        if requested_drink_key == 'off':
            machine_on = False
        elif requested_drink_key == 'report':
            coffee_machine.report()
            money_machine_obj.report()
        else:
            requested_drink = menu_obj.find_drink(requested_drink_key)

            if coffee_machine.is_resource_sufficient(requested_drink):
                successful_payment = money_machine_obj.make_payment(requested_drink.cost)
                if successful_payment:
                    coffee_machine.make_coffee(requested_drink)




get_coffee()