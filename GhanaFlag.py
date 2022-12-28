# Import the turtle, Screen and time module
import time
from turtle import Turtle
from turtle import Screen

# Instantiate the Screen class to the sc object type
sc = Screen()
# Instantiate the Turtle class to the tt object type
tt = Turtle()

# Increase the size of the drawing turtle pen
tt.pensize(2)
# Hide the turtle shape during drawing
tt.hideturtle()
# Increase the speed of the turtle during drawing, the fastest speed is by 10
tt.speed(5)
# place the pen up to avoid and line drawing during the position of the turtle
tt.penup()
# pause the turtle before drawing
time.sleep(3)


# Create a function to Draw a Square

def penDown():
    tt.pendown()
    tt.forward(700)
    tt.right(90)
    tt.forward(200)
    tt.right(90)
    tt.forward(700)
    tt.right(90)
    tt.forward(200)
    tt.right(90)


# Draw the red side of the flag
tt.color("red")


def red():
    tt.goto(-350, 250)
    penDown()


# The beginning of filling the side of the drawing with the color
tt.begin_fill()
# call the red function to execute the code in the body of the red function
red()
# The end to stop the color painting on the drawing
tt.end_fill()

tt.color("yellow")


# Draw the yellow side of the flag
def yellow():
    tt.penup()
    tt.goto(-350, 50)
    penDown()


tt.begin_fill()
yellow()
tt.end_fill()

# Draw the green side of the flag
tt.color("green")


def green():
    tt.penup()
    tt.goto(-350, -150)
    penDown()
    tt.penup()


tt.begin_fill()
green()
tt.end_fill()

# Center and draw the star on the flag
tt.color("black")


def star():
    tt.goto(-100, -25)
    for drawStar in range(5):
        tt.pendown()
        tt.forward(210)
        tt.right(144)


tt.begin_fill()
star()
tt.end_fill()

sc.exitonclick()
