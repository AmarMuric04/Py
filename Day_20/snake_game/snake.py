from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            square = Turtle()
            square.shape("square")
            square.penup()
            square.color("white")
            square.goto(position)
            self.squares.append(square)

    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)

        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        self.squares[0].setheading(90)

    def down(self):
        self.squares[0].setheading(270)

    def left(self):
        self.squares[0].setheading(180)

    def right(self):
        self.squares[0].setheading(0)
