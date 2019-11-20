import tkinter
import random

c = tkinter.Canvas(height=600,width=600)
c.pack()

c.create_line(0,0,600,600)
idd = 0

while True:
    x = 2
    
    while(x < 599 and x > 1):
        c.delete(idd)
        idd = c.create_oval(x-5,x-5,x+5,x+5,fill = "red")
        x += 1
        c.update()
        c.after(100)

