from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.goto(0,0)
        self.game_speed = 0.1
        self.velocity = 10
        self.gravity = self.velocity

    def move(self):
            new_x = self.xcor() + self.velocity 
            new_y = self.ycor() + self.gravity
            self.goto(new_x,new_y)

    def bounce(self):
        self.gravity *= -1

    def bounce_of_paddle(self):
         self.velocity *= -1
         self.game_speed *= 0.9

    def dissapear(self):
         self.goto(1000,1000)

    def reset(self):
         self.velocity *= -1
         self.game_speed = 0.1
         self.goto(0,0)
