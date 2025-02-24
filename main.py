from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting collision with top and bottom walls:
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.y_bounce()

    # Detecting collision with paddles:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Detecting if r_paddle missed the ball:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detecting if l_paddle missed the ball:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        


screen.exitonclick()