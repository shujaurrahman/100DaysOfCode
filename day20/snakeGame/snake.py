from turtle import Turtle,Screen
POSITIONS=[0,-20,-40]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]

    def createSnake(self):
        for square in range(0,3):
            new_Square=Turtle("square")
            new_Square.color("white")
            new_Square.penup()
            new_Square.goto(x=POSITIONS[square],y=0)
            self.segments.append(new_Square)
    
    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x=self.segments[seg_num-1].xcor()
                new_y=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(20)
            

    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
         
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
         