from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the scoreboard at the top of the screen
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.pu()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()


    def update(self):
        # Update the score display
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset_scoreboard(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update()
