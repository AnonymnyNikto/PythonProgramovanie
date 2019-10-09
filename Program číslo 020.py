import tkinter
import random

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

canvas=tkinter.Canvas(width=1000,height=1000,background=farba())
canvas.pack()

def panelak(x,y,s,v):
    q = (s-1)*40+10
    w = (v-1)*30+10
    canvas.create_rectangle(x,y,x+q,y+w, fill=farba())
    a = 10
    b = 10
    for i in range(1,v):
        for c in range(1,s):
            canvas.create_rectangle(x+a,y+b,x+a+20,y+b+20,fill="blue",outline="brown")
            a = a + 40
        a = 10
        b = b + 30

def mesto ():
    a = random.randint(1,100)
    for i in range(1,a):
        x = random.randint(1,900)
        y = random.randint(1,900)
        s = random.randint(2,10)
        v = random.randint(2,10)
        panelak (x,y,s,v)

mesto()
