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

def draw_eddy(x, y, pitch, circletime, angle = 0, pen_color = 'black'):
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle)
    r = pitch
    for i in range(circletime*2):
        t.circle(r, 180)
        r += pitch

def test1():
    myfirst()
    draw_eddy(-50,-50,5,8,45,'medium blue')
    draw_eddy(80,80,3,12,0,'gold')
    myfinished()

test1()