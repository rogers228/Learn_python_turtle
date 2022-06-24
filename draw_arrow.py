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
    # t.speed('fastest') # fastest, fast, normal slow, slowest
    paper.tracer(2) #瞬間完成

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle();  p.tracer(2) #瞬間完成
    p.exitonclick()

    
def draw_arrow(x, y, lenght, arrow_lenght, width, angle = 0, pen_color = 'black', fill_color = None):
    t = myTurtle
    poly = [(0,0)]*7
    if poly:
        t.up()
        t.goto(x, y)
        t.setheading(angle)
        p1 = t.pos()
        t.forward(lenght)
        poly[4] = t.pos()
        t.goto(p1)
        t.right(90)
        t.forward(width/2)
        poly[0] = t.pos()
        t.right(180)
        t.forward(width)
        poly[1] = t.pos()
        t.right(90)
        t.forward(lenght-arrow_lenght)
        poly[2] = t.pos()
        t.left(90)
        t.forward(width*0.6)
        poly[3] = t.pos()
        t.goto(poly[0])
        t.right(90)
        t.forward(lenght-arrow_lenght)
        poly[6] = t.pos()
        t.right(90)
        t.forward(width*0.6)
        poly[5] = t.pos()
    # draw
    t.goto(poly[6])
    t.down()
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()    
    for p in poly:
        t.goto(p)
    t.end_fill()

def test1():
    myfirst()
    draw_arrow(-180,-70,50,20,10,30,'red', 'pink')
    draw_arrow(-120,-33,50,20,10,30,'red')
    draw_arrow(-60,4,50,20,10,30,'red')
    draw_arrow(0,38,50,20,10,30,'red')
    draw_arrow(60,38,120,20,10,-60,'red') 
    myfinished()

test1()