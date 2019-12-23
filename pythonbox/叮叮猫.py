'''
使用海龟画图工具，画一个叮当猫。
先学习几个基本函数：
import turtle;#引入海龟工具模块
t=turtle.Pen()#创建海龟画笔

t.fillcolor("blue")#填充颜色
t.begin_fill()#开始填充
t.circle(160)#画圆
t.end_fill()#结束填充

t.up() #鼠标抬起
t.goto(-20,240)#重新调整画笔的位置
t.down()#鼠标落下
'''
#画叮当猫。
import turtle as t

#画头
t.fillcolor("blue")
t.begin_fill()
t.circle(160)
t.end_fill()
#画脸
t.fillcolor("white")
t.begin_fill()
t.circle(130)
t.end_fill()
#画眼睛
t.up()
t.goto(-20,240)#第一只眼睛（左）
t.down()
t.fillcolor("#fff")
t.begin_fill()
t.circle(20)
t.up()
t.goto(20,240)#第二只眼睛
t.down()
t.circle(20)
t.end_fill()

#画里面的眼珠黑色部分
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.up()
t.goto(-20,240)
t.down()
t.circle(10)
t.end_fill()

#画鼻子
t.up()
t.goto(0,200)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()
t.right(90)
t.forward(70)
#画嘴巴
t.up()
t.goto(-50,100)
t.down()
t.circle(50,180)

#画胡子
t.up()
t.goto(20,150)
t.down()
t.right(100)
t.forward(80)
t.up()
t.goto(20,180)
t.down()
t.left(30)
t.forward(80)

t.up()
t.goto(20,160)
t.down()
t.left(-10)
t.forward(80)

#画左边胡子
t.up()
t.goto(-20,160)
t.down()
t.right(180)
t.forward(80)

t.up()
t.goto(-20,180)
t.down()
t.right(20)
t.forward(80)

t.up()
t.goto(-20,150)
t.down()
t.right(-40)
t.forward(80)

t.up()
t.goto(0,-80)
t.write("我爱大脸猫", align="center",font=("微软雅黑", 22, "bold"))

t.up()
t.goto(0,-120)
t.write("李家营小学", align="center",font=("方正舒体 常规", 16, "bold"))

t.done()