# robot assignment 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moverob():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
for i in range(1,7):
    moverob()
