from turtle import Turtle

MY_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class UserTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(MY_POSITION)


    def finish_game(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
