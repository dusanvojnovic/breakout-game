from turtle import Screen
from ball import Ball
from brick import Brick
from paddle import Paddle
from scoreboard import Scoreboard
import time

x_positions = range(-450, 510, 80)
y_positions = range(160, 300, 40)
colors = ['yellow', 'blue', 'green', 'red']

screen = Screen()
screen.setup(width = 1000, height = 800)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -370))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

bricks = []

i = 0
for y in y_positions:
    for x in x_positions:
        brick = Brick((x, y))
        brick.color(colors[i])
        bricks.append(brick)
    i += 1

game_is_on = True
count = 0
speed = 0.02

while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # detect collision with side wall
    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_from_side_wall()
    # detect collision with top wall
    if ball.ycor() > 380:
        ball.bounce()
    # detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -365:
        ball.bounce()
    
    # detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 35:
            ball.bounce()
            brick.destroy()
            bricks.remove(brick)

            if brick.color()[0] == 'yellow':
                scoreboard.score += 5
                
            if brick.color()[0] == 'blue':
                scoreboard.score += 10
                
            if brick.color()[0] == 'green':
                scoreboard.score += 15

            if brick.color()[0] == 'red':
                scoreboard.score += 20
                
            scoreboard.update_scoreboard()
    if len(bricks) == 0:
        scoreboard.win_game()
        game_is_on = False
        
    # game end
    if ball.ycor() < -400:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()