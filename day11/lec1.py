
import random
def deal_cards():
    """Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]    
    card=random.choice(cards)
    return card

def calculate_score(cards):
    """takes a list of score and return score of the card"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "its a draw :-) "
    elif computer_score==0:
        return "Loose,Opponent has a blackjack!"
    elif user_score==0:
        return "You won with a blackjack!"
    elif user_score>21:
        return "You went over, you loose."
    elif computer_score>21:
        return "Opponent went over. you win!"
    elif user_score>computer_score:
        return "you win"
    else:
        return "you loose"
