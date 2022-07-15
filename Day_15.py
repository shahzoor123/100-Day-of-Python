print("Hello i am Coffee making machine")

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

def check_resources(whole_resources, used_resources , coffee_name , money):
    if coffee_name == 'espresso':
        remaining_water = whole_resources['water'] - used_resources[coffee_name]['ingredients']['water']
        remaining_coffee = whole_resources['coffee'] - used_resources[coffee_name]['ingredients']['coffee']
        remaining_milk = whole_resources['milk']
        return print(f"water:{remaining_water}\nMilk:{remaining_milk}\nCoffee:{remaining_coffee}\nMoney:${money}")
    else:
        remaining_water = whole_resources['water'] - used_resources[coffee_name]['ingredients']['water']
        remaining_milk = whole_resources['milk'] - used_resources[coffee_name]['ingredients']['milk']
        remaining_coffee = whole_resources['coffee'] - used_resources[coffee_name]['ingredients']['coffee']
        return print(f"water:{remaining_water}\nMilk:{remaining_milk}\nCoffee:{remaining_coffee}\nMoney:${money}")


check_resources(resources,MENU,"espresso" , 100)


def make_coffee(coffee_name):

    pass


def report():
    money = 100
    return print(f"water:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:${money}")


machine_off = True
while machine_off:
    user_input = input("“What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        machine_off = False
    elif user_input == "report":
        report()
    elif user_input == "espresso":
        pass
    elif user_input == "latter":
        pass
    elif user_input == "cappuccino":
        pass
