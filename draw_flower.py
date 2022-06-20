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
    # t.hideturtle()
    p.exitonclick()

def draw_flower(x, y, r, angle = 0, pen_color = 'black', fill_color1 = 'green', fill_color2 = 'yellow'):
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color1:
        t.fillcolor(fill_color1)

    for i in range(5):
        t.up()
        t.goto(x, y)
        t.setheading(angle)
        t.forward(r*0.8)
        t.down()
        t.begin_fill()
        t.circle(r*0.6)
        t.end_fill()
        angle += 72

    t.up()
    t.goto(x, y-r)
    t.fillcolor(fill_color2)
    t.down()
    t.setheading(0)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def test1():
    myfirst()
    draw_flower(0,0, 30, 15, 'midnight blue', 'forest green','gold')
    draw_flower(-100,0, 24, -25, 'midnight blue', 'spring green','orange')
    myfinished()

test1()