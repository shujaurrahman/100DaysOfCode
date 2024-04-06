from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    
    def move(self):
        '''Moves the ball by 10 distance both x and y '''
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        '''bounces back the wall if touches up or down'''
        self.y_move*=-1

    def bounce_x(self):
        '''bounces if it collides with paddle '''
        self.x_move*=-1
        self.move_speed*=0.9

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()