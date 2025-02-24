from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detecting collision with top and bottom walls:
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()




screen.exitonclick()