import tkinter
import random

##Úlohy z michalpuskel.github.io

def farba():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return f"#{r:02x}{g:02x}{b:02x}"

w = 1000

canvas=tkinter.Canvas(width= w,height= w,background="white")
canvas.pack()

##zaciatok 2. ulohy
def vlajka(x,y,c):
    canvas.create_oval(x,y,300+x,y+300,fill="brown")
    canvas.create_line(150+x,y,150+x,y-200)
    canvas.create_rectangle(150+x,y-200,350+x,y-100,fill=c)

vlajka(0,400,"green")

##koniec 2. ulohy

##zaciatok 3. ulohy
vlajka(600,400,"red")
##koniec 3. ulohy


canvas.create_rectangle(0,500,1000,1000,fill="blue",outline="blue")

##zaciatok 1. ulohy
def mesiac(x,y,z,f,b,v,r):
    canvas.create_oval(x,y,x+z-r,y+z,fill=b,width = 0)
    canvas.create_oval(x+(z//2)-v,y,x+z+(z//2)-v-r,y+z,fill= f,width = 0)    

y = random.randint(50,350)
mesiac(500,y,100,"white","yellow",0,0)
y = w-y
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
for _ in range(1,4):
    

##koniec 8. ulohy
