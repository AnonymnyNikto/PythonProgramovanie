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
zvacsenie_r = 3
zvacsenie_g = 3
zvacsenie_b = 3



while True:
    r = r + zvacsenie_r
    while True:
        g = g + zvacsenie_g
        while True:           
            if b >= 252:
                zvacsenie_b = zvacsenie_b*-1
                b = b + zvacsenie_b
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)
                 
            elif b<=2:
                zvacsenie_b = zvacsenie_b*-1
                b = b + zvacsenie_b
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)
                break
            else:
                
                b = b + zvacsenie_b
                c.create_rectangle(0,0,1000,600,fill = farba(r,g,b))
                c.update()
                c.after(1)

        if g >= 252:
            zvacsenie_g *= -1
        elif g<=2:
            zvacsenie_g *= -1
            break
    if r >= 252:
        zvacsenie_r *= -1
    elif r<=2:
        zvacsenie_r *= -1
        break
            
                
    
