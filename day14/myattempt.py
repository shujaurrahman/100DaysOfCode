
# from game_data import data
# from art import logo
# from art import vs
# import random

# # data contains a list of people and people are in form dictionary i.e every list element is in key
# #  and value keys are same for every element of list the value of key changes for every person
# Score=0
# # getting random person
# def randomPersonality():
#     index=random.randint(0,len(data))
#     return data[index]

# # debug
# p=randomPersonality()
# # print(data[0])
# def printPersonality(dic):
#     name=dic["name"]
#     description=dic["description"]
#     country=dic["country"]
#     return f"{name}, a {description} , from {country}"

# # x=printPersonality(p)
# # print(x)

# def compare(a,b):
#     a_followers=a["follower_count"]
#     b_followers=b["follower_count"]
#     if a_followers>b_followers:
#         return printPersonality(a)
#     else:
#         return printPersonality(b)
    

# a=0
# b=0
# # def new_personaloty(a,b,flag):
# def newVs():
#     global a,b
#     a=randomPersonality()
#     b=randomPersonality()
    
# def game():
#     global Score,a,b
#     is_game_over=False
#     newVs()
#     while(not is_game_over):
#         print(logo)
#         print(f"Compare A: {printPersonality(a)}")
#         print(vs)
#         print(f"Compare B: {printPersonality(b)}")
#         choice=input("who has more followers? Type 'A' and 'B' : ").lower()
#         if choice=='a':
#             if compare(a,b)==a:
#                 Score+=1
#                 print(f"You're right! Current score: {Score}")
#                 print(f"a:{a},b:{b}")
#                 a=b
#                 b=randomPersonality()
#             else:
#                 print(f"Sorry that's wrong. final score: {Score}")
#                 print(f"a:{a},b:{b}")
#                 newVs()
#         elif choice=='b':
#             if compare(a,b)==b:
#                 Score+=1
#                 print(f"You're right! Current score: {Score}")
#                 print(f"a:{a},b:{b}")
#                 b=a
#                 a=randomPersonality()
#             else:
#                 print(f"Sorry that's wrong. final score: {Score}")
#                 print(f"a:{a},b:{b}")
#                 newVs()
#         else:
#             print("Invalid Input.")
#         if(Score==20):
#             is_game_over=True
#     print("Game Over!! ")

# game()
