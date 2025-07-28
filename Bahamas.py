import turtle as t
t.speed(9)
t.colormode(200)
t.bgcolor('pink')

def pen_move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_rec(color,w,h):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()

def triangle(color,w):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(w)
        t.left(120)
        
    t.end_fill()

pen_move(10,0)
style = ('Arial',17,'italic')
t.write('Bahamas',font=style,align='center')
pen_move(-20,-315)

draw_rec('deepskyblue',550,100)
pen_move(-20,-215)
draw_rec('gold',550,100)
pen_move(-20,-115)
draw_rec('deepskyblue',550,100)
t.right(90)
t.backward(100)

triangle('black',300)

t.hideturtle()
t.done()
