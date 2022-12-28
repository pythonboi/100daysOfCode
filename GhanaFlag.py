from turtle import Turtle

from turtle import Screen

sc = Screen()

tt = Turtle()

tt.pensize(2)
tt.hideturtle()

tt.speed(10)

lines = [-100, 15, 100, 30]

line = 360

tt.penup()


# Draw Square

def penDown():
    tt.pendown()
    # tt.forward(100)
    tt.forward(450)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    tt.forward(450)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    # tt.right(line / 4)
    # tt.forward(70)


print(tt.pos())
print(tt.xcor())
print(tt.ycor())

tt.color("red")

tt.goto(-200, 250)


def red():
    penDown()


tt.begin_fill()
red()
print(tt.position())
print(round(tt.xcor(), 5))
print(round(tt.ycor()))

tt.end_fill()

print("Printing the headings")
print(tt.heading())

print("Drawing Yellow now")
tt.color("yellow")

tt.penup()

tt.goto(-200, 50)


def yellow():
    penDown()


tt.begin_fill()
yellow()
tt.end_fill()
print(tt.ycor())

tt.color("green")

print("getting the heading of Green")
print(tt.heading())


def green():
    tt.penup()
    tt.goto(-200, -150)
    penDown()
    tt.penup()


tt.begin_fill()
green()
tt.end_fill()
print(tt.position())

tt.goto(-80, -25)

tt.color("black")
tt.begin_fill()


def star():
    tt.penup()
    for drawStar in range(5):
        tt.pendown()
        tt.forward(210)
        tt.right(144)


star()
tt.end_fill()

# def moveForward():
#     tt.penup()
#     tt.goto(-100, 80)
#     tt.pendown()
#     tt.forward(300)
#     tt.right(90)
#     tt.forward(200)
#     tt.right(90)
#     tt.forward(300)
#     tt.right(90)
#     tt.forward(200)
#
#
# moveForward()
#
# tt.color("#ff0000")
# tt.begin_fill()
#
#
# def drawMiddle():
#     tt.penup()
#     tt.goto(-100, 15)
#     tt.right(90)
#     tt.pendown()
#     tt.forward(300)
#
#
# drawMiddle()
# tt.end_fill()
#
# tt.color("#ffff00")
#
#
# def drawMiddlen():
#     tt.penup()
#     tt.goto(-100, -55)
#     # tt.right(90)
#     tt.pendown()
#     tt.forward(300)
#
#
# tt.begin_fill()
# drawMiddlen()
# tt.end_fill()
#
# tt.penup()
# tt.goto(20, -10)
#
# tt.color("black")
# tt.begin_fill()
#
#
# def star():
#     for drawStar in range(5):
#         tt.pendown()
#         tt.forward(75)
#         tt.right(144)
#
#
# star()
# tt.end_fill()
#
sc.exitonclick()
