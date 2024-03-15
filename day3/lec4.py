# Leap year problem in python
# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# for a number to be leap year it has 3 condtion and all are else-if form 4-100-400
# 1. year/4 yes-> leap year no-> not a leap year
# 2. if year/4 ->yes then two check year/100 yes-> leap year and check by 400 no->then also year year
# 3. if year/100 is yes then year/400 yes-> leap year no-> not a leap year

# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not leap year")

if year%4==0 and year%100!=0 and year%400==0:
    print("Leap year")
else:
    print("Not leap year")