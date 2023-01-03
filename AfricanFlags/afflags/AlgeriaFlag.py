from turtle import Turtle
from turtle import Screen

tl = Turtle()

sc = Screen()

tl.penup()
tl.pensize(2)
tl.speed(8)
#tl.hideturtle()


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


tl.color("green")


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
        tl.circle(108 * i)

        tl.end_fill()

        # This is the inner circle
        for m in range(1, 1 + 1, 1):
            tl.color("white")
            tl.begin_fill()
            tl.circle(77 * i)
            tl.end_fill()

            # Before the half circle

            tl.penup()
            print(tl.position())
            tl.goto(0, -110)
            tl.left(90)
            tl.color("green")
            tl.begin_fill()

            # Creating the half circle
            for w in range(180):
                tl.pendown()

                tl.forward(1.3)
                tl.right(1)
            tl.right(90)
            tl.forward(115)
            tl.end_fill()
            tl.penup()


crescent()

# tl.goto(-0, 35)
#
# tl.penup()
#
# tl.color("green")
#
#
# def straight():
#     tl.left(90)
#     tl.forward(40)
#     tl.left(90)
#     tl.forward(150)
#     tl.left(90)
#     tl.forward(40)
#
#
# tl.begin_fill()
# straight()
# tl.end_fill()

print(tl.position())

tl.goto(60, -10)
tl.color("red")


def star():
    tl.begin_fill()
    tl.penup()
    tl.right(15)
    for mn in range(5):

        tl.pendown()

        tl.forward(80)
        tl.right(145)


star()
tl.end_fill()

tl.penup()

print(tl.pos())

tl.goto(90, 50)

tl.color("pink")

tl.begin_fill()
tl.circle(80)
tl.end_fill()


# tl.goto(140, -180)
#
# tl.left(90)
#
# for x in range(180):
#     tl.color("blue")
#     tl.begin_fill()
#     tl.forward(1)
#     tl.right(1)
#
#
# tl.right(90)
# tl.forward(115)
# tl.end_fill()

sc.exitonclick()
