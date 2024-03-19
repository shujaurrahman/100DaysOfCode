# Hangman 
# what we have done till now 
# created a list with bunch of words in it
# get random word fromt the list 
# take input form user 
# check if it matchs the input letter with chosen word 

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