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

def mesiac(x,y,z,f,b,v,r):
    p = canvas.create_oval(x,y,x+z-r,y+z,fill=b,width = 0)
    m = canvas.create_oval(x+(z//2)-v,y,x+z+(z//2)-v-r,y+z,fill= f,width = 0)
    return p, m

y = random.randint(50,350)
mesiac(500,y,100,"white","yellow",0,0)
z = w-y
mesiac(500,z,-100,"blue","yellow",-100,-200)

    
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



##zaciatok 4. ulohy
mesiac(220,220,60,"green","red",0,0)

##koniec 4. ulohy

##zaciatok 5. ulohy

mesiac(850,230,40,"red","orange",0,0)
mesiac(800,230,40,"red","orange",40,0)

##koniec 5. ulohy

##zaciatok 6. ulohy
def lodka(x,y,a,c):
    p = canvas.create_rectangle(x-c,y-2*(a-50),x,y,fill="brown")
    m = canvas.create_polygon(x,y-2*(a-50),x+a/2,y-(a-50),x,y-(a-50)/2,fill="white",outline="black")
    n = canvas.create_polygon(x-a,y,x+a,y,x+a/2,y+(a-50),x-a/2,y+(a-50),fill="brown")
    r = mesiac(x,y+c,c,"brown","pink",0,0)
    t = mesiac(x-c,y+c,c,"brown","pink",c,0)
    r1 = r[0]
    r2 = r[1]
    t1 = t[0]
    t2 = t[1]
    return p, m, n, r1, r2, t1, t2
x = 500
y = 400
z = 200
for _ in range(1,50):
    i = lodka(x,480,100,20)
    ra = lodka(y,500,150,40)
    rb = lodka(z,800,200,60)
    canvas.update()
    canvas.after(100)
    for idd in i:
        canvas.delete(idd)
    for idd in ra:
        canvas.delete(idd)
    for idd in rb:
        canvas.delete(idd)
    x += 10
    y += 30
    z += 60


##koniec 6. ulohy


##zaciatok 1. ulohy
##t = 500
##for _ in range(50):
##    a = mesiac(500,t,100,"blue","yellow",0,0)
##    y = w-t
##    b = mesiac(500,y,-100,"white","yellow",-100,-200)
##    
##    t += 10
##    canvas.update()
##    canvas.after(50)
##    for i in b:
##        canvas.delete(i)
##    for i in a:
##        canvas.delete(i)
##



