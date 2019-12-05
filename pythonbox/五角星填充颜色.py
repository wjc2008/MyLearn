import turtle
def colorstar(c1,c2,d):
    p.color(c1,c2)
    p.begin_fill()
    for i in range(5):
        p.forward(d)
        p.right(144)
    p.end_fill()
Icolor = input("input a line color")
Fcolor = input("input a fill color")
length = eval(input("input the length of line"))
# paintstar()
colorstar(Icolor,Fcolor,length)
turtle.done()   #不能用p.done()