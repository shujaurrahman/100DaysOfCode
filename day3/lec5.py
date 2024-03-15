# Multiple if statement 
# take picture in case of rollercoster 

height=int(input("What is your height in cm ?"))
bill=0
if height>=120:
    print("You can ride ! Pay tickets fee..")
    age=int(input("What is your age?"))
    if age<=12:
        bill=50
        print(f"Please pay {bill} Rupees..")
    elif age>12 and age<18:
        bill=60
        print(f"Please pay {bill} Rupees..")
    else:
        bill=70
        print(f"Please pay {bill} Rupees..")
    want_photo=input("Do you want a photo taken? Y or N.")
    if want_photo=='Y':
        bill+=3
    print(f"Your Bill is {bill}")
    
else:
    print("Sorry, You have to grow taller before you can ride.")