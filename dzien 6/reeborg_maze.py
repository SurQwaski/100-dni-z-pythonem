def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    else:
        if  not wall_on_right():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()