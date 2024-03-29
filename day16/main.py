from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from data import MENU

# print report 
# check resourses are suffient or not 
# process coins 
# check if transaction sucessful 
# Make Coffee 

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()
is_one=True
while is_one:
    options=menu.get_items()
    choice=input(f"what would you like ? {options} :")
    if choice=="off":
        is_one=False
    elif choice=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
