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

def draw_triangle(color,w):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(w)
        t.left(120)
    t.end_fill()

pen_move(50,0)
style = ('timesnewroman',20,'italic')
t.write('Czech Republic',font=style,align='center')
pen_move(-50,-315)
draw_rec('red',610,150)
pen_move(-50,-165)
draw_rec('white',610,150)
pen_move(-50,-15)
t.right(90)
draw_triangle('blue',300)

t.done()