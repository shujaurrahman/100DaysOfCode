from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)

is_race_on=False

user_bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race ? Enter the color: ")
print(user_bet)
# create a list of colors for turtle

colors=["red","orange","yellow","green","blue","purple"]

# tim.shape("turtle") we can user construction at instance of the object to give shape to the turtle 
y_pos=[-60,-20,20,60,100,140]
if user_bet:
    is_race_on=True

all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_pos[turtle_index])
    all_turtle.append(new_turtle)

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()











# tim2=Turtle(shape="turtle")
# tim2.penup()
# tim2.goto(x=-230,y=-60)


# tim3=Turtle(shape="turtle")
# tim3.penup()
# tim3.goto(x=-230,y=-20)

# tim4=Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(x=-230,y=20)

# tim4=Turtle(shape="turtle")
# tim4.penup()
# tim4.goto(x=-230,y=60)

# tim5=Turtle(shape="turtle")
# tim5.penup()
# tim5.goto(x=-230,y=100)

# tim6=Turtle(shape="turtle")
# tim6.penup()
# tim6.goto(x=-230,y=140)