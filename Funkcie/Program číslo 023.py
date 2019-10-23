import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

X_MAX = 800
Y_MAX = 600

canvas=tkinter.Canvas(width=X_MAX,height=Y_MAX,background=farba())
canvas.pack()

v = random.randint(150,300)


def stvorceky(x,y,v,m):
    u = random.randint(6,11)
    for i in range(1,u):
        a = x + v
        b = y + v
        c = x - v
        d = y - v
        canvas.create_retangle(a,b,c,d)
        v = v - m

for i in range(1,11):
    
    v = random.randint(150,300)
    m = random.randint(5,20)
    x = random.randint(,X_MAX-v)
    y = random.randint(0+v,Y_MAX-v)
    stvorcek(x,y,v,m)
