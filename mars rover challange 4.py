#Mars Perseverance Rover - Challenge #3 - www.101computing.net/mars-perseverance-rover/
import turtle
from turtle import *
screen = turtle.Screen()

# this assures that the size of the screen will always be 400x400 ...
screen.setup(400, 400)
screen.bgpic("mars-path-3.png")

# Initialise the rover...
rover = turtle.Turtle()
screen.addshape("rover.gif")
rover.shape("rover.gif")
rover.speed(2)

rover.color("#810000")
rover.pensize(4)
rover.penup()
rover.goto(-165,-165)
rover.pendown()

#Implement Rover Path...

for i in range(2):
    rover.forward(335)
    rover.left(90)

#     # rover.forward(49)
# rover.left(80)
# rover.forward(330)
# rover.right(107)
# rover.forward(49)
# rover.right(73)
# rover.forward(322)
#
# rover.left(95)
# rover.forward(49)
# rover.left(86)
# rover.forward(331)
# rover.right(110)
# rover.forward(46)
# rover.right(71)
# rover.forward(323)
# rover.left(104)
# rover.forward(54)
# rover.left(76)
# rover.forward(330)

done()