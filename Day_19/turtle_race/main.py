import random
from turtle import Screen, Turtle

TURTLES = 5
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 500
TURTLE_HEIGHT = 20
TOP_Y = SCREEN_HEIGHT / 2 - TURTLE_HEIGHT
BOTTOM_Y = -TOP_Y + TURTLE_HEIGHT
VERTICAL_RANGE = TOP_Y - BOTTOM_Y - TURTLE_HEIGHT * (TURTLES - 1)

turtles = []
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "magenta",
    "pink",
    "white",
]

for index in range(TURTLES):
    # Creating a turtle
    turtle = Turtle()
    turtles.append(turtle)

    # Modifying the turtle
    turtle.shapesize(stretch_wid=TURTLE_HEIGHT / 20, stretch_len=TURTLE_HEIGHT / 20)
    turtle.shape("turtle")
    turtle.color(colors[index])
    turtle.pensize(10)
    turtle.pencolor(colors[index])

    # Updating the position
    turtle.penup()
    if TURTLES > 1:
        y_position = TOP_Y - index * (VERTICAL_RANGE / (TURTLES - 1) + TURTLE_HEIGHT)
    else:
        y_position = (TOP_Y + BOTTOM_Y) / 2

    turtle.goto(-225, y_position)
    turtle.pendown()

    turtle.speed(1)


def move(t):
    global bet
    move = 0
    if t.fillcolor() == bet:
        move = random.randint(4, 20)
    else:
        move = random.randint(0, 20)

    # Disallowing the turtle to move off-screen
    if move + t.xcor() > SCREEN_WIDTH / 2 - TURTLE_HEIGHT:
        move = SCREEN_WIDTH / 2 - TURTLE_HEIGHT - t.xcor()
    t.forward(move)


bet = screen.textinput(
    title="Make your bet!", prompt="Which turtle will win the race? Enter a color:"
)

race_over = False
while not race_over:
    for turtle in turtles:
        move(turtle)
        if turtle.xcor() >= 225:
            race_over = True
            print(f"The {turtle.fillcolor()} turtle won the race!")
            if bet.lower() != turtle.fillcolor().lower():
                print("You were wrong!")
            else:
                print("Boom! You got it right!")
            break

screen.exitonclick()
