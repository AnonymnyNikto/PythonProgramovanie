import tkinter
import random

x_max, y_max = 800, 600

c = tkinter.Canvas(width = x_max, height = y_max, bg = "white")
c.pack()

b = 30
kreslit = False
guma = False
gumovat = False
farba = "Black"
farba_y = y_max - 2*b
hrubka = 1

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
    c.create_oval(stredna_x+0.5*b,farba_y+0.5*b,stredna_x+1.5*b,farba_y + 1.5*b, fill = "black")
    
def tenka():
    global tenka_x
    tenka_x = 4*b
    c.create_rectangle(tenka_x,farba_y,tenka_x + 2*b,farba_y + 2*b)
    c.create_oval(tenka_x+0.75*b,farba_y+0.75*b,tenka_x + 1.25*b,farba_y + 1.25*b, fill = "black")

hruba()
stredna()
tenka()

def guma():
    global guma_x
    guma_x = 6*b
    c.create_rectangle(guma_x,farba_y,guma_x + 2*b,farba_y + 2*b)
    c.create_text(guma_x+b,farba_y+b,text = "guma")

guma()



def press(event):
    global xx
    global yy
    global kreslit, farba, hrubka, guma, gumovat
    x = event.x
    y = event.y
    xx, yy = x, y
    if guma == True:
        gumovat = True
    else:
        kreslit = True
    if y >= farba_y:
            if x >= cervena_x:
                farba = "red"
                kreslit = True
                guma = False
            elif modra_x <= x < cervena_x:
                farba = "blue"
                kreslit = True
                guma = False
            elif zelena_x <= x < modra_x:
                farba = "green"
                kreslit = True
                guma = False
            elif cierna_x <= x < zelena_x:
                farba = "black"
                kreslit = True
                guma = False
            elif stredna_x > x >= hruba_x:
                hrubka = 10
            elif tenka_x >= x > stredna_x:
                hrubka = 5
            elif guma_x >= x > tenka_x:
                hrubka = 1
            elif guma_x+2*b >= x > guma_x:
                if guma == False:
                    kreslit = False
                    guma = True
                else:
                    kreslit = True
                    guma = False

def release(event):
    global kreslit, gumovat
    kreslit = False
    gumovat = False
    
    

def motion(event):
    global kreslit, gumovat
    if kreslit == True:
        global xx
        global yy
        x = event.x
        y = event.y
        if y <= farba_y or guma_x + 2*b <= x <= cierna_x:
            c.create_line(x,y,xx,yy,fill = farba,width = hrubka)
            xx, yy = x, y
        else:
            kreslit = False
    elif gumovat == True:
        x = event.x
        y = event.y
        if y <= farba_y or guma_x + 2*b <= x <= cierna_x:
            c.create_oval(x + 2*hrubka, y + 2*hrubka, x - 2*hrubka, y - 2*hrubka, fill = "white", outline = "white")
        else:
            gumovat = False
            
        
    
        


        
    

c.bind("<ButtonPress>",press)
c.bind("<ButtonRelease>",release)
c.bind("<Motion>",motion)
