import tkinter
import random

X_MAX, Y_MAX = 800, 600

c=tkinter.Canvas(height=Y_MAX,width=X_MAX)
c.pack()

def stvorce(velkost_najvacsi, pocet, medzera, x, y,):
    velkost = velkost_najvacsi
    for _ in range(pocet):
        c.create_rectangle(x - velkost//2, y - velkost//2, velkost//2 + x, velkost//2 + y)
        velkost -= medzera


for _ in range(11):
    velkost_najvacsi = random.randint(150,301)
    f = 10 + (velkost_najvacsi//2)
    x = random.randint(f,X_MAX-f)
    y = random.randint(f,Y_MAX-f)
    stvorce(velkost_najvacsi, random.randint(5,11), 10, x, y)




