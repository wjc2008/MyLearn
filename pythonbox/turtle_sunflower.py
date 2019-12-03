import turtle as t
import time
t.color("red","yellow")
#同时设置pencolor=color1,fillcolor=color2

t.begin_fill()
for _ in range(50):
    t.fd(200)
    t.lt(170)
t.end_fill()

t.mainloop()