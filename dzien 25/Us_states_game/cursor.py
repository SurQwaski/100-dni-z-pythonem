from turtle import Turtle

class Cursor(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()

    def write_text(self, x, y, text):
        self.goto(x,y)
        self.write(text)