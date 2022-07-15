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
    },
    "start": {
        "ingredients": {
            "water": 0,
            "milk": 0,
            "coffee": 0,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(whole_resources, used_resources, coffee_name, money):

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


def process_coin(coffee_name):
    coffee_cost = MENU[coffee_name]['cost']
    print(f"The coffee costs ${coffee_cost}")
    print("Please insert the coins")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies: "))
    total = round(q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01, 2)
    if total > coffee_cost:
        change = round(total - coffee_cost, 2)
        print(f"The total amount you gave was ${total} Here is your change ${change}")
        print(f"And here is your {coffee_name} coffee ☕ Enjoy")
    else:
        print("You didn't have the sufficient money to buy a coffee")
    return total


profit = 0
machine_off = True
while machine_off:
    user_input = input("“What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        machine_off = False
    elif user_input == "report":
        print(f"water {resources['water']}ml")
        print(f"milk {resources['milk']}ml")
        print(f"coffee {resources['coffee']}g")
        print(f"money ${profit}")
    else:
        drink = MENU[user_input]
        print(drink)
        process_coin(user_input)

