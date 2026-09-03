from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.scored = ""
        self.show_score()

    def update_score(self):
        if self.scored == "left":
            self.lscore += 1
        else:
            self.rscore += 1

        self.clear()
        self.show_score()

    def show_score(self):
        self.goto(-100,220)
        self.write(self.lscore, False, align="center", font=('Arial', 40, 'normal'))

        self.goto(100,220)
        self.write(self.rscore, False, align="center", font=('Arial', 40, 'normal'))

    def show_winner(self):
        self.goto(0,0)
        self.write("The winner is "+self.scored+"!", False, align="center", font=('Arial', 40, 'normal'))

                