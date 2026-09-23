from turtle import Screen, TK, shape
import pandas as pd
from cursor import Cursor

screen = Screen()
screen.title("U.S. States Game")
background_image = "100-dni-z-pythonem/dzien 25/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(background_image)
shape(background_image)

game_data = pd.read_csv("100-dni-z-pythonem/dzien 25/day-25-us-states-game-start/50_states.csv")
list_of_states = game_data["state"].tolist()
game_on = True
cursor = Cursor()
score = 0
correct_guesses = []

while game_on:
    if len(correct_guesses) == len(list_of_states):
        TK.messagebox.showinfo(title="Game over!", message="You guessed all the states correctly!")
        break

    scoreboard = str(score)+"/50 States Correct"

    answer_state = screen.textinput(title=scoreboard, prompt="What's another state's name?").title()

    if answer_state == "Exit":
        remaining_states = [state for state in list_of_states if state not in correct_guesses]
        dataframe = pd.DataFrame({"state":remaining_states})
        dataframe.to_csv("100-dni-z-pythonem/dzien 25/day-25-us-states-game-start/remaining_states.csv")
        screen.bye()
        break

    if answer_state in list_of_states and answer_state not in correct_guesses:
        cur_state = game_data[game_data["state"] == answer_state]

        x_cor = cur_state["x"].values[0]
        y_cor = cur_state["y"].values[0]
        state_text = cur_state["state"].values[0]

        cursor.write_text(x=x_cor, y=y_cor, text=state_text)
        correct_guesses.append(state_text)
        score += 1


screen.exitonclick()