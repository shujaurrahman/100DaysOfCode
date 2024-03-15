print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names=name1+name2
combined_names=combined_names.lower()
t=combined_names.count('t')
r=combined_names.count('r')
u=combined_names.count('u')
e=combined_names.count('e')
first_digit=t+r+u+e
l=combined_names.count('l')
o=combined_names.count('o')
v=combined_names.count('v')
e=combined_names.count('e')
second_digit=l+o+v+e
love_score=str(first_digit)+str(second_digit)
love_score=int(love_score)
if love_score<10 or love_score>90:
    print(f"Your score is {love_score}, you go together like code and mentos.")
elif love_score>=40 and love_score<=50:
    print(f"Your score is {love_score},you are alright together.")
else:
    print(f"Your score is {love_score}")