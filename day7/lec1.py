word_list=["shuja","Yusuf","Shadab"]
import random
chosen_item=random.choice(word_list)
print(chosen_item)
guess=input("Guess a letter: ").lower()
for letter in chosen_item:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")