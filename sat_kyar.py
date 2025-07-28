import turtle as t
t.speed(5)
t.colormode(200)
t.bgcolor('black')

def pen_move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

pen_move(0,0)
color = ['yellow','red','green','pink']
t.left(90)
for i in range(4):
    t.fillcolor(color[i])
    t.begin_fill()
    t.circle(50,180)
    t.left(90)
    t.forward(100)
    t.end_fill()

t.done()

import turtle as t
t.speed(5)
t.colormode(200)
t.bgcolor('pink')

t.circle(100,360,5)

t.done()