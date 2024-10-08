import random
import turtle as t


def rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle = t.Turtle()
t.colormode(255)
turtle.speed("fastest")
# turtle.pensize(2)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.circle(200)
        turtle.setheading(turtle.heading() + size_of_gap)
        turtle.color(rgb_color())


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
