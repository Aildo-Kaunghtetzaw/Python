#Belgium Flag ///***///***///***///***
import turtle as t
t.speed(8)
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

pen_move(0,0)
draw_rec('black',100,300)
pen_move(100,0)
draw_rec('yellow',100,300)
pen_move(200,0)
draw_rec('red',100,300)
pen_move(300,0)
t.done()

# _____________________________________________

#France Flag ///***///***///***///***
import turtle as t
t.speed(8)
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

pen_move(0,0)
draw_rec('blue',150,300)
pen_move(150,0)
draw_rec('white',150,300)
pen_move(300,0)
draw_rec('red',150,300)
pen_move(450,0)
t.hidetrutle()
t.done()