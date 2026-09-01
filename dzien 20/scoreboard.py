from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setpos(0,270)

        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.increase_score()
        self.clear()
        self.show_score()

    def show_score(self):
        self.write("Score : "+str(self.score), False, align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.setpos(0,0)
        self.write("Game Over", False, align="center", font=('Arial', 16, 'normal'))