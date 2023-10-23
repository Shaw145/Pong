import turtle
import winsound


wn = turtle.Screen()
wn.title("PONG by Suman Shaw")
wn.bgpic("background.png") # Set backgroung img
wn.setup(width=1000, height=600) #Set the size of the screen
wn.tracer(0) # Stops the window from updating

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # Default Size 20x20
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretch the width by 5 & length the default
paddle_a.penup()
paddle_a.goto(-450, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(450, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # Default Size 20x20
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #Everytime the ball move to 1px
ball.dy = 0.2 # Speed of the Ball

# Pen (Score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Functions to move the paddles
def paddle_a_up():
    y = paddle_a.ycor() #returns the Y coordinate of paddle A
    if y < 250:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -250:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #returns the Y coordinate of paddle B
    if y < 250:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
        paddle_b.sety(y)


# Keyboard Binding
wn.listen() # listen the keyboard inputs
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



# The Main game Loop
while(1):
    wn.update() # update the screen everytime the loop runs

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for the Ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #Reverse the Ball direction
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -490:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


    # *** Paddle & Ball Collision ****
    if ball.xcor() < -440 and  paddle_a.ycor()+ 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 440 and  paddle_b.ycor()+ 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
