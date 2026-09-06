from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.current_lvl = 1
        self.goto(-200,200)
        self.show_level()

    def show_level(self):
        self.write("Level: " + str(self.current_lvl), False, align="center", font=('Arial', 12, 'normal'))

    def update_level(self):
        self.clear()
        self.current_lvl += 1
        self.show_level()

    def display_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, align="center", font=('Arial', 20, 'normal'))

        
