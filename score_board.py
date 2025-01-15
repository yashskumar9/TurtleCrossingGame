from turtle import Turtle

FONT_1 = ('Arial', 15, 'normal')
FONT_2 = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT_2)

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align='center', font=FONT_1)
        self.goto(200, 250)
        self.write(f"Score: {self.score}", align='center', font=FONT_1)

    def level_increment(self):
        self.level += 1
        self.score += 50
