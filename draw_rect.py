import turtle
import numpy as np

paper = None
myTurtle = None

def myfirst():
    global paper
    paper = turtle.Screen()
    paper.setup(500, 400)

    global myTurtle
    myTurtle = turtle.Turtle(); t = myTurtle
    t.width(2)
    t.speed('fastest') # fastest, fast, normal slow, slowest

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle()
    p.exitonclick()

def draw_rect(x, y, width, heighe, angle = 0, pen_color = 'black', fill_color = None):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x, y)
    t.setheading(angle) # angle
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.down()
    t.forward(width)
    t.left(90)
    t.forward(heighe)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(heighe)
    t.end_fill()

def test1():
    myfirst()
    draw_rect(-60,-60,260,40,30,'black', 'yellow green')
    draw_rect(-60,0,160,40,30,'black')
    myfinished()

test1()