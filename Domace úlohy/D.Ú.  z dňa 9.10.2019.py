import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

canvas=tkinter.Canvas(width=1000,height=1000,background=farba())
canvas.pack()



def strom(x,y,z):
    canvas.create_rectangle(x+0.25*z,y,x-0.25*z,y+2*z,fill="brown")
    canvas.create_oval(x-z,y-1.5*z,x+z,y+0.5*z,fill="green")

def trava(x,y,c):
    for i in range(1,c):
        a = random.randint(1,5)
        b = random.randint(-50,50)
        d = random.randint(1,50)
        canvas.create_line(x,y,x-b,y-d,fill="green",width=a)
        
for i in range(1,10):
    strom(random.randint(100,1000),random.randint(100,1000),random.randint(10,100))


for i in range(1,20):
    trava(random.randint(100,1000),random.randint(100,1000),random.randint(1,25))
