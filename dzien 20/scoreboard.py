from turtle import Turtle
from pathlib import Path

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")

        self.score = 0
        self.highscore = 0

        path = Path("100-dni-z-pythonem/dzien 20/data.txt")

        if path.is_file():
            with open("100-dni-z-pythonem/dzien 20/data.txt", mode="r") as f:
                content = f.read()
                if content != "":
                    self.highscore = int(content)
        else:
            with open("100-dni-z-pythonem/dzien 20/data.txt", mode="w") as f:
                f.write(str(self.highscore))

        self.show_score()

    def increase_score(self):
        self.score += 1

    def update_shown_score(self):
        self.clear()
        self.show_score()

    def show_score(self):
        self.goto(0,270)
        self.write("Score : "+str(self.score)+" High score: "+str(self.highscore), False, align="center", font=('Arial', 16, 'normal'))

    def game_over(self):
        self.update_highscore()
        self.setpos(0,0)
        self.write("Game Over.", False, align="center", font=('Arial', 16, 'normal'))

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

        with open("100-dni-z-pythonem/dzien 20/data.txt", mode="w") as f:
            f.write(str(self.highscore))
        self.update_shown_score()