import turtle

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

def draw_circle(x, y, r, pen_color = 'black', fill_color = None):
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x, y-r)
    t.down()
    t.setheading(0) # angle
    t.begin_fill()
    t.circle(r, 360)
    t.end_fill()

def test1():
    myfirst()
    draw_circle(0, 0, 100, 'black', 'blue')
    myfinished()

test1()