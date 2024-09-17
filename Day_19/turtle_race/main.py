import random
from turtle import Screen, Turtle

turtles = [Turtle() for _ in range(5)]
screen = Screen()

for index, turtle in enumerate(turtles):
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(-500, index * 50)


def move(t):
    t.forward(random.randint(0, 20))


while not any(turtle.xcor() >= 500 for turtle in turtles):
    for turtle in turtles:
        move(turtle)

screen.exitonclick()
