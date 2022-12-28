import turtle

from turtle import Turtle

from turtle import Screen

sc = Screen()

# t = turtle.Turtle()

tt = Turtle()

tt.pensize(2)
tt.hideturtle()

lines = [-100, 15, 100, 30]


def moveForward():
    tt.penup()
    tt.goto(-100, 80)
    tt.pendown()
    tt.forward(300)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    tt.forward(300)
    tt.right(90)
    tt.forward(200)


moveForward()


def drawMiddle():
    tt.penup()
    tt.goto(-100, 15)
    tt.right(90)
    tt.pendown()
    tt.forward(300)


drawMiddle()


def drawMiddlen():
    tt.penup()
    tt.goto(-100, -55)
    # tt.right(90)
    tt.pendown()
    tt.forward(300)


drawMiddlen()

tt.penup()
tt.goto(20, -10)


def star():
    tt.fillcolor("black")
    tt.begin_fill()
    for drawStar in range(5):
        tt.pendown()
        tt.forward(75)
        tt.right(144)


tt.end_fill()

star()

sc.exitonclick()
