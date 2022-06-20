import turtle

paper = None
myTurtle = None

def myfirst():
    global paper
    paper = turtle.Screen()
    paper.setup(500, 400)

    global myTurtle
    myTurtle = turtle.Turtle(); t = myTurtle
    t.width(4)
    t.speed('fastest') # fastest, fast, normal slow, slowest

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle()
    p.exitonclick()

def draw_waves(x, y, r, count, angle = 0, pen_color = 'black'):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x, y)
    t.setheading(angle+270) # angle
    t.down()
    for i in range(count):
        ra = -1 if i % 2 else 1
        t.circle(ra * r * 0.1 ,30)
        t.circle(ra * r * 1   ,120)
        t.circle(ra * r * 0.1 ,30)

def test1():
    myfirst()
    draw_waves(-200,-150,10,10,0,'steel blue')
    draw_waves(-240,-100,10,27,0,'blue')
    myfinished()

test1()