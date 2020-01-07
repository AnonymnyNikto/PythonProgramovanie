import tkinter
import random
X_MAX, Y_MAX = 800, 600

c = tkinter.Canvas(height = Y_MAX, width = X_MAX)
c.pack() 

def click(event):
    x = event.x
    y = event.y
    velkost = 5
    c.create_oval(x + velkost ,y + velkost, x - velkost, y - velkost, fill = "salmon")
    a = X_MAX - x
    c.create_oval(a + velkost ,y + velkost, a - velkost, y - velkost, fill = "gold")
    b = Y_MAX - y
    c.create_oval(x + velkost ,b + velkost, x - velkost, b - velkost, fill = "aqua")
    c.create_oval(a + velkost ,b + velkost, a - velkost, b - velkost, fill = "royal blue")




c.bind("<Motion>", click)
