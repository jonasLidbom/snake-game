from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The head of the snake which we styre the snake with.

    def create_snake(self):
        # Snake Start.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def reset(self):
        # Clear the snake from the screen.
        for segment in self.segments:
            segment.goto(1000,0)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Adds a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Makes the segments follow each other. From last to first, so that you can steer the snake from segment[0].
        for seg_num in range(len(self.segments) - 1, 0, -1):  # (Start, stop, step)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
