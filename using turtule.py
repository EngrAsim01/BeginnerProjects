import random
import turtle
from random import *

myPen = turtle.Turtle()
myPen.shape('turtle')
myPen.speed(1)
myPen.pensize(5)


# myPen.color(40, 40, 40)

def add_text(message, x, y):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.write(message, False, 'center', ("", 25, 'italic'))


def snow(color, x, y, size, branches):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()

    myPen.color(color)
    myPen.left(90)

    for i in range(0, branches):
        myPen.forward(100 * size / 100)
        myPen.forward(-40 * size / 100)
        myPen.left(40)
        myPen.forward(30 * size / 100)
        myPen.forward(-30 * size / 100)
        myPen.right(80)
        myPen.forward(30 * size / 100)
        myPen.forward(-30 * size / 100)
        myPen.left(40)
        myPen.forward(-60 * size / 100)
        myPen.left(360 / branches)


for i in range(0, 10):
    randomSize = randint(20, 60)

    randomX = randint(-180, 180)
    randomY = randint(-180, 180)

    clr = ['green', 'blue', 'purple', 'red', 'yellow']
    color = choice(clr)

    branches = randint(5, 8)
    snow(color, randomX, randomY, randomSize, branches)

add_text('Hello December', 0, 0)

turtle.done()
# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
