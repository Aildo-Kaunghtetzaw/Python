import turtle as t

t.speed(8)
t.colormode(255)
def pen_move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def rectangle(a, b):
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
def star(fd):
    for i in range(5):
        t.left(72)
        t.forward(fd)
        t.right(144)
        t.forward(fd)
# Draw Larger Rectangle
pen_move(0, 0)
t.fillcolor("red")
t.begin_fill()
rectangle(450, 110)
t.end_fill()
pen_move(0,110)
t.fillcolor("green")
t.begin_fill()
rectangle(450, 110)
t.end_fill()
pen_move(0,220)
t.fillcolor("yellow")
t.begin_fill()
rectangle(450, 110)
t.end_fill()
center_rec_x = 450 / 2
center_rec_y = 110 / 2
fd = 80
center_star_x = center_rec_x
center_star_y = center_rec_y + (fd*2)
pen_move(center_star_x,center_star_y)
t.fillcolor("white")
t.begin_fill()
star(fd)
t.end_fill()
t.hideturtle()
t.done()