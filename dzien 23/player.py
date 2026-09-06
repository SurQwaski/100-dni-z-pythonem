from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.color("black")
        self.shape("turtle")

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def go_back_to_start(self):
        self.goto(STARTING_POSITION)
