import turtle as t
t.colormode(255)
t.speed(9)

def pen_move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def rec_box(w,h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
def star(w):
    for i in range(5):
        t.left(72)
        t.forward(w)
        t.right(144)
        t.forward(w)

# pen_move(50,100)
# style = ('Arial',15,'italic')
# t.write('Myanmar',font=style,align='center')
pen_move(0,0)
t.fillcolor('red')
t.begin_fill()
rec_box(400,100)
t.end_fill()
pen_move(0,100)
t.fillcolor('green')
t.begin_fill()
rec_box(400,100)
t.end_fill()
pen_move(0,200)
t.fillcolor('yellow')
t.begin_fill()
rec_box(400,100)
t.end_fill()

# rec_x = 400 / 2
# rec_y = 100 / 2

fd = 70

# star_x =  rec_x
# star_y =  rec_y + (fd*2)

# pen_move(star_x,star_y)
pen_move(180,50+(fd*2))
t.fillcolor('white')
t.begin_fill()
star(fd)
t.end_fill()
t.done()