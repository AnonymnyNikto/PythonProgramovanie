import tkinter
import random

x_max, y_max = 1200, 800

c = tkinter.Canvas(width = x_max, height = y_max)
c.pack()

b = 30
a = 10
kreslit = False
farba = "Black"
farba_y = y_max - 2*b

def cervena():
    global cervena_x
    cervena_x = x_max - 2*b
    c.create_rectangle(cervena_x,farba_y,cervena_x + 2*b,farba_y + 2*b, fill = "red")
    
def modra():
    global modra_x
    modra_x = x_max - 4*b
    c.create_rectangle(modra_x,farba_y,modra_x + 2*b,farba_y + 2*b, fill = "blue")

def zelena():
    global zelena_x
    zelena_x = x_max - 6*b
    c.create_rectangle(zelena_x,farba_y,zelena_x + 2*b,farba_y + 2*b,fill = "green")
    

def cierna():
    global cierna_x
    cierna_x = x_max - 8*b
    c.create_rectangle(cierna_x,farba_y,cierna_x + 2*b,farba_y + 2*b, fill="black")

cervena()
zelena()
cierna()
modra()

def hruba():
    global hruba_x
    hruba_x = 0
    c.create_rectangle(hruba_x,farba_y,hruba_x + 2*b,farba_y + 2*b)
    c.create_oval(hruba_x,farba_y,hruba_x + 2*b,farba_y + 2*b, fill = "black")
    
def stredna():
    global stredna_x
    stredna_x = 2*b
    c.create_rectangle(stredna_x,farba_y,stredna_x + 2*b,farba_y + 2*b)
    c.create_oval(stredna_x,farba_y+0.5*b,stredna_x+0.5*b + 1.5*b,farba_y + 1.5*b, fill = "black")
    
def tenka():
    global tenka_x
    tenka_x = 4*b
    c.create_rectangle(tenka_x,farba_y,tenka_x + 2*b,farba_y + 2*b)
    c.create_oval(tenka_x,farba_y,tenka_x + 2*b,farba_y + 2*b, fill = "black")

hruba()
stredna()
tenka()



def press(event):
    global xx
    global yy
    global kreslit, farba
    x = event.x
    y = event.y
    if y < farba_y or x < cierna_x:
        xx, yy = x, y
        kreslit = True
    else:
        kreslit = False
    if y >= farba_y:
            if x >= cervena_x:
                farba = "red"
            elif modra_x < x < cervena_x:
                farba = "blue"
            elif zelena_x < x < modra_x:
                farba = "green"
            elif cierna_x < x < zelena_x:
                farba = "black"
    

def release(event):
    global kreslit
    kreslit = False
    
    

def motion(event):
    global kreslit
    if kreslit == True:
        global xx
        global yy
        x = event.x
        y = event.y
        if y <= farba_y or x <= cierna_x:
            c.create_line(x,y,xx,yy,fill = farba)
            xx, yy = x, y
        else:
            kreslit = False
        


        
    

c.bind("<ButtonPress>",press)
c.bind("<ButtonRelease>",release)
c.bind("<Motion>",motion)
