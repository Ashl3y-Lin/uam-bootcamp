from menu import MENU, resources

PROFIT = 0
def insert_coins():
    user_quartre = int(input("quarter: "))
    quarter = 0.25 * user_quartre
    user_dime = int(input("dime: "))
    dime = 0.10 * user_dime
    user_nickel = int(input("nickel: "))
    nickel = 0.05 * user_nickel
    user_penny = int(input("penny: "))
    penny = 0.01 * user_penny
    total_added = quarter + dime + nickel + penny
    total = round(total_added, 2)
    return total

def calculate_amount(user_want):
    total = insert_coins()
    if total > MENU[user_want]["cost"]:
        change = total -MENU[user_want]["cost"]
        print(f"The {user_want} cost :{MENU[user_want]["cost"]}. Your total is : {total}")
        print(f"your change: {change}")
        print(f"Enjoy your {user_want}!")
        global PROFIT
        PROFIT += MENU[user_want]["cost"]
        return True
    else:
        print("Not enough money")
        add_back_ing(user_want)
        return False

def add_back_ing(user_want):
    if user_want == "report":
        pass
    elif user_want == "latte" or "cappuccino" or "espresso":
        for ingredient in MENU[user_want]["ingredients"]:
                substracted_ing = resources[ingredient] + MENU[user_want]["ingredients"][ingredient]
                resources[ingredient] = substracted_ing

def report_ingredient(user_want):
    if user_want == "report":
        pass
    elif user_want == "latte" or "cappuccino" or "espresso":
        for ingredient in MENU[user_want]["ingredients"]:
            if resources[ingredient] >= MENU[user_want]["ingredients"][ingredient]:
                substracted_ing = resources[ingredient] - MENU[user_want]["ingredients"][ingredient]
                resources[ingredient] = substracted_ing
            else:
                print(f"not enough {ingredient}")
                return False
        return True



playing = True

while playing:

    user_want = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if  user_want == "report":
        print(resources)
        print(f"profit : {PROFIT}")
    elif user_want == "off":
        playing = False
    elif report_ingredient(user_want):
            calculate_amount(user_want)
