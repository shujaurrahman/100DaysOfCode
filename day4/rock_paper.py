rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("what do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. ")
list=[rock,paper,scissors]
comp_list=["rock","paper","scissors"]
end=len(comp_list)
comp_choice=random.randint(0,end-1)
user_choice=int(input())
print("Your choice: ")
print(list[user_choice])
print("Computer Choice: ")
print(list[comp_choice])
if user_choice==0 and comp_choice==1:
    print("You Lost.")
elif user_choice==0 and comp_choice==2:
    print("You won!")
elif user_choice==1 and comp_choice==0:
    print("You won!")
elif user_choice==1 and comp_choice==2:
    print("You Lost.")
elif user_choice==2 and comp_choice==0:
    print("You Lost")
elif user_choice==2 and comp_choice==1:
    print("You won!")
elif user_choice==comp_choice:
    print("Its a Tie!")
else:
    print("Error! Enter Valid choice..!")