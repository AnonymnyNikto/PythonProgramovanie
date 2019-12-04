import tkinter
import random

x_max, y_max = 1000, 600

c = tkinter.Canvas(width = x_max, height = y_max)
c.pack()

def farba(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

r = random.randrange(256)
g = random.randrange(256)
b = random.randrange(256)
x = 3
y = 3
z = 3



while True:
    r = r+z
    while True:
        g = g + y
        while True:           
            if b >= 252:
                x = x*-1
                b = b+x
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)
                 
            elif b<=0:
                x = x*-1
                b = b+x
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)
                break
            else:
                
                b = b+x
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)

        if g >= 252:
            y *= -1
        elif g<=0:
            y *= -1
            break
    if r >= 252:
        z *= -1
    elif r<=0:
        z *= -1
        break
            
                
    
