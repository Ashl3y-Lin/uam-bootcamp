import ingredient
from money import Transaction
from ingredient import Ingredient
from ui import Ui

transaction = Transaction()
resources = Ingredient()
playing = True

while playing:

    user_want = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if  user_want == "report":
        print(ingredient.resources)
        print(f"profit : {transaction.profit}")
    elif user_want == "off":
        playing = False
    elif resources.report_ingredient(user_want):
        transaction.calculate_amount(user_want, transaction.insert_coins())

