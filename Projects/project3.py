import turtle
import random

#t1 setup
t = 0

class tsetup:
    # I hate python classes are so scuffed and the construct litterly take the class as an augment never seen any other language do this smh :(
    # I used a class for fun its not optimal
    def __init__(self,color,lr):
        #setup
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(0, -175)
        t.color(color)
        t.pendown()
        for x in range(10):
            t.setheading(90)

            if (lr==0):
                t.left(10*x)
            elif(lr==2):
                t.right(10*(x+10))
            else:
                t.right(10*x)

            t.penup()
            t.goto(0, -200)
            t.pendown()
            t.hideturtle()
            for x in range(10):
                t.forward(25)
                t.left(10)
                t2=t.clone()
                for x in range(5):
                    t2.right(10)
                    t2.forward(25)
                    t2.hideturtle()
                
#screen color
turtle.Screen().bgcolor("black")


#drawing
tsetup("red",0)
tsetup("orange",1)
tsetup("yellow",2)
    
    

turtle.exitonclick()