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

def draw_polygon(x, y, quantity, lenght, angle = 0, pen_color = 'black', fill_color = None):
    if quantity < 3:
        quantity = 3
    if quantity > 20:
        quantity = 20
    a = ((quantity-2)*180)/quantity
    t = myTurtle
    t.pencolor(pen_color)
    if fill_color:
        t.fillcolor(fill_color)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.down()
    t.setheading(angle)
    for i in range(quantity):
        t.forward(lenght)
        t.left(180-a)
    t.end_fill()

def test1():
    myfirst()
    draw_polygon(-50,-50,3,50,30,'black', 'red')
    draw_polygon(-120,10,4,40,0,'black', 'green')
    draw_polygon(50,50,5,40,0,'black', 'yellow')
    draw_polygon(80,-50,6,35,30,'black', 'blue')
    draw_polygon(-180,-10,7,30,0,'black', 'orange')
    draw_polygon(0,-120,8,25,0,'black', 'magenta')
    myfinished()

test1()