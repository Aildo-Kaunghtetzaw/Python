import turtle as t
t.colormode(255)
t.speed(10)
def rectangle(a,b):
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)
def star(a):
    for i in range(5):
        t.lt(72)
        t.fd(a)
        t.rt(144)
        t.fd(a)
def pen_move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

pen_move(0,0)
t.fillcolor('red')
t.begin_fill()
rectangle(400,100)
t.end_fill()
pen_move(0,100)
t.fillcolor('white')
t.begin_fill()
rectangle(400,100)
t.end_fill()
pen_move(0,100)
t.fillcolor('blue')
t.begin_fill()
rectangle(120,100)
t.end_fill()
center_rec_x = 120 / 2
center_rec_y = 100 / 2

fd = 28

star_x = center_rec_x
star_y = center_rec_y + (fd*4)
pen_move(star_x,star_y)
t.fillcolor('white')
t.begin_fill()
star(fd)
t.end_fill()
t.done()
