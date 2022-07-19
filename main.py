from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Message import Message


import time

message = Message()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

message.intro()
time.sleep(1)
message.clean()

screen.tracer(0)
screen.listen()

paddle1 = Paddle(380)  # generates LHS Paddle
paddle1.line()
paddle2 = Paddle(-380)  # generates RHS Paddle
ball = Ball()

lesc = Message()
risc = Message()

left = 0
lesc.score(left, -30)
lesc.player_name(-352, 1)
right = 0
risc.score(right, 30)
risc.player_name(348, 2)

while True:
    screen.update()
    time.sleep(0.08)
    ball.move()
    screen.onkey(paddle1.up, "Up")
    screen.onkey(paddle1.down, "Down")
    screen.onkey(paddle2.up, "w")
    screen.onkey(paddle2.down, "s")
    ball.bounce_wall()
    if ball.xcor() > 360:
        pos = paddle1.position()
        ball.rebound(pos)
    if ball.xcor() < -360:
        pos = paddle2.position()
        ball.rebound(pos)

    if ball.scorer() == 1:
        left += 1
        lesc.score(left, -30)
        lesc.player_name(-352, 1)
        ball = Ball()
        paddle1.goback(380)
        paddle2.goback(-380)
    if ball.scorer() == 2:
        right += 1
        risc.score(right, 30)
        risc.player_name(348, 2)
        ball = Ball()
        paddle1.goback(380)
        paddle2.goback(-380)
    if left == 5:
        message.winner(-200, "1")
        break
    elif right == 5:
        message.winner(200, "2")
        break

screen.exitonclick()
