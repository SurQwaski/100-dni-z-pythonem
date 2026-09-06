from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on = True
while game_on:
    if scoreboard.lscore >= 5 or scoreboard.rscore >= 5:
        game_on = False
        ball.dissapear()
        scoreboard.show_winner()
        break
    else:
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()

        if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
            ball.bounce_of_paddle()

        if ball.xcor() < -400 or ball.xcor() > 400:
            if ball.xcor() < -400:
                scoreboard.scored = "right"
            else:
                scoreboard.scored = "left"

            scoreboard.update_score()
            ball.reset()

        time.sleep(ball.game_speed)

screen.exitonclick()