import tkinter
import random

x_max , y_max = 1600 , 900

c = tkinter.Canvas(width=x_max, height=y_max)
c.pack()

polomer = 5
x = random.randrange(polomer,x_max-polomer)
y = random.randrange(polomer,y_max-polomer)
x_posun = polomer
y_posun = polomer

while True:
    if x >= x_max - polomer and y < y_max - polomer:
        x_posun = - x_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    elif x < x_max - polomer and y >= y_max - polomer:
        y_posun = - y_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    elif x >= x_max - polomer and y >= y_max - polomer:
        x_posun = - x_posun
        y_posun = - y_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    elif x <= polomer and y > polomer:
        x_posun = - x_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    elif x > polomer and y <= polomer:
        y_posun = - y_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    elif x <= polomer and y <= polomer:
        x_posun = - x_posun
        y_posun = - y_posun
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun
    else:
        c.create_oval(x + polomer, y + polomer, x - polomer, y - polomer)
        x += x_posun
        y += y_posun 
    c.update()
    c.after(1)
    c.delete("all")
