import turtle as turtle_module
import random


def draw_line():
    i = 0
    for i in range(10):
        colors = random.choice(color_list)
        draw.dot(20, colors)
        draw.penup()
        draw.forward(50)


def set_direction_parameters():
    draw.hideturtle()
    draw.penup()
    draw.setheading(225)
    draw.forward(300)
    draw.setheading(0)
    draw.speed(0)


turtle_module.colormode(255)
color_list = [(122, 163, 195), (141, 206, 212), (77, 136, 149), (91, 181, 181),
          (218, 198, 189), (168, 98, 106), (127, 120, 181), (165, 89, 99)]

draw = turtle_module.Turtle()
set_direction_parameters()

for _ in range(10):
    draw_line()
    draw.backward(500)
    draw.left(90)
    draw.forward(50)
    draw.right(90)


screen = turtle_module.Screen()
screen.exitonclick()