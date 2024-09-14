import random
import turtle as t

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


turtle = t.Turtle()
t.colormode(255)
turtle.hideturtle()
turtle.color("red")
turtle.pensize(5)
turtle.speed("fastest")

rotation = [0, 90, 180, 270]

for _ in range(500):
    rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.setheading(random.choice(rotation))
    turtle.forward(25)

    # turtle.color(random.choice(turtle_colors))
    turtle.color(rgb)


screen = t.Screen()
screen.exitonclick()
