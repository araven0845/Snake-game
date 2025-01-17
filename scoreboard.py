from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the scoreboard at the top of the screen
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update(self):
        # Update the score display
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        # Display "Game Over" message at the center of the screen
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
