user_cards = []
computer_cards = []
is_game_over=False

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards} , Current score: {user_score}")
    print(f"Computers first card: {computer_cards[0]}")

    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Type 'y' to get another card, type 'n' to pass : ").lower()
        if user_should_deal=='y':
            user_cards.append(deal_cards())
        else:
            is_game_over=True