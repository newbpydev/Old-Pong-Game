from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()

l_paddle = Paddle(location='left')
r_paddle = Paddle(location='right')
ball = Ball()

screen.listen()

screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s', fun=l_paddle.move_down)
screen.onkey(key='Up', fun=r_paddle.move_up)
screen.onkey(key='Down', fun=r_paddle.move_down)

game_is_on = True
while game_is_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the ball
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with left and right imaginary wall and paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        ball.ball_increase_speed()
    elif ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball.ball_increase_speed()

    # Detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball.ball_reset_speed()

    # Detect if l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.ball_reset_speed()


screen.exitonclick()
