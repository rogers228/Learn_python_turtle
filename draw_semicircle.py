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

def draw_semicircle( # 畫半圓
    x, y, lenght, radius_ratio, rotation = 'r', angle = 0, pen_color = 'black', fill_color = None):
    '''
        x, y:       起始點絕對座標
        lenght:     邊長度
        radius_ratio 半徑比例 0.1~1 (1等同半徑等同長度的一半)
        rotation:   畫圓方向 r順時針 l逆時針
        angle:      起始絕對角度
        pen_color:  筆顏色
        fill_color: 填充顏色
        '''
    a = lenght/2
    if radius_ratio < 0.1:
        radius_ratio = 0.1
    if radius_ratio > 1:
        radius_ratio = 1
    height = radius_ratio*(lenght/2) # 半圓高度
    r = (a**2 + height**2)/(2*height) # 半徑
    angle_g= math.degrees(math.acos(a/r)) # 角度
    angle_all= 2*(90-math.degrees(math.acos(a/r))) # 整體角度

    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x, y)
    t.down()
    t.setheading(angle) # angle
    t.begin_fill()
    t.forward(lenght)
    if rotation == 'l': # l逆時針
        t.right(90 + angle_g)
        t.circle(-r, angle_all)
    else: # r順時針
        t.left(90 + angle_g) 
        t.circle(r, angle_all)
    t.end_fill()

def test1():
    myfirst()
    draw_semicircle(0, 0, 100, 1,'l', 10, 'black', 'yellow')
    draw_semicircle(-3, 10, 100, 1,'r',10)
    myfinished()


test1()