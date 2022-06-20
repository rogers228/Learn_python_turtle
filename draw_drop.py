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

def draw_drop(x, y, r, angle = 0, pen_color = 'black', fill_color = None):
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x, y)
    t.setheading(angle+90)
    t.forward(r*3.5)
    p1 = t.pos()
    t.begin_fill()
    t.setheading(angle) # angle
    t.goto(x, y)
    t.down()
    t.circle(r ,110)
    t.goto(p1)
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle+180) # angle
    t.circle(-r ,110)
    t.goto(p1)
    t.end_fill()

def test1():
    myfirst()
    draw_drop(  0,-60, 30, -10, 'midnight blue', 'blue')
    draw_drop( 57,-12, 25, -10, 'midnight blue', 'royal blue')
    draw_drop(-45,-10, 20, -10, 'midnight blue', 'alice blue')
    myfinished()

test1()