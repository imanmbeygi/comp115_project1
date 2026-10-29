import turtle

# Set up the drawing window
screen = turtle.Screen()
screen.setup(700, 700)
screen.setworldcoordinates(-200, -200, 200, 200)
screen.bgcolor("black")
screen.title("BMW Emblem")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


# Draw a filled circle
def draw_circle(x, y, radius, fill_color, outline_color, width=2):
    pen.penup()
    pen.goto(x, y - radius)
    pen.setheading(0)
    pen.pensize(width)
    pen.pencolor(outline_color)
    pen.fillcolor(fill_color)
    pen.pendown()

    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()


# Draw one quarter of the inner circle
def draw_sector(start_angle, color):
    radius = 75

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(start_angle)
    pen.forward(radius)
    pen.setheading(start_angle + 90)
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.pendown()

    pen.begin_fill()
    pen.circle(radius, 90)
    pen.goto(0, 0)
    pen.end_fill()
    pen.penup()


# Draw a straight line
def draw_line(x1, y1, x2, y2, color, width=2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()
    pen.goto(x2, y2)
    pen.penup()

# Draw the outer circle
draw_circle(0, 0, 112, "black", "white", 4)

# Draw the inner circle
draw_circle(0, 0, 82, "white", "black", 2)

# Draw the four blue and white sections
for angle in range(0, 360, 90):
    if angle == 0 or angle == 180:
        color = "blue"
    else:
        color = "white"

    draw_sector(angle, color)

# Draw the dividing lines
draw_line(-75, 0, 75, 0, "black", 3)
draw_line(0, -75, 0, 75, "black", 3)

# Draw the inner border
pen.penup()
pen.goto(0, -77)
pen.setheading(0)
pen.pencolor("black")
pen.pensize(2)
pen.pendown()
pen.circle(77)
pen.penup()


turtle.done()
