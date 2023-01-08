from turtle import Turtle
from turtle import Screen

ng = Turtle()
sn = Screen()

sn.bgcolor("black")


ng.speed(10)
ng.hideturtle()


def drawRec():

    ng.pendown()
    ng.forward(600)
    ng.right(90)
    ng.forward(200)
    ng.right(90)
    ng.forward(600)
    ng.right(90)
    ng.forward(200)
    ng.penup()


drawRec()


def orange():
    ng.color("orange")
    ng.penup()
    ng.goto(-300, 300)
    ng.right(90)
    drawRec()


ng.begin_fill()
orange()
ng.end_fill()


def white():
    ng.color("white")
    ng.goto(-300, 100)

    ng.right(90)
    drawRec()


ng.begin_fill()
white()
ng.end_fill()


def green():
    ng.color("green")
    ng.goto(-300, -100)

    ng.right(90)
    drawRec()


ng.begin_fill()
green()
ng.end_fill()


def circle():
    ng.color("orange")
    ng.begin_fill()
    ng.goto(90, 0)
    ng.circle(85)


circle()
ng.end_fill()


sn.exitonclick()
