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

used = {
    "water": 100,
    "milk": 100,
    "coffee": 50,
}

def process_coin(coffee_name):
    coffee_cost = MENU[coffee_name]['cost']
    print(f"${coffee_cost}")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies: "))
    total = round(q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01 , 2)
    if total > coffee_cost:
        change = round(total - coffee_cost , 2)
        print(f"Here is your change ${change}")
        print(f"${total}")
    else:
        print("You didn't have the money to buy a coffee")
    return total
process_coin('espresso')