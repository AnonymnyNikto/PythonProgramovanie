import tkinter
import random

x_max, y_max = 1200, 800

c = tkinter.Canvas(width = x_max, height = y_max)
c.pack()


for _ in range(5000):
    y = random.randrange(15,785)
    x = random.randrange(15,1185)
    if 300 < x <= 400:
        farba = "white"
    elif 450>= y > 350:
        farba = "white"
    else :
            farba = "red"

    c.create_oval(x-15,y-15,x+15,y+15,fill = farba)
