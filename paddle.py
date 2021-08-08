from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):
    """
    A class used to represent a Paddle.

    ...

    Attributes
    ----------

    Methods
    -------
    up()
        moves the paddle up
    down()
        moves the paddle down
    """
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.setheading(UP)
        self.forward(distance=20)

    def down(self):
        self.setheading(DOWN)
        self.forward(distance=20)


class RightPaddle(Paddle):
    """
    A class used to represent the right paddle.

    """
    def __init__(self):
        super().__init__()
        self.goto(x=350, y=0)


class LeftPaddle(Paddle):
    """
    A class used to represent the left paddle.

    """
    def __init__(self):
        super().__init__()
        self.goto(x=-350, y=0)

