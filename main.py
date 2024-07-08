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

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def is_resources_sufficient(order):
    for item in order:
        if resources[item] > order[item]:
            return True
        else:
            print(f"sorry, there are not enough {item}")
            return False



def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry, not enough money entered, money returned")


def make_coffee(order_ingredient, drink_name):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]

    print(f"enjoy your {drink_name}")    








is_machine_on =True

while is_machine_on:
    choice =input("enter off to make machine to be off, resources for show current resources, coffee name for order coffee ").lower()
    if choice =="off":
        is_machine_on =False
    elif choice == "resources":
        print(f"current resources are: {resources}")
        print(f"profit : {profit}")    
    else:
        if is_resources_sufficient(MENU[choice]["ingredients"]):
            payment =process_coins()

            if transaction_successful(payment, MENU[choice]["cost"]):
                make_coffee(MENU[choice]["ingredients"], choice)

