from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.scored_pts = 0
        self.score = Turtle()
        self.score.color("white")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 250)
        self.update()

    def update(self):
        self.scored_pts += 1
        self.score.clear()
        self.score.write(
            f"Score: {self.scored_pts}",
            False,
            align="center",
            font=("Arial", 24, "normal"),
        )
        print(f"{self.scored_pts}")

    def game_over(self):
        self.score.goto(0, 0)
        self.score.write(
            f"GAME OVER!",
            False,
            align="center",
            font=("Arial", 24, "normal"),
        )
