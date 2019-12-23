#编写程序绘制一个国际象棋的棋盘
import turtle
turtle.speed(30)
turtle.penup()
off = True
for y in range(-40, 30 + 1, 10):
	for x in range(-40, 30 + 1, 10):
		if off:
			turtle.goto(x, y)
			turtle.pendown()
			turtle.begin_fill()
			turtle.color("black")
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.end_fill()
			turtle.penup()
		else:
			turtle.goto(x, y)
			turtle.pendown()
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.forward(10)
			turtle.left(90)
			turtle.penup()
		off = bool(int(off) - 1)
	off = bool(int(off) - 1)
turtle.hideturtle()
turtle.done()