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
    t.speed('normal') # fastest, fast, normal slow, slowest

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle()
    p.exitonclick()

def draw_lines(points, pen_color = 'black'):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(points[0])
    t.down()
    for p in points[1:]:
        t.goto(p)

def test1():
    myfirst()
    points = [
        (-120,-50),(10,10),(30,50),(30,150),(-30,100),
        (-60,150),(-120,-50)]
    draw_lines(points, 'orange red')
    myfinished()

test1()