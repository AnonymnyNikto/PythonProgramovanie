import tkinter
import random

c = tkinter.Canvas(height=600,width=900)
c.pack()

farby = ["gold","lime","brown","red"]
pocty = [2,3,4,5]


def krabica(x,y,farba,pocet):
    for _ in range(1,pocet):
        c.create_rectangle(x,y,x-100,y-100,fill = farba)
        c.create_line(x,y,x-100,y-100,fill = "khaki")
        c.create_line(x-100,y,x,y-100,fill = "khaki")
        y -= 100
    farby.remove(farba)
    pocty.remove(pocet)

x = 200
y = 500
for _ in range(1,5):
    krabica(x,y,random.choice(farby),random.choice(pocty))
    x += 200
    
