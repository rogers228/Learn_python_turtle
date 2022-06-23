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
    t.speed('fastest') # fastest, fast, normal slow, slowest

def myfinished():
    p = paper
    t = myTurtle
    t.hideturtle()
    p.exitonclick()

def draw_star(x, y, r1, r2, angle = 0, pen_color = 'black', fill_color = None):
    '''
        x, y:       星星中心座標
        r1,         內頂點距離中心距離
        r2,         外頂點距離中心距離
        angle:      傾斜角度
        pen_color:  筆顏色
        fill_color: 填充顏色
        '''
    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    lis_vertex1 = []
    t.goto(x, y)
    t.setheading(angle) # angle
    for i in range(5):
        t.forward(r1)
        lis_vertex1.append(t.pos())
        t.goto(x, y)
        t.left(72)

    lis_vertex2 = []
    t.goto(x, y)
    t.setheading(angle+36) # angle
    for i in range(5):
        t.forward(r2)
        lis_vertex2.append(t.pos())
        t.goto(x, y)
        t.left(72)

    t.goto(lis_vertex1[0])
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.down()
    for i in range(5):
        t.goto(lis_vertex1[i])
        t.goto(lis_vertex2[i])
    t.goto(lis_vertex1[0])
    t.end_fill()

def test1():
    myfirst()
    draw_star(0, -20, 20, 40, 15, 'black', 'yellow')
    draw_star(50, 70, 12, 20, 30, 'black', 'orange')
    draw_star(-100, 150, 10, 28, 45, 'black')
    myfinished()

test1()