import turtle as t

t.speed(5)
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

# Draw Larger Rectangle
pen_move(0, 0)
t.fillcolor("white")
t.begin_fill()
rectangle(200, 110)
t.end_fill()

# Center Position of Rectangle
rect_center_x = 200 / 2
rect_center_y = 110 / 2

# Radius of Circle
radius = 25  # Adjust this as needed

# Adjusted Position for Circle
circle_x = rect_center_x
circle_y = rect_center_y - radius

# Draw Circle
t.fillcolor("red")
t.begin_fill()
pen_move(circle_x, circle_y)
t.circle(radius)
t.end_fill()
t.done()