import tkinter
import random

x_max, y_max = 1200, 800

c = tkinter.Canvas(width = x_max, height = y_max)
c.pack()

def click(event):
    x = event.x
    y = event.y
    a = 10
    c.create_oval(x+a,y+a,x-a,y-a,fill = "aqua")
    b = x_max -x
    c.create_oval(b+a,y+a,b-a,y-a,fill = "lime")
    d = y_max -y
    c.create_oval(x+a,d+a,x-a,d-a,fill = "salmon")
    c.create_oval(b+a,d+a,b-a,d-a,fill = "gold")

c.bind("<Motion>",click)
