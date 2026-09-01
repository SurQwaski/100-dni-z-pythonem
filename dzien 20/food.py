from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.spawn()

    def spawn(self):
        random_x = random.randrange(-260,260,20)
        random_y = random.randrange(-260,260,20)
        self.setpos(random_x,random_y)