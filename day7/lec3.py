# check if player has won or not
# step-1
word_list=["shuja","Yusuf","Shadab"]
# step-2
import random
chosen_item=random.choice(word_list)
print(chosen_item)

display=[] #Empty list for _
for _ in chosen_item:
    display+='_'
print(display)
end_of_game=False
while not end_of_game:
    # step-3
    guess=input("Guess a letter: ").lower()

    # step-4
    for position in range(len(chosen_item)):
        #here position tell pos index in list of through range 
        # we can get letter via pos 
        letter=chosen_item[position]
        if letter==guess:
            display[position]=letter
    print(display)

    if '_' not in display:
        end_of_game=True
        print("You win! ")