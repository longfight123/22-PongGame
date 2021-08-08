from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class used to represent a Scoreboard.

    ...

    Attributes
    ----------
    left_score: int
        left players current score
    right_score: int
        right players current score

    Methods
    -------
    update_score()
        updates the current score
        for both players on the screen

    """
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.update_score()

    def update_score(self):
        """updates the current score
        for both players on the screen
        """
        self.clear()
        self.goto(x=0, y=290)
        self.write(f'{self.left_score} | {self.right_score}', align='center', font=('Arial', 35, 'bold'))

