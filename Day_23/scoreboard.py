from turtle import Turtle

FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(-270, 250)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.write(f'level {self.level}', align='left', font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over buddy', align='left', font=FONT)
