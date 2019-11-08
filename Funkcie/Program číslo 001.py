import tkinter
import random

X_MAX, Y_MAX = 800, 600

c=tkinter.Canvas(height=Y_MAX,width=X_MAX)
c.pack()

def stvorce(a,b,s,d,X_MAX, Y_MAX):
    for _ in range(1,d):
        k = a
        f = 10 + (k/2)
        x = random.randint(f,X_MAX-f)
        y = random.randint(f,Y_MAX-f)
        for _ in range(b):
            c.create_rectangle(x - k/2, y - k/2, k/2 + x, k/2 + y)
            k -= s
        

stvorce(random.randint(150,301), random.randint(5,11), 10, 11, X_MAX, Y_MAX)
