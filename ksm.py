#Kat,Spencer,Max
#cityscape

import turtle
import math
                                                #These variables make it easier to goto each corner
leftSide = turtle.window_width() / 2 * -1
topSide = turtle.window_height() / 2
rightSide = turtle.window_width() / 2
bottomSide = turtle.window_height() / 2 * -1 

turtle.screensize(500,400)

def sky():          #draws the sky by Spencer
    sky = turtle.Turtle()
    sky.up()
    sky.color("SkyBlue")
    sky.fillcolor("SkyBlue")
    sky.goto(leftSide,topSide)
    sky.down()
    sky.begin_fill()
    sky.forward(turtle.window_width())
    sky.right(90)
    sky.forward(turtle.window_height() * (2/3))
    sky.right(90)
    sky.forward(turtle.window_width())
    sky.right(90)
    sky.forward(turtle.window_height() * (2/3))
    sky.right(90)
    sky.end_fill()

def ground():           #draws the ground by Spencer
    ground = turtle.Turtle()
    ground.up()
    ground.goto(leftSide,bottomSide)
    ground.color("Green")
    ground.fillcolor("Green")
    ground.down()
    ground.begin_fill()
    ground.forward(turtle.window_width())
    ground.left(90)
    ground.forward(turtle.window_width() * (1/3))
    ground.left(90)
    ground.forward(turtle.window_width())
    ground.left(90)
    ground.forward(turtle.window_width() * (1/3))
    ground.left(90)
    ground.end_fill()

def building(x,height):         #draws a building at x parameter with a height given in another parameter by Spencer
    building = turtle.Turtle()
    building.up()
    building.goto(x, -97)
    building.color("Black")
    building.fillcolor("Gray")
    building.down()
    building.begin_fill()
    for y in range(0,2):
        building.forward(50)
        building.left(90)
        building.forward(height)
        building.left(90)
    building.end_fill()

def mountain(x,h):
    mountain = turtle.Turtle()
    mountain.penup()
    mountain.fillcolor("gray")
    mountain.right(90)
    mountain.forward(97)
    mountain.right(90)
    mountain.pendown()
    mountain.begin_fill()
    mountain.forward(x)
    mountain.right(135)
    mountain.forward(h)
    mountain.right(90)
    mountain.forward(h)
    mountain.right(135)
    mountain.forward(math.sqrt(2*h*h))
    mountain.end_fill()
    mountain.fillcolor("white")
    mountain.right(135)
    mountain.forward(h-(h/5))
    mountain.begin_fill()
    mountain.forward(h/5)
    mountain.right(90)
    mountain.forward(h/5)
    mountain.right(90)
    mountain.forward(h/10)
    mountain.right(90)
    mountain.forward(h/10)
    mountain.left(90)
    mountain.forward(h/10)
    mountain.right(90)
    mountain.forward(h/10)
    mountain.end_fill()
    
sky()
ground()
mountain(25,250)
building(-160,75)
building(-290,120)
building(120,170)
building(80,85)
building(340,120)
building(260,75)
building(-340,100)
building(-20,150)
building(40,100)
building(-80,100)
building(80,100)


