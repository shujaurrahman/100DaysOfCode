size = input() # What size pizza do you want? S, M, or L
print("Do you want to add pepperoni. Y or N? ")
add_pepperoni = input() # Do you want pepperoni? Y or N
print("Do you want to add Extra cheese. Y or N? ")
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill=0
if size=='S':
    bill=15
  
    if add_pepperoni=='Y':
        bill+=2
if size=='M':
    bill=20
    if add_pepperoni=='Y':
        bill+=3
if size=='L':
    bill=25
    if add_pepperoni=='Y':
        bill+=3
if extra_cheese=='Y':
    bill+=1
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
else:
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
    
    