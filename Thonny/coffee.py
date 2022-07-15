print("Coffee making machine")
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# print(MENU['espresso']['ingredients'])


def which_coffee(coffee_name):
    pass


def report():
    return resources


machine_off = False
while machine_off:
    user_input = input("“What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        machine_off = True
    elif user_input == "report":
        print(report())
    elif user_input == "espresso":
        pass
    elif user_input == "latter":
        pass
    elif user_input == "cappuccino":
        pass
