import turtle

wn = turtle.Screen()
wn.title("jimbex pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

Score_a = 0
Score_b = 0
# Paddle A
Paddle_a = turtle.Turtle()
Paddle_a.speed(0)
Paddle_a.shape("square")
Paddle_a.color("white")
Paddle_a.shapesize(stretch_wid=5, stretch_len=1)
Paddle_a.penup()
Paddle_a.goto(-350, 0)

# Paddle B
Paddle_b = turtle.Turtle()
Paddle_b.speed(0)
Paddle_b.shape("square")
Paddle_b.color("white")
Paddle_b.shapesize(stretch_wid=5, stretch_len=1)
Paddle_b.penup()
Paddle_b.goto(+350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0 ", align="center", font=("courier", 24, "normal"))

# functions
def paddle_a_up():
	y = Paddle_a.ycor()
	y += 20
	Paddle_a.sety(y)

def paddle_a_down():
	y = Paddle_a.ycor()
	y -= 20
	Paddle_a.sety(y)

def paddle_b_up():
	y = Paddle_b.ycor()
	y += 20
	Paddle_b.sety(y)

def paddle_b_down():
	y = Paddle_b.ycor()
	y -= 20
	Paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while  True:
	wn.update()

	# move the ball

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking

	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		Score_a += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {} ".format(Score_a, Score_b), align="center", font=("courier", 24, "normal"))


	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		Score_b += 1
		pen.clear()
		pen.write("Player A: {}   Player B: {} ".format(Score_a, Score_b), align="center", font=("courier", 24, "normal"))

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Paddle_b.ycor() + 50 and ball.ycor() > Paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx *= -1
	
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Paddle_a.ycor() + 50 and ball.ycor() > Paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1

	if Paddle_a.ycor() > 250:
		Paddle_a.sety(250)

	if Paddle_a.ycor() < -250:
		Paddle_a.sety(-250)

	if Paddle_b.ycor() > 250:
		Paddle_b.sety(250)

	if Paddle_b.ycor() < -250:
		Paddle_b.sety(-250)

	if Score_a == 5:
		ball.goto(0, 0)
		pen.clear()
		pen.write("Player A wins", align="center", font=("courier", 24, "normal"))

	if Score_b == 5:
		ball.goto(0, 0)
		pen.clear()
		pen.write("Player B wins", align="center", font=("courier", 24, "normal"))
	