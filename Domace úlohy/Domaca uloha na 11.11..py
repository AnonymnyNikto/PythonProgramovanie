import tkinter
import random

c = tkinter.Canvas(width=800,height=600)
c.pack()

def vlacik(x,y,f,opakovanie):
    for _ in range(opakovanie):
        c.create_line(x-90,y-10,x+90,y-10,width=5)
        c.create_rectangle(x-80,y-80,x+80,y,fill=f)
        c.create_oval(x-60,y-20,x-20,y+20,fill="black")
        c.create_oval(x+60,y+20,x+20,y-20,fill="black")
        x += 180

vlacik(100,120,"red",4)
vlacik(100,300,"lime",2)
vlacik(100,480,"blue",3)
