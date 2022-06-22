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

def draw_rect_r(x, y, width, height, r=5, angle = 0, pen_color = 'black', fill_color = 'white'):
    h = 2 if height <2 else height - 2*r
    w = 4 if width <4 else width - 2*r
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x+r, y)
    t.begin_fill()
    t.down()
    t.setheading(angle)
    t.forward(w)
    t.circle(r, 90)
    t.forward(h)
    t.circle(r, 90)
    t.forward(w)
    t.circle(r, 90)
    t.forward(h)
    t.circle(r, 90)
    t.end_fill()

def draw_arrow(x1, y1, x2, y2, x3, y3, pen_color = 'black', fill_color = 'white'):
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x1, y1)
    t.begin_fill()
    t.down()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.end_fill()

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
    draw_rect_r(-150, 20,300,100,15)
    draw_arrow(-80,21,-40,-10,-30,21)
    goto_write(-130,50, 'hello! i\'m learning python turtle.\nthis is funning.')
    myfinished()

test1()