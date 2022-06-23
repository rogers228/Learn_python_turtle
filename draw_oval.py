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

def draw_oval(x, y, r, angle = 0, pen_color = 'black', fill_color = None):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x, y)
    t.setheading(angle) # angle
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.down()
    for i in range(2):
        print(i)
        t.circle(r*0.5,40)
        t.circle(r,100)
        t.circle(r*0.5,40)
    t.end_fill()

def test1():
    myfirst()
    draw_oval(-20,-70,100,-15,'black', 'silver')
    myfinished()

test1()