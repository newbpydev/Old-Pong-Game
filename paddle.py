from turtle import Turtle

POS_PADDLE = {'right': (350, 0), 'left': (-350, 0)}


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        position = POS_PADDLE
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position[location])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
