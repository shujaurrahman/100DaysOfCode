import turtle
import pandas
screen=turtle.Screen()
screen.title(" US State Game.")
image="day25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv("day25/day-25-us-states-game-start/50_states.csv")
all_states=data.state.to_list()
# print(all_states)

gussed_state=[]

while len(gussed_state)<50:
    answer_state=screen.textinput(title=f"{len(gussed_state)}/50 states correct ",prompt="what's another state's name?").title()

    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in gussed_state:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("day25/day-25-us-states-game-start/states_to_learn.csv")
        break

    if answer_state in all_states:
        gussed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(state_data.state.item())
    
# turtle.mainloop()
screen.exitonclick()
