
# ===========================================================================================================
from game_data import data
from art import logo
from art import vs
import random

# Break down problem in smaller chunks

def format_data(account):
    """format account data into printable format"""
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name}, a {description} , from {country}"


def check_answer(guess,a_followers,b_followers):
    """if user gets right answer or not """
    if a_followers>b_followers:
        return guess=='a'
    else:
        return guess=='b'
    

# display art
score=0
print(logo)
should_game_continue=True
account_b=random.choice(data)

while should_game_continue:
    # genrate random account form the game data
    account_a=account_b
    account_b=random.choice(data)
    while account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")



    # Ask user to guess
    guess=input("who has more followers? Type 'A' and 'B' : ").lower()


    # check if user is correct
    # #get follower account of each account 
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    ## check if user is correct
    is_correct=check_answer(guess,a_follower_count,b_follower_count)

    # give us a feedback 
    if is_correct:
        score+=1
        print(f"You are right!, current score : {score}.")
    else:
        should_game_continue=False
        print(f"Sorry, that's wrong! final score : {score}.")
    # score keeping 

    # make the game repeatable

    # making the account at position B become next account in position A

