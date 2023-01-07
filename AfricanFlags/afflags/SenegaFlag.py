from turtle import Turtle
from turtle import Screen

sc = Screen()
tt = Turtle()

sc.bgcolor("black")

tt.penup()
tt.hideturtle()


def square():
    tt.pendown()

    tt.right(180)
    tt.forward(500)
    tt.left(90)
    tt.forward(250)
    tt.left(90)
    tt.forward(500)
    tt.left(90)
    tt.forward(250)


square()


def green():
    tt.penup()
    tt.color("green")
    tt.goto(-400, 250)
    square()


tt.begin_fill()
green()
tt.end_fill()


def yellow():
    tt.color("yellow")
    tt.penup()
    tt.right(90)
    tt.goto(-150, 250)
    square()


tt.begin_fill()
yellow()
tt.end_fill()


def red():
    tt.color("red")
    tt.penup()
    tt.right(90)
    tt.goto(100, 250)
    square()


tt.begin_fill()
red()
tt.end_fill()


def star():
    tt.color("green")
    tt.penup()
    tt.goto(15, -50)
    tt.right(35)
    for n in range(5):
        tt.forward(135)
        tt.right(144)


tt.begin_fill()
star()
tt.end_fill()


sc.exitonclick()
