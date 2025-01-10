import turtle
import random


t1 = turtle.Turtle()
t1.speed(0)
t1.penup()
t1.goto(0, 0)
t1.color("red")
t1.pendown()

t2 = turtle.Turtle()
t2.speed(0)
t2.penup()
t2.goto(0, 0)
t2.color("white")
t2.right(20)
t2.pendown()

turtle.Screen().bgcolor("black")

while(True):
    t1angle = random.randrange(10,60)
    t2angle = random.randrange(10,60)

    t1distance = random.randrange(10,60)
    t2distance = random.randrange(10,60)

    t1dir = random.randrange(1,2)
    t2dir = random.randrange(1,2)
    t1.pendown()
    
    if(t1dir==1):
        t1.right(t1angle)
    else:
        t1.left(t1angle)
    t1.forward(t1distance)

    t2.pendown()
    if(t2dir==1):
        t2.right(t2angle)
    else:
        t2.left(t2angle)
    t2.forward(t2distance)
    

turtle.exitonclick()