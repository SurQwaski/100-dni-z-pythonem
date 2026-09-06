import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 300

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.move_up,"Up")

game_is_on = True
while game_is_on:
    car_manager.spawn_car()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()

    if player.ycor() >= FINISH_LINE_Y:
        player.go_back_to_start()
        car_manager.remove_all_cars()
        car_manager.increase_all_cars_speed()
        scoreboard.update_level()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.display_game_over()
            break

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
