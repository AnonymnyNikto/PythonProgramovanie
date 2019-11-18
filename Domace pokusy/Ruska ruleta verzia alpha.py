import tkinter
import random

c = tkinter.Canvas(width = 800, height = 600)
c.pack()

def stvorec(x,y,a,p):
    c.create_rectangle(x,y,x+100,y+100,fill=p)
    c.create_text(x+50,y+50,text=a)

mena11 = "Martin", "Matej", "Ema B.", "Matúš B.", "Nela", "Bibiana"
mena12 = "Teo", "Suri", "Tomáš H.", "Katka", "Matúš H.", "Hanka"
mena13 = "Tomáš M.", "Diana", "Paťo M.", "Veronika", "Saška", "Maťa"
mena14 = "Adam", "David", "Paťo R.", "Mišo", "Jakub", "Andrej"
mena2 = "Ema T.", "Sarah"
mena = mena11 + mena12 + mena13 + mena14 + mena2

x = 100
y = 50

for i in mena11:
    stvorec(x,y,i,"white")
    x += 100

x = 100
y += 100

for i in mena12:
    stvorec(x,y,i,"white")
    x += 100

x = 100
y += 100

for i in mena13:
    stvorec(x,y,i,"white")
    x += 100

x = 100
y += 100

for i in mena14:
    stvorec(x,y,i,"white")
    x += 100


x = 100
y = 450

for u in mena2:
    
    stvorec(x,y,u,"white")
    x += 100

stvorec(600,450,random.choice(mena),"red")



