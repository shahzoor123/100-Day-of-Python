from mod.coffee.menu import Menu, MenuItem
from mod.coffee.coffee_maker import CoffeeMaker
from mod.coffee.money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

game_loop = True
while game_loop:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    if user_input == 'off':
        game_loop = False
    elif user_input == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
