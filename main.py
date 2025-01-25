from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

# 1. Setup the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Arjun's Snake Game")
screen.tracer(0)  # Turn off animation to manually control screen updates

# 2. Initialize game objects: snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 3. Set up controls for the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# 4. Main game loop
game_on = True
while game_on:
    screen.update()  # Refresh the screen to show updates
    time.sleep(0.1)  # Pause for a short duration to control the game speed
    snake.move()  # Move the snake in its current direction

    # 5. Detect collision with food
    if snake.head.distance(food) <= 15:
        scoreboard.update()  # Update the score
        food.move()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake

    # 6. Detect collision with walls
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        scoreboard.reset_scoreboard()  # Reset game and update high score
        snake.reset_snake()
        snake.head.goto(0, 0)

    # 7. Detect collision with the snake's own body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # If the head collides with any body segment
            scoreboard.reset_scoreboard()  # Display "Game Over" on the screen
            snake.reset_snake()
            snake.head.goto(0,0)

# 8. Exit the game when the screen is clicked
screen.exitonclick()
