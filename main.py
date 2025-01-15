from turtle import Screen
from user_turtle import UserTurtle
from cars import Cars
from score_board import ScoreBoard
import time

my_screen = Screen()
my_screen.bgcolor('black')
my_screen.setup(width=600, height=600)
my_screen.tracer(0)

user = UserTurtle()

cars = Cars()

score = ScoreBoard()

my_screen.listen()
my_screen.onkeypress(user.move_forward, 'Up')

game_on = True
while game_on:
    time.sleep(0.1)
    my_screen.update()

    cars.create_cars()
    cars.move()

    # turtle collide with the car
    for car in cars.all_cars:
        if car.distance(user) < 20:
            game_on = False
            score.game_over()

    # user finishes the game
    if user.finish_game():
        user.go_to_start()
        cars.level_up()
        score.level_increment()
        score.update()

my_screen.exitonclick()
