import turtle as t
import random
import colorgram

def draw_dotted_line(length):
    for _ in range(length):
            tim.forward(10)
            tim.penup()
            tim.forward(10)
            tim.pendown()

def random_color():
      return tuple(random.randint(0,255) for _ in range(3))

def extract_color_from_image_to_list(file_path):
      color_list = []
      colors = colorgram.extract(file_path,6)
      for color in colors:
            red, green, blue = color.rgb.r, color.rgb.g, color.rgb.b
            clean_tuple = (red,green,blue)
            color_list.append(clean_tuple)
      return color_list


def draw_shape(sides_list,size):
      for sides in sides_list:
            degrees_of_turn = 360/sides
            tim.pencolor(random_color())
            for _ in range(sides):
                tim.left(degrees_of_turn)
                tim.forward(size)

def spirograph(steps):
      angle = 360/steps
      tim.speed("fastest")
      t.colormode(255)
      for _ in range(steps):
            tim.pencolor(random_color())
            tim.circle(100)
            tim.left(angle)

def draw_painting(size):
      color_list = extract_color_from_image_to_list('100-dni-z-pythonem/dzien 18/image.jpg')
      start_x = -500/2
      start_y = -500/2
      t.colormode(255)

      for _ in range(size):
            tim.teleport(start_x,start_y)
            for _ in range(size):
                  tim.dot(size,random.choice(color_list))
                  tim.penup()
                  tim.forward(50)
                  tim.pendown()
            start_y += 50
            

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
screen = t.Screen()
screen.screensize(500,500)
draw_painting(10)
screen.exitonclick()
