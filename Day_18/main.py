from turtle import Screen, Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)


for _ in range(4):
    turtle.right(90)
    turtle.forward(100)

screen = Screen()
screen.exitonclick()
