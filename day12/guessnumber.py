import random
import art
print(art.logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
choice=input("choose a difficulty. Type 'easy' or 'hard' : ").lower()

hardLife=5
easyLife=10
number=random.randint(1,100)
def hardLifeRemmaining():
    global hardLife
    print(f"Life remaining: {hardLife}")
def easyLifeRemmaining():
    global easyLife
    print(f"Life remaining: {easyLife}")
def hard():
    """user chose hard"""
    global hardLife,number
    while hardLife>0:
        print(f"You have {hardLife} attempt remaining to guess the number.")
        guess=int(input("Guess a number: "))
        if number>guess:
            print("Too low")
            hardLife-=1
            hardLifeRemmaining()
        elif number<guess:
            print("Too high")
            hardLife-=1
            hardLifeRemmaining()
        elif(number==guess and hardLife>0):
            hardLifeRemmaining()
            print(f"You gussed right, number is  {number}")
            break
        else:
            print("Error no condition aligned")
    if (number!=guess):
        print(f"You lost, number was {number}")
 

def easy():
    """User chose easy"""
    global easyLife,number
    while easyLife>0:
        print(f"You have {easyLife} attempt remaining to guess the number.")
        guess=int(input("Guess a number: "))
        if number>guess:
            print("Too low")
            easyLife-=1
            easyLifeRemmaining()
        elif number<guess:
            print("Too high")
            easyLife-=1
            easyLifeRemmaining()
        elif(number==guess and easyLife>0):
            easyLifeRemmaining()
            print(f"You gussed right, number is  {number}")
            break
        else:
            print("Error no condition aligned ")
    if (number!=guess):
        print(f"You lost, number was {number}")

    


if choice=='easy':
    easy()
elif choice=='hard':
    hard()
else:
    print("Wrong choice!")