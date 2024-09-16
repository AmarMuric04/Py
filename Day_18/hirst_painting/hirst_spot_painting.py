import random
import turtle as t

import colorgram

COLOR_AMOUNT = 25

# colors = colorgram.extract(
#     r"C:\Users\AMAR\Desktop\a\Py\Day_18\hirst_painting/hirst.jpg", COLOR_AMOUNT
# )

turtle = t.Turtle()
t.colormode(255)

rgb_colors = [
    (133, 164, 201),
    (226, 150, 101),
    (32, 44, 63),
    (164, 58, 48),
    (201, 136, 148),
    (235, 212, 90),
    (47, 100, 142),
    (137, 182, 162),
    (148, 65, 73),
    (161, 32, 30),
    (61, 116, 100),
    (58, 49, 46),
    (229, 165, 170),
    (53, 41, 44),
    (238, 166, 156),
    (213, 84, 74),
    (171, 30, 33),
    (36, 60, 54),
    (15, 96, 70),
    (35, 61, 106),
    (171, 187, 220),
    (196, 99, 106),
    (110, 126, 154),
    (175, 199, 189),
    (17, 85, 106),
    (36, 150, 206),
]
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     rgb_colors.append(color)


print(rgb_colors)

turtle.hideturtle()
turtle.penup()
turtle.goto(-250, -250)
turtle.speed("fastest")

for dot in range(100):
    turtle.penup()
    if dot % 10 == 0 and dot != 0:
        turtle.goto(-250, turtle.ycor() + 50)
    elif dot % 10 != 0:
        turtle.forward(50)
    turtle.pendown()
    turtle.dot(20, random.choice(rgb_colors))


screen = t.Screen()
screen.exitonclick()
