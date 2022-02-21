from turtle import Turtle
from random import randint

DEF_SPEED = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = DEF_SPEED
        # self.setheading(randint(0, 359))
        # self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.setheading(45)
        # self.forward(0.2)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1


    def reset_position(self):
        self.home()
        self.bounce_x()


    def ball_increase_speed(self):
        self.move_speed *= 0.9
        # if self.x_move > 0:
        #     self.x_move += 1
        # else:
        #     self.x_move += -1
        #
        # if self.y_move > 0:
        #     self.y_move += 1
        # else:
        #     self.y_move += -1


    def ball_reset_speed(self):
        self.move_speed = DEF_SPEED
        # self.x_move = 10
        # self.y_move = 10
