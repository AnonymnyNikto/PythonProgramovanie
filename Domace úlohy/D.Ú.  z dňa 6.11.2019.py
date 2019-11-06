import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

c = tkinter.Canvas(width=1000,height=1000)
c.pack()


for _ in range(1000):
    for _ in range(1,200):
        x = random.randint(1,1000)
        y = random.randint(1,1000)
        c.create_oval(x,y,x+10,y+10,fill="light blue")
    c.update()
    c.after(50)
    c.delete("all")
    
