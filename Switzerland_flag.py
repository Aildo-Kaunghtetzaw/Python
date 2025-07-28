#Switzerland Flag ///***///***///***///***
import turtle as t
t.speed(5)
t.colormode(255)
t.bgcolor('pink')

def pen_move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_rec(color,w,h):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def plus_sign(color,w,h):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.left(90)
        t.fd(w)
        t.right(90)
        t.fd(h)
        t.right(90)
        t.fd(w)
    t.end_fill()


pen_move(0,0)
draw_rec('red',200,200)

rec_x = 200 / 2
rec_y = 200 / 2
width = 50
height = 30
plus_x = rec_x - (width / 2) + 10
plus_y = rec_y + (height / 2) 

pen_move(plus_x,plus_y)
plus_sign('white',width,height)

t.hideturtle()
t.done()