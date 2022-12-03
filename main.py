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
    """prints  the resources that we have in stock"""
    for key, value in resources_dict.items():
        print(f"{key} = {value}")


def get_ingredients(order_ing):
    # print(MENU[order]["ingredients"])
    return MENU[order_ing]["ingredients"]


def get_cost(order_cost):
    return MENU[order_cost]["cost"]*100


def check_resources(needed_resources):
    enough = True
    for key, value in needed_resources.items():
        if resources[key] < value:
            print(f"{key} missing we've about {resources[key] - value}  to less.")
            enough = False
    if not enough:
        print(" check report and use the command refill to add some resources")
    return enough


def make_coffee(order_res):
    needed_resources = get_ingredients(order_res)
    # print(needed_resources)
    if check_resources(needed_resources):
        for key, value in needed_resources.items():
            resources[key] -= value
            # print(resources[key])


def enough_money(money_check, order_mon):
    cost = get_cost(order_mon)
    if money_check >= cost:
        print(f"here's your change {(money_check - cost) / 100}$")
        return True
    else:
        print(f"nice try. not enough money given !!! the price is {cost/100}$, u gave {money_check / 100}$ \n"
              f"you were missin {(cost - money_check) / 100}$ dollars")
        return False


def insert_money():
    """Returns the inserted money in cent"""
    coins_list = []
    money_sum = 0
    coins_list.append(int(input("give penny's ")))
    coins_list.append(int(input("give Dime ")) * 10)
    coins_list.append(int(input("give Nickels ")) * 5)
    coins_list.append(int(input("give Quartas ")) * 25)
    for coin in coins_list:
        money_sum += coin
    # print (round(money_sum, 3))
    return round(money_sum, 3)

resources["Coins"] = 0
is_on = True
while is_on:
    order = input("what u want my friend? latte? espresso? cappuccino?\n")
    money = 0
    if order == "report":
        get_resources(resources)
    elif order in MENU:
        if check_resources(get_ingredients(order)):
            print(f"price is {get_cost(order)/100}$ please throw in some coins")
            money = insert_money()
            resources["Coins"] += money
            if enough_money(resources["Coins"] , order):
                make_coffee(order)
                resources["Coins"] = 0
                print(f"hmm heres you freshly pressed {order} ☕ 🥵")
            # print(resources)
    elif order == "off":
        is_on = False
    elif order == "refill":
        refil = input("what u want to refill? water, milk, coffee?")
        resources[refil] += 100

    else:
        print(f"we dont serve {order} in here bru")
