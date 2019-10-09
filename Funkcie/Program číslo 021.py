import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

canvas=tkinter.Canvas(width=1000,height=1000,background="white")
canvas.pack()

##zaciatok 2. ulohy
def vlajka(k,c):
    canvas.create_oval(0+k,400,300+k,700,fill="brown")
    canvas.create_line(150+k,400,150+k,200)
    canvas.create_rectangle(150+k,200,350+k,300,fill=c)

vlajka(0,"green")

##koniec 2. ulohy

##zaciatok 3. ulohy
vlajka(600,"red")
##koniec 3. ulohy


canvas.create_rectangle(0,500,1000,1000,fill="blue",outline="blue")

##zaciatok 1. ulohy
def mesiac(x,y,z,f,b,v,r):
    canvas.create_oval(x,y,x+z-r,y+z,fill=b,outline=b)
    canvas.create_oval(x+(z//2)-v,y,x+z+(z//2)-v-r,y+z,fill= f,outline= f)    

y = random.randint(50,350)
mesiac(500,y,100,"white","yellow",0,0)
y = 1000-y
mesiac(500,y,-100,"blue","yellow",-100,-200)
## koniec 1. ulohy

##zaciatok 4. ulohy
mesiac(220,220,60,"green","red",0,0)

##koniec 4. ulohy

##zaciatok 5. ulohy

mesiac(850,230,40,"red","orange",0,0)
mesiac(800,230,40,"red","orange",40,0)

##koniec 5. ulohy

##zaciatok 6. ulohy
def lodka(x,y,a,b,c,v):
    canvas.create_rectangle(x-c,y-2*b,x,y,fill="brown")
    canvas.create_polygon(x,y-2*b,x+a/2,y-b,x,y-b/2,fill="white",outline="black")
    canvas.create_polygon(x-a,y,x+a,y,x+a/2,y+b,x-a/2,y+b,fill="brown")
    mesiac(x,y+v,v,"brown","pink",0,0)
    mesiac(x-v,y+v,v,"brown","pink",v,0)

lodka(500,480,100,50,20,20)
##koniec 6. ulohy

##zaciatok 8. ulohy
lodka(400,600,150,100,40,40)
lodka(200,800,200,150,60,60)

##koniec 8. ulohy
