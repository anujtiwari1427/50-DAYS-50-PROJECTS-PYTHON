from turtle import Screen
from board import board
from coin import Ball
from scoreboard import scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_board = board((350, 0))
l_board = board((-350, 0))
ball = Ball()
scoreboard = scoreboard()

screen.listen()
screen.onkeypress(r_board.go_up,"Up")
screen.onkeypress(r_board.go_down,"Down")
screen.onkeypress(l_board.go_up,"w")
screen.onkeypress(l_board.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_board) < 50 and ball.xcor() > 320 or ball.distance(l_board) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


