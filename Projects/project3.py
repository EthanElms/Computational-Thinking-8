import turtle
import random

#t1 setup
x = 10

class tsetup:
    def __init__(self, x):
        t1 = turtle.Turtle()
        t1.speed(4)
        t1.penup()
        t1.goto(0, -200)
        t1.color("black")
        t1.pendown()
t1 = tsetup(x)
#screen color
#turtle.Screen().bgcolor("white")


#drawing
for x in range(6):
    for x in range(6):
        #t1.forward(100)
        print()


turtle.exitonclick()