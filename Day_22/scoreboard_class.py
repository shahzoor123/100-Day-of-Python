from turtle import Turtle

ALIGNMENT = 'center'
FONT = "Courier", 80, "normal"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.l_Score = 0
        self.r_Score = 0
        self.score_update()

    def score_update(self):
        self.goto(-100, 200)
        self.write(self.l_Score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_Score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.score += 1
        self.score_update()

    def r_point(self):
        self.score += 1
        self.score_update()