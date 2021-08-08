"""

This script simulates the popular 'Pong' game. This game is
played with two players.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
from paddle import Paddle, LeftPaddle, RightPaddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvheight=600, canvwidth=800)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

ball = Ball()
right_paddle = RightPaddle()
left_paddle = LeftPaddle()
scoreboard = Scoreboard()
screen.onkey(fun=right_paddle.up, key='Up')
screen.onkey(fun=right_paddle.down, key='Down')
screen.onkey(fun=left_paddle.up, key='w')
screen.onkey(fun=left_paddle.down, key='s')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)

    # Detect collision with the left paddle
    if ball.xcor() < -320 and ball.distance(left_paddle) < 50:
        ball.x_offset -= 1
        ball.bounce()
    # Detect collision with the right paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50:
        ball.x_offset += 1
        ball.bounce()
    # Detect if ball missed right paddle
    if ball.xcor() > 325 and ball.distance(right_paddle) > 50:
        scoreboard.left_score += 1
        scoreboard.update_score()
        ball.x_offset = 10
        ball.reset_ball()
    # Detect if ball missed left paddle
    if ball.xcor() < -325 and ball.distance(left_paddle) > 50:
        scoreboard.right_score += 1
        scoreboard.update_score()
        ball.x_offset = -10
        ball.reset_ball()
    ball.move()

screen.exitonclick()