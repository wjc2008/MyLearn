#绘制象棋盘
import turtle as t
t.speed(100)
def angle(x,y):
    t.penup()
    t.goto(x+3,y+3)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+3,y+3)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x+3,y-3)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+3,y-3)
    t.left(90)
    t.forward(-5)
    t.penup()
    t.goto(x-3,y+3)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-3,y+3)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x-3,y-3)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-3,y-3)
    t.left(90)
    t.forward(-5)
def v(x,y):
    t.penup()
    t.goto(x+3,y+3)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+3,y+3)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x+3,y-3)
    t.pendown()
    t.setheading(0)
    t.forward(5)
    t.goto(x+3,y-3)
    t.left(90)
    t.forward(-5)
    t.penup()
def a(x,y):
    t.penup()
    t.goto(x-3,y+3)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-3,y+3)
    t.left(90)
    t.forward(5)
    t.penup()
    t.goto(x-3,y-3)
    t.pendown()
    t.setheading(0)
    t.forward(-5)
    t.goto(x-3,y-3)
    t.left(90)
    t.forward(-5)
#1.绘制所有横线
t.penup()
t.goto(-80,90)
t.pendown()
for i in range(1,6,1):
    t.forward(160)
    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    t.forward(160)
    t.penup()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.pendown()
#2.绘制所有竖线
t.left(90)
t.penup()
t.forward(20)
t.pendown()
for i in range(1,5,1):
    t.forward(80)
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(80)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(80)
    t.penup()
    t.forward(20)
    t.pendown()
    t.forward(80)
    t.left(90)
    t.forward(20)
    t.left(90)
t.forward(180)
t.left(90)
t.forward(160)
t.left(90)
t.forward(180)
#3.绘制斜线
t.left(90)
t.forward(60)
t.left(45)
t.forward(40*1.414)
t.left(45)
t.forward(-40)
t.left(45)
t.forward(40*1.414)
t.penup()
t.goto(-20,90)
t.pendown()
t.right(180)
t.forward(40*1.414)
t.right(45)
t.forward(-40)
t.right(45)
t.forward(40*1.414)
#4.绘制炮和兵的位置
angle(60,50)
angle(-60,50)
angle(60,-50)
angle(-60,-50)
angle(40,30)
angle(-40,30)
angle(40,-30)
angle(-40,-30)
angle(0,30)
angle(0,-30)


a(80,30)
a(80,-30)
v(-80,-30)
v(-80,30)
#5.绘制外围线   绘制一个长方形，设置笔的粗细
t.penup()
t.goto(-90,-100)
t.pendown()
t.pensize(10)
t.forward(200)
t.right(90)
t.forward(180)
t.right(90)
t.forward(200)
t.right(90)
t.forward(180)
t.right(90)