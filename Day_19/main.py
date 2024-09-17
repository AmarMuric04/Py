from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.speed("fastest")
    turtle.penup()
    turtle.home()
    turtle.setheading(0)
    turtle.clear()
    turtle.pendown()
    turtle.speed("normal")


def toggle_pen():
    if not turtle.isdown():
        turtle.pendown()
    else:
        turtle.penup()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=toggle_pen)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
