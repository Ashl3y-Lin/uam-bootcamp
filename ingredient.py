from menu import MENU, resources

class Ingredient:
    def __init__(self):
        self.menu = MENU
        self.resources = resources

    def report_ingredient(self,user_want):
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

    def add_back_ing(self, user_want):
        if user_want == "report":
            pass
        elif user_want == "latte" or "cappuccino" or "espresso":
            for ingredient in MENU[user_want]["ingredients"]:
                substracted_ing = resources[ingredient] + MENU[user_want]["ingredients"][ingredient]
                resources[ingredient] = substracted_ing



    "def add_ash()"
