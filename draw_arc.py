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

def draw_arc(x, y, r_min, angle_arc, angle_start, scales, pen_color = 'black', fill_color = None):
    # r_min = 10        最小半徑 負值為反向
    # angle_arc = 270   圓弧角 
    # angle_start =120  起始角度 
    # scales = [2,5]    自訂比例 list
    if angle_arc > 360:
        angle_arc = 360

    t = myTurtle
    t.pencolor(pen_color)
    t.up()
    t.goto(x, y)
    t.setheading(angle_start)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.down()
    for s in scales:
        pro = s / sum(scales) # 所占比例 Proportion
        a = angle_arc * pro
        r = r_min*sum(scales) * pro
        t.circle(r, a)
    t.end_fill()

def test1():
    myfirst()
    draw_arc(40,-50,15,300,30,[5,4,5],'black','yellow')
    draw_arc(-25,0,10,150,-72,[2,5,2]) # smile 微笑
    draw_arc(25,30,-8,180,90,[1]) # eye 眼睛
    draw_arc(-15,30,-8,180,90,[1]) # eys 眼睛
    
    myfinished()

test1()