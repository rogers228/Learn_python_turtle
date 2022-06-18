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
    t.speed('fast') # fastest, fast, normal slow, slowest

def myfinished():
    p = paper
    t = myTurtle
    # t.hideturtle()
    p.exitonclick()

def goto_write(x, y, mystr, size = 12, angle = 0, pen_color = 'black'):
    font=("Verdana", size, "normal")
    t = myTurtle
    t.color(pen_color)
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle) # angle
    t.write(mystr, move=False, align='left', font=font)

def test1():
    myfirst()
    goto_write(-100, 30, 'Hello Pythn',20, 45, 'green')
    myfinished()

test1()