from turtle import Turtle, Screen
import random

def prepare_racers_from_color_list(color_list):
    racers_list = []
    i = 0

    for color in color_list:
        racers_list.append(Turtle(shape="turtle"))
        racers_list[i].color(color)
        racers_list[i].penup()
        i += 1
    return racers_list

def setup_race(enlisted_racers_list):
    start_x = -220
    start_y = -100

    for turtle in enlisted_racers_list:
        turtle.goto(x=start_x, y=start_y)
        start_y +=50

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue","purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

if user_bet:
    is_race_on = True
    racers_list = prepare_racers_from_color_list(colors)
    setup_race(racers_list)


while is_race_on:
    rand_distance = random.randint(0,10)
    selected_racer = random.choice(racers_list)

    selected_racer.forward(rand_distance)
    current_racer_x = selected_racer.pos()[0]
    if current_racer_x >= 220:
        is_race_on = False
        winners_color = selected_racer.color()[0]
        if winners_color == user_bet:
            print(f"You win! The winner was {winners_color}.")
        else:
            print(f"You lose! The winner was {winners_color}.")



screen.exitonclick()
