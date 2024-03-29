from moduleex import anExample
print(anExample)
# as in this example with use of . we have used the variable declared in the module moduleex
# similar by . operator we can use class of an module by firstly importing the module then accessing the class 
# of the imported module and then using it with the help of . operator.

# import turtle

# shuja=turtle.Turtle()


# her shuja is an object of class Turtle . operator is used to access class from module turtle 
# which we have imported earlier

# to use more effiently and reglect redundancy 

# we can import full class 

from turtle import Turtle,Screen

timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("purple")
timmy.forward(100)


myScreen=Screen()
print(myScreen.canvheight) 
myScreen.exitonclick() 
# open a screen and exit on click with use of method exitonclick()
 