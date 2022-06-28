# Ping Pong program

import time
import turtle

wn = turtle.Screen()
wn.title('Ping Pong Lets Play')
wn.bgcolor('white')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('black')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('black')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('red')
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = -2
ball.dy = -2.1


# paddle up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    else:
        y = 260
    paddle_a.sety(y)


# paddel_a down
def paddle_a_down():
        y = paddle_a.ycor()
        if y > -250:
            y -= 20
        else:
            y = -260
        paddle_a.sety(y)


# paddle_b up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    else:
        y = 260
    paddle_b.sety(y)


# paddel_b down
def paddle_b_down():
        y = paddle_b.ycor()
        if y > -250:
            y -= 20
        else:
            y = -260
        paddle_b.sety(y)


# Listen keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, 'x')
wn.onkeypress(paddle_b_up, "u")
wn.onkeypress(paddle_b_down, 'n')

# define Variables
score_a = 0
score_b = 0

# define a ScoreBoard
scoreboard = turtle.Turtle()
scoreboard.color('blue')
scoreboard.penup()
scoreboard.goto(0, 275)
# ping_pong = 'Sound effects/Ping_pong.wav'

while True:
    wn.update()
    time.sleep(0)

    # Scoreboard
    scoreboard.clear()
    scoreboard.write(f'{int(score_a)} - TEAM A -- TEAM B - {int(score_b)}', align='center', font=('Courier', 14, 'bold'))

    # ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() > 290:
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.dy *= -1

    if abs(ball.xcor()) >= 350:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= 1
    time.sleep(.01)

    # ball collision. Left Paddle (paddle_a)
    if ball.xcor() < -330:
        if paddle_a.ycor()-50 <= ball.ycor() <= paddle_a.ycor()+50:
            ball.dx *= -1
        else:
            score_b += .5


        # ball collision. Right Paddle (paddle_a)
    if ball.xcor() > 330:
        if paddle_b.ycor() - 50 <= ball.ycor() <= paddle_b.ycor() + 50:
            ball.dx *= -1
        else:
            score_a += .5
