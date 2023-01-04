from turtle import Turtle
from turtle import Screen

tl = Turtle()

sc = Screen()

sc.bgcolor("black")

tl.penup()
tl.pensize(2)
tl.speed(10)


# tl.hideturtle()


# Draw the square flag shape

def square():

    tl.pendown()
    tl.forward(300)
    tl.right(90)
    tl.forward(350)
    tl.right(90)
    tl.forward(300)
    tl.right(90)
    tl.forward(350)
    tl.right(90)


# tl.color("green")
tl.color("#008040")


def dkgreen():
    tl.goto(-300, 150)
    square()


tl.begin_fill()
dkgreen()
tl.end_fill()

print(tl.position())
print("This is after printing the green square ")

# Creating the white square
tl.penup()
tl.goto(0, 150)


def whiteSquare():
    tl.color("white")

    square()


tl.begin_fill()
whiteSquare()
tl.end_fill()

tl.color("red")


def crescent():
    tl.penup()
    # tl.goto(90, -35)
    tl.left(90)
    tl.goto(95, -35)
    tl.pendown()
    tl.begin_fill()
    for i in range(1, 1 + 1, 1):
        tl.circle(108 * i)

        tl.end_fill()

        # This is the inner circle
        for m in range(1, 1 + 1, 1):
            tl.color("white")
            tl.begin_fill()
            # tl.circle(77 * i)
            tl.circle(80 * m)
            tl.end_fill()

            # Before the half circle

            tl.penup()
            print(tl.position())
            # tl.goto(0, -110)
            tl.goto(-0, -115)
            tl.left(90)
            # tl.color("green")
            tl.color("#008040")
            tl.begin_fill()

            # Creating the half circle
            for w in range(180):
                tl.pendown()
                # tl.forward(1.33)
                tl.forward(1.38)
                tl.right(1)
            tl.right(90)
            tl.forward(115)
            tl.end_fill()
            tl.penup()


crescent()

print(tl.position())

tl.goto(47.5, -0)
tl.color("red")


def star():
    tl.begin_fill()

    tl.right(1)

    for a in range(5):
        tl.pendown()

        tl.forward(81)

        tl.right(145)


star()
tl.end_fill()

tl.penup()

print(tl.pos())

# tl.goto(75, -14)
tl.goto(80, -20)

tl.color("white")

tl.begin_fill()
tl.circle(100)
tl.end_fill()

sc.exitonclick()
