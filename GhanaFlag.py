import turtle

from turtle import Turtle

from turtle import Screen

sc = Screen()

# t = turtle.Turtle()

tt = Turtle()


def moveForward():
    pass


tt.pensize(2)

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

tt.penup()

sc.exitonclick()
