from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()
screen.onkey(snake.turn_up,"Up")
screen.onkey(snake.turn_down,"Down")
screen.onkey(snake.turn_left,"Left")
screen.onkey(snake.turn_right,"Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 10:
        food.spawn()
        scoreboard.increase_score()
        scoreboard.update_shown_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        screen.update()
        time.sleep(1)
        scoreboard.update_shown_score()
        snake.reset()


    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            time.sleep(1)
            scoreboard.update_shown_score()
            snake.reset()

screen.exitonclick()