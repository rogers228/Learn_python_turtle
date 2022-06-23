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
    # paper.tracer(2) #瞬間完成

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle()
    p.exitonclick()

def draw_dotted(x1, y1, x2, y2, lenght_dotted = 10, pen_color = 'black'):
    a = lenght_dotted; b = a*0.6
    lenght = np.sqrt((x2-x1)**2 + (y2-y1)**2)
    count = int(lenght // (a+b))
    b = (lenght-count*a)/(count-1)
    angle = np.arctan2(y2-y1, x2-x1)
    t = myTurtle
    t.up()
    t.pencolor(pen_color)
    t.goto(x1, y1)
    t.radians()
    t.setheading(angle)
    for i in range(count):
        t.down()
        t.forward(a)
        t.up()
        t.forward(b)

def test1():
    myfirst()
    draw_dotted(-180,50,180,50,10,'red')
    draw_dotted(-180,0,180,0,12,'black')
    draw_dotted(0,-180,0,180,8,'blue')
    myfinished()

test1()