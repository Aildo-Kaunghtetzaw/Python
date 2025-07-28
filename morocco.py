#Morocco Flag ///***///***///***///***
import turtle as t
t.speed(8)
t.colormode(255)
t.bgcolor('deepskyblue')

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

def draw_star(w):
    for _ in range(5):
        t.right(144)
        t.forward(w)

pen_move(0,0)
draw_rec('red',500,300)

# rec_x = 500 / 2
# rec_y = 300 / 2

t.pensize(4)
t.pencolor('yellow')
width = 200
# star_x = rec_x + (width/2)
# star_y = rec_y

# pen_move(star_x,star_y)
pen_move(350,190)
draw_star(width)

t.hideturtle()
t.done()