from turtle import Turtle


class Ball(Turtle):
    """
    A class used to represent a Ball.

    ...

    Attributes
    ----------
    x_offset: int
        the amount to move the ball in
        the x direction.
    y_offset: int
        the amount to move the ball in
        the y direction

    Methods
    -------
    move()
        moves the ball and
        changes direction of the ball
        if it collides with top or bottom
        walls.
    bounce()
        changes the x direction of the ball
    reset_ball()
        moves the ball back to the starting
        position
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_offset = 10
        self.y_offset = 10

    def move(self):
        """moves the ball and
        changes direction of the ball
        if it collides with top or bottom
        walls.
        """
        # Also detects collision with the top or bottom wall
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.y_offset = -self.y_offset
        new_x = self.xcor() + self.x_offset
        new_y = self.ycor() + self.y_offset
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        """changes the x direction of the ball
        """
        self.x_offset *= -1

    def reset_ball(self):
        """moves the ball back to the starting
        position"""
        self.goto(x=0, y=0)
        self.x_offset *= -1
