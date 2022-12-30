from turtle import Turtle
from turtle import Screen

tl = Turtle()

sc = Screen()

tl.penup()
tl.pensize(2)
tl.speed(8)

full = 360


# Draw the square flag shape

def square():
    tl.goto(-300, 150)
    tl.pendown()
    tl.forward(300)
    tl.right(90)
    tl.forward(350)
    tl.right(90)
    tl.forward(300)
    tl.right(90)
    tl.forward(350)


# square()

tl.color("#004d00")


def dkgreen():
    square()


tl.begin_fill()
dkgreen()
tl.end_fill()

tl.color("#ff0000")


def crescent():
    tl.penup()
    tl.goto(90, -35)
    tl.pendown()
    tl.circle(90)


crescent()

sc.exitonclick()
