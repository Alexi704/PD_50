import turtle
import time

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("springgreen")

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(2)

# draw sun
my_turtle.color("yellow")
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.setposition(150, 150)
my_turtle.begin_fill()
my_turtle.pendown()
my_turtle.circle(50)
my_turtle.end_fill()

# draw rays
my_turtle.penup()
my_turtle.goto(150, 140)
my_turtle.pendown()
my_turtle.goto(150, 130)

my_turtle.penup()
my_turtle.goto(150, 260)
my_turtle.pendown()
my_turtle.goto(150, 270)

my_turtle.penup()
my_turtle.goto(210, 200)
my_turtle.pendown()
my_turtle.goto(220, 200)

my_turtle.penup()
my_turtle.goto(90, 200)
my_turtle.pendown()
my_turtle.goto(80, 200)

# I quad
my_turtle.penup()
my_turtle.goto(185 + 7, 165 - 7)
my_turtle.pendown()
my_turtle.goto(185 + 14, 165 - 14)

# II quad
my_turtle.penup()
my_turtle.goto(185 + 7, 235 + 7)
my_turtle.pendown()
my_turtle.goto(185 + 14, 235 + 14)

# III quad
my_turtle.penup()
my_turtle.goto(115 - 7, 235 + 7)
my_turtle.pendown()
my_turtle.goto(115 - 14, 235 + 14)

# IV quad
my_turtle.penup()
my_turtle.goto(115 - 7, 165 - 7)
my_turtle.pendown()
my_turtle.goto(115 - 14, 165 - 14)

shift = 90
# draw lines
my_turtle.penup()
my_turtle.goto(-190, -180 - shift)
my_turtle.color("red")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(190, -180 - shift)

my_turtle.penup()
my_turtle.goto(-160, -150 - shift)
my_turtle.color("purple")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(160, -150 - shift)

my_turtle.penup()
my_turtle.goto(-130, -120 - shift)
my_turtle.color("teal")
my_turtle.pensize(6)
my_turtle.pendown()
my_turtle.goto(130, -120 - shift)

# draw cake
my_turtle.penup()
my_turtle.goto(-74, -110 - shift)
my_turtle.pendown()
my_turtle.color("white")
my_turtle.goto(50, -110 - shift)
my_turtle.left(90)
my_turtle.forward(60)
my_turtle.left(90)
my_turtle.forward(125)
my_turtle.left(90)
my_turtle.forward(60)

# draw candles
my_turtle.penup()
my_turtle.goto(-60, -40 - shift)
my_turtle.color("aquamarine")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-60, -20 - shift)

my_turtle.penup()
my_turtle.goto(-40, -40 - shift)
my_turtle.color("yellow")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-40, -20 - shift)

my_turtle.penup()
my_turtle.goto(-20, -40 - shift)
my_turtle.color("green")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(-20, -20 - shift)

my_turtle.penup()
my_turtle.goto(0, -40 - shift)
my_turtle.color("pink")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(0, -20 - shift)

my_turtle.penup()
my_turtle.goto(20, -40 - shift)
my_turtle.color("blue")
my_turtle.pendown()
my_turtle.pensize(3)
my_turtle.goto(20, -20 - shift)

# print message
my_turtle.penup()
my_turtle.goto(0, 130 - shift)
my_turtle.color("red")
my_turtle.pendown()
str1 = b'\xd0\x9c\xd0\xb8\xd0\xbb\xd1\x8b\xd0\xb5 \xd0\xb4\xd0\xb5\xd0\xb2\xd1\x83\xd1\x88\xd0\xba\xd0\xb8!'
my_turtle.write(
    str1.decode(), move=False,
    font=("Helvetica", 28, "bold"), align='center')

my_turtle.penup()
my_turtle.goto(0, 70 - shift)
my_turtle.color("red")
my_turtle.pendown()
str2 = b'\xd0\xa1 \xd0\xb4\xd0\xbd\xd1\x91\xd0\xbc 8 \xd0\xbc\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0!!!'
my_turtle.write(
    str2.decode(), move=False,
    font=("Helvetica", 30, "bold"), align='center')

# send the turtle to the corner
my_turtle.pensize(1)
my_turtle.penup()
my_turtle.goto(-330, 330)
time.sleep(10)