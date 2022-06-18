import turtle
import math

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

def draw_line(x1, y1, x2, y2, pen_color = 'black'):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

def test1():
    myfirst()
    draw_line(0, 0, 100, 50, 'red')
    myfinished()

test1()