from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.score_r, align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(self.score_l, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()