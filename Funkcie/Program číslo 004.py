import tkinter
import random

X_MAX, Y_MAX = 800, 600

canvas = tkinter.Canvas(width=X_MAX, height=Y_MAX)
canvas.pack()

def dom(x, y):
    velkost = 150
    canvas.create_rectangle(x - velkost//2, y - velkost//2,
                            x + velkost//2, y + velkost//2,
                            fill='NavajoWhite2')
    canvas.create_polygon(x - velkost//2, y - velkost//2,
                          x + velkost//2, y - velkost//2,
                          x, y - velkost, fill='OrangeRed2')

def oblaky():
    for _ in range(10):
        x, y = random.randrange(X_MAX), random.randrange(Y_MAX/2)
        r = random.randint(20, 40)
        canvas.create_oval(x-r, y-r, x+r, y+r, fill='light sky blue')

oblaky()
dom(200,500)
