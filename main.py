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

def get_resources(resources_dict):
    '''prints  the ressources that we have in stock'''
    for key, value in resources_dict.items():
        print(f"{key} = {value}")

def get_ingredients(order):
    #print(MENU[order]["ingredients"])
    return MENU[order]["ingredients"]


def get_cost(order):
    return MENU[order]["cost"]*100

def check_resources(needed_resources):
    enough = True
    for key , value in needed_resources.items():
        if resources[key] < value:
            print(f"{key} missing weve about {resources[key] - value}  to less. check report \n"
                  f"or\n"
                  f"use the order 'refill")
            enough = False
    return enough

def use_resources(order):
    needed_resources = get_ingredients(order)
    #print(needed_resources)
    if check_resources(needed_resources):
        for key , value in needed_resources.items():
            resources[key] -= value
            #print(resources[key])

def enough_money(money, order):
    cost=get_cost(order)
    if money >= cost:
        print(f"heres your change {(money-cost)/100}$")
        return True
    else:
        print(f"nice try. not enough money given !!! the price is {cost/100}$, u gave {money/100}$ \n"
              f"you were missin {(cost-money)/100}$ dollars")
        return False

def insert_money():
    money = []
    money_sum=0
    money.append(int(input("give pennys")))
    money.append(int(input("give Dime"))*10)
    money.append(int(input("give Nickels"))*5)
    money.append(int(input("give Quartas"))*25)
    for coin in money:
        money_sum += coin
    #print (round(money_sum, 3))
    return round(money_sum, 3)

is_on = True
while is_on:
    order = input("what u want my friend? latte? espresso? cappuccino?")
    money = 0
    if order == "report":
        get_resources(resources)
    elif order in MENU:
        if check_resources(get_ingredients(order)):
            print(f"price is {get_cost(order)/100}$ please throw in some coins")
            money = insert_money()
            if enough_money(money, order):
                use_resources(order)
            #print(resources)
    elif order == "off":
        is_on = False
    elif order == "refill":
        refil = input("what u want to refill? water, milk, coffee?")
        resources[refil] += 100

    else:
        print(f"we dont serve {order} in here bru")



# TODO: 1 ask Input

# TODO: 2 get report what in inventory when input

# TODO: 2 calculate Money
