import turtle as t
import time

t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")

t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

time.sleep(2)

t.penup()
t.goto(0,-240)
t.color("violet")
t.write("很OK!",font =( "Arial",60,'normal'))

t.mainloop()