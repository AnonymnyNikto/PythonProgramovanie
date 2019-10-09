import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

canvas=tkinter.Canvas(width=1000,height=1000,background="white")
canvas.pack()



def strom(x,y,g,z):
    canvas.create_rectangle(x-20,y,x+20,y+z,fill="brown")
    canvas.create_oval(x+g,y,x-g,y+g+g,fill="green")

def trava(x,y,c):
    for i in range(1,c):
        b = random.randint(-50,50)
        d = random.randint(1,50)
        canvas.create_line(x,y,x-b,y-d,fill="green")
        
a = random.randint(1,25)
for i in range(1,a):
    strom(random.randint(100,1000),random.randint(100,1000),random.randint(10,100),random.randint(10,100))

a = random.randint(1,50)
for i in range(1,a):
    trava(random.randint(100,1000),random.randint(100,1000),random.randint(1,25))
