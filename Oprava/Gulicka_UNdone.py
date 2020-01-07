import tkinter
from random import randrange

x_max , y_max = 1600 , 900

c=tkinter.Canvas(width=x_max, height=y_max)
c.pack()
c.create_text(x_max/4, y_max/4, text="blue")
c.create_text(x_max/4*3, y_max/4, text="red")
c.create_text(x_max/4, y_max/4*3, text="purple")
c.create_text(x_max/4*3, y_max/4*3, text="green")

c.create_line(0,y_max/2,x_max,y_max/2)
c.create_line(x_max/2,0,x_max/2,y_max)
for _ in range(2000):
    x, y = randrange(x_max), randrange(y_max)
    a, b = randrange(x_max), randrange(y_max)
    farba="black"
    if (y >= y_max/2 and x >= x_max/2):
        farba="green"

    if (y >= y_max/2 and x <= x_max/2):
        farba="blue"

    if (y <= y_max/2 and x >= x_max/2):
        farba="red"

    if (y <= y_max/2 and x <= x_max/2):
        farba="purple"
    
    f = c.create_rectangle(x-5,y-5,x+5,y+5,fill=farba)
