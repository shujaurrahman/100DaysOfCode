# Nested if else 
# Paying for rollercoster where conditions are more than one

height=int(input("What is your height in cm ?"))

if height>=120:
    print("You can ride ! Pay tickets fee..")
    age=int(input("What is your age?"))
    if age<=12:
        print("Please pay 50 Rupees..")
    elif age>12 and age<18:
        print("Please pay 60 Rupees..")
    else:
        print("Please pay 70 Rupees..")
else:
    print("Sorry, You have to grow taller before you can ride.")