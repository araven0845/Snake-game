from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        # Set up food appearance and initial position
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.move()

    def move(self):
        # Move food to a random location on the screen
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
