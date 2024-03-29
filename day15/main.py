from day16.data import MENU
from day16.data import resources
from art import logo
profit=0
# print report
# check resource sufficient?
def is_resource_sufficient(order_ingredients):
    """Return ture when order can be made ,False if ingredients are insufficients..."""
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# process coins
def process_coint():
    """returns total calculated from coins inserted"""
    print("Please insert the coins -")
    total=int(input("how many quaters? : "))*0.25
    total+=int(input("how many dimes? : "))*0.1
    total+=int(input("how many nikkels? : "))*0.05
    total+=int(input("how many penny? : "))*0.01
    return total

# check transaction successful?
def is_transaction_successfull(money_recieved,drinkcost):
    """Returns True when payment is accepted else false"""
    if money_recieved>drinkcost:
        change=round(money_recieved-drinkcost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=money_recieved
        return True
    else:
        print(f"Sorry that not enough money. Money refunded.")
        return False

# make coffee  and update resources 
def make_coffee(drink_name, order_ingredients):
    """deduct the ingredients from resources and make coffee"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy")


is_on=True

while is_on:
    print(logo)
    choice=input("what would you like to have? (espresso/latte/cappuccino) ? : ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water: {resources["water"]}ml.")
        print(f"milk: {resources["milk"]}ml.")
        print(f"coffee: {resources["coffee"]}g.")
        print(f"Money: ${round(profit,2)}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coint()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])