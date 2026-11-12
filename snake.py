from turtle import Turtle,Screen
POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.tim = Turtle()
        self.my_snake = []
        self.shape()
        self.head=self.my_snake[0]
        self.screen = Screen()

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def turn_up(self):
        if self.head.heading() != 270:
           self.head.setheading(90)

    def control(self):
        self.screen.listen()
        self.screen.onkey(self.move_right, "Right")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.turn_up, "Up")
        self.screen.onkey(self.turn_down, "Down")

    def shape (self):
        for i in POSITION:
            self.add_segment(i)

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.my_snake.append(tim)

    def extend (self):
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake) - 1, 0, -1):
            x_cord = self.my_snake[seg_num - 1].xcor()
            y_cord = self.my_snake[seg_num - 1].ycor()
            self.my_snake[seg_num].goto(x_cord, y_cord)
        self.head.forward(20)
