from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
