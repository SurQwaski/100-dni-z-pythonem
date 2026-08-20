import turtle as t
import random

def draw_dotted_line(length):
    for _ in range(length):
            tim.forward(10)
            tim.penup()
            tim.forward(10)
            tim.pendown()

def draw_shape(sides_list,size):
      for sides in sides_list:
            degrees_of_turn = 360/sides
            tim.pencolor(random_color())
            for _ in range(sides):
                tim.left(degrees_of_turn)
                tim.forward(size)

def random_color():
      return tuple(random.randint(0,255) for _ in range(3))

def random_walk(steps,distance):
      directions = [0,90,180,270]
      tim.width(4)
      tim.speed("fastest")
      t.colormode(255)
      for _ in range(steps):
            tim.pencolor(random_color())
            direction = random.choice(directions)
            tim.left(direction)
            tim.forward(distance)
  

tim = t.Turtle()
random_walk(2500,10)

screen = t.Screen()
screen.exitonclick()