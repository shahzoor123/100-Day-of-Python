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
x = resources['water'] - 100

#print(MENU['espresso']['ingredients'])
#print(MENU['espresso']['cost'])

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


