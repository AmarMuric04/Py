import random
from turtle import Screen, Turtle

turtles = [Turtle() for _ in range(5)]
screen = Screen()
screen.setup(500, 400)

colors = ["red", "orange", "yellow", "green", "blue"]

for index, turtle in enumerate(turtles):
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(-225, index * 25)
    turtle.color(colors[index])


def move(t):
    global bet
    if t.fillcolor() == bet:
        t.forward(random.randint(4, 20))
    else:
        t.forward(random.randint(0, 20))


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
