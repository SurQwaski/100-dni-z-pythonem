from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = 5

    def spawn_car(self):
        if random.randint(1,10) <= 2:
            self.car_list.append(Car())

    def remove_offscreen_cars(self):
        temp_list = self.car_list.copy()
        for car in self.car_list:
            if car.xcor() < -350:
                car.hideturtle()
                temp_list.remove(car)
        self.car_list = temp_list

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.car_speed)

    def remove_all_cars(self):
        for car in self.car_list:
            car.hideturtle()
        self.car_list.clear()

    def increase_all_cars_speed(self):
        self.car_speed += 2.5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(320,random.randint(-240,280))