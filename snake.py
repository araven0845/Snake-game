from turtle import Turtle

# Constants for initial snake setup and movement
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        # Initialize the snake with its segments and define the head
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create the initial snake body using start positions
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        # Add a new segment to the snake at the specified position
        new_part = Turtle("square")
        new_part.color("white")
        new_part.pu()
        new_part.goto(position)
        self.segments.append(new_part)

    def move(self):
        # Move the snake forward by shifting each segment to the position of the one in front
        for segnum in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segnum - 1].xcor()
            newY = self.segments[segnum - 1].ycor()
            self.segments[segnum].goto(newX, newY)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        # Change direction to up if the snake isn't moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change direction to down if the snake isn't moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change direction to left if the snake isn't moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change direction to right if the snake isn't moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())
