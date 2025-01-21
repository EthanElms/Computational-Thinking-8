import turtle
import time
import random

winturtle = input("which turtle will win 1,2,3,4 \n")
winturtle = int(winturtle)
bet = input("how much do you bet ")

# Section 1 - Variables
x1 = -300
y1 = 200
x2 = -300
y2 = 100
x3 = -300
y3 = 0
x4 = -300
y4 = -100

# Section 2 - Setup
t1 = turtle.Turtle()
t1.penup()
t1.goto(x1, y1)
t2 = turtle.Turtle()
t2.penup()
t2.goto(x2, y2)
t3 = turtle.Turtle()
t3.penup()
t3.goto(x3, y3)
t4 = turtle.Turtle()
t4.penup()
t4.goto(x4, y4)

t1.pendown()
t2.pendown()
t3.pendown()
t4.pendown()

t1.color("black")
t2.color("red")
t3.color("green")
t4.color("blue")


# Section 3 -
for i in range(65):
    x1 += random.randint(1, 15)
    x2 += random.randint(1, 15)
    x3 += random.randint(1, 15)
    x4 += random.randint(1, 15)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)
    time.sleep(0.01)

winner = 0

# Section 4 -
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    winner = 1
    print("1 wins\n")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    winner = 2
    print("2 wins\n")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    winner = 3
    print("3 wins\n")
elif x4 >= x1 and x4 >= x3 and x4 >= x2:
    winner = 4
    print("4 wins\n")

if (winturtle == winner):
    print("\nyou picked winner")
    print(f'you win {bet}')
else:
    print("\nyou lose life savings")
    print(f'you lose {bet}')

turtle.exitonclick()
