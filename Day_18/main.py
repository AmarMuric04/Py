import random
from turtle import Screen, Turtle

# from turtle import *
# import turtle as tur


turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)


# for _ in range(4):
#     turtle.right(90)
#     turtle.forward(100)

# turtle.forward(100)
# turtle.forward(100)

# for _ in range(3):
#     turtle.right(90)
#     turtle.forward(100)

# turtle.forward(100)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.forward(100)

# for _ in range(50):
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()
#     turtle.forward(5)

sides = 3
turtle_colors = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "black",
    "white",
    "gray",
    "cyan",
    "magenta",
    "lightblue",
    "lightgreen",
    "gold",
    "silver",
    "coral",
    "violet",
    "indigo",
]
for _ in range(150):
    for _ in range(sides):
        # if sides % 2 == 0:
        #     turtle.right(360 / sides)
        # else:
        #     turtle.left(360 / sides)
        turtle.right(360 / sides)
        turtle.forward(100)
    sides += 1
    turtle.color(random.choice(turtle_colors))


screen = Screen()
screen.exitonclick()

# import heroes
