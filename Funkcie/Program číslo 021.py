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
def lodka(x,y,a,c):
    canvas.create_rectangle(x-c,y-2*(a-50),x,y,fill="brown")
    canvas.create_polygon(x,y-2*(a-50),x+a/2,y-(a-50),x,y-(a-50)/2,fill="white",outline="black")
    canvas.create_polygon(x-a,y,x+a,y,x+a/2,y+(a-50),x-a/2,y+(a-50),fill="brown")
    mesiac(x,y+c,c,"brown","pink",0,0)
    mesiac(x-c,y+c,c,"brown","pink",c,0)

lodka(500,480,100,20)
##koniec 6. ulohy

##zaciatok 8. ulohy
x=400
y=600
a=150
b=40

for _ in range(1,3):
    lodka(x,y,a,b)
    x-=200
    y+=200
    a+=50
    b+=20
    

##koniec 8. ulohy
