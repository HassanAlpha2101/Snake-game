from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

#The screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

game_is_on = True
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
snake.control()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#detect the collision with wall
    if snake.head.xcor() ==280 or  snake.head.xcor() == -280 or snake.head.ycor() == 280 or  snake.head.ycor() ==-280:
        score.game_over()
        game_is_on = False
# detect the collision with the food
    if snake.head.distance(food) <15:
        snake.extend()
        food.refresh()
        score.increase_score()

    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
