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

tl.color("red")


def crescent():
    tl.penup()
    tl.goto(90, -35)
    tl.pendown()
    tl.begin_fill()
    for i in range(1, 1 + 1, 1):

        tl.circle(90 * i)

        tl.end_fill()

        for m in range(1, 1 + 1, 1):
            tl.color("white")
            # tl.begin_fill()
            tl.circle(70 * i)
            # tl.end_fill()


crescent()

sc.exitonclick()
