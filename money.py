from menu import MENU
from ingredient import Ingredient

class Transaction():
    def __init__(self):
        self.profit = 0
        self.ingredient = Ingredient()
        #self.calculate_amount(user_want= self.insert_coins())


    def insert_coins(self):
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

    def calculate_amount(self,user_want, total):
        if total > MENU[user_want]["cost"]:
            change = total - MENU[user_want]["cost"]
            print(f"The {user_want} cost: ${MENU[user_want]["cost"]}. Your total is : {total}")
            print(f"your change: ${round(change,2)}")
            print(f"Enjoy your {user_want}!")
            self.profit += MENU[user_want]["cost"]
        else:
            print("Not enough money")
            self.ingredient.add_back_ing(user_want)


