from turtle import Turtle

class Snake():
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]  

    def create_snake(self):
        for _ in range(3):
            self.segment_list.append(self.create_segment())
        
        start_x, start_y = 0,0
        for segment in self.segment_list:
            segment.setpos(start_x,start_y)
            start_x -= 20

    def create_segment(self, position = None):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()

        if position:
            segment.setpos(position)

        return segment        

    def update_segments(self):
        for segment_index in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[segment_index - 1].xcor()
            new_y = self.segment_list[segment_index - 1].ycor()

            self.segment_list[segment_index].goto(new_x,new_y)

    def extend(self):
        new_segment = self.create_segment(self.segment_list[-1].position())
        self.segment_list.append(new_segment)

    def reset(self):
        for segment in self.segment_list:
            segment.hideturtle()
            
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]

    def move(self):
        self.update_segments()
        self.head.forward(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)    

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
