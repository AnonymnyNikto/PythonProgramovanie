import tkinter
import random

x_max, y_max = 800, 600
bg = input("Farba pozadia: ")

root = tkinter.Tk()
root.title("Skicar")
root.attributes("-topmost", True)

c = tkinter.Canvas(width = x_max, height = y_max, bg = bg)
c.pack()

b = 30
farba = ["red","blue","green","black"]
x = x_max - 2*b
kreslit = False
guma = False
gumovat = False
farba_kreslenia = "Black"
farba_y = y_max - 2*b
hrubka = 1




for i in range(4):
    farba_stvorca = farba[i] 
    c.create_rectangle(x,farba_y,x + 2*b,farba_y + 2*b, fill= farba_stvorca)
    x = x - 2*b
    
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

def guma_button():
    global guma_x
    guma_x = 6*b
    c.create_rectangle(guma_x,farba_y,guma_x + 2*b,farba_y + 2*b)
    c.create_text(guma_x+b,farba_y+b,text = "Guma")

def guma_vsetko():
    global guma_vsetko_x
    guma_vsetko_x = x_max - 2*b
    c.create_rectangle(guma_vsetko_x, 0, guma_vsetko_x + 2*b, 2*b)
    c.create_text(guma_vsetko_x+b,0+b, text = "Zmaz vsetko")
    

guma_button()
guma_vsetko()



def press(event):
    global kreslit, farba_kreslenia, hrubka, guma, gumovat, xpress, ypress
    x, y = event.x, event.y
    xpress, ypress = x, y
    if guma == True:
        gumovat = True
    else:
        kreslit = True
    if y >= farba_y:
            if x >= (x_max - 2*b):
                farba_kreslenia = farba[0]
                kreslit = False
                gumovat = False
            elif (x_max - 4*b) <= x < (x_max - 2*b):
                farba_kreslenia = farba[1]
                kreslit = False
                gumovat = False
            elif (x_max - 6*b) <= x < (x_max - 4*b):
                farba_kreslenia = farba[2]
                kreslit = False
                gumovat = False
            elif (x_max - 8*b) <= x < (x_max - 6*b):
                farba_kreslenia = farba[3]
                kreslit = False
                gumovat = False
            elif stredna_x > x >= hruba_x:
                hrubka = 10
                kreslit = False
                gumovat = False
            elif tenka_x >= x > stredna_x:
                hrubka = 5
                kreslit = False
                gumovat = False
            elif guma_x >= x > tenka_x:
                hrubka = 1
                kreslit = False
                gumovat = False
            elif guma_x+2*b >= x > guma_x:
                if guma == False:
                    kreslit = False
                    guma = True
                else:
                    kreslit = True
                    guma = False
    if y <= 2*b and x >= guma_vsetko_x :
        c.delete("all")
        x = x_max - 2*b
        for i in range(4):
            farba_stvorca = farba[i] 
            c.create_rectangle(x,farba_y,x + 2*b,farba_y + 2*b, fill= farba_stvorca)
            x = x - 2*b
        hruba()
        stredna()
        tenka()
        guma_button()
        guma_vsetko()
        kreslit = False
        gumovat = False

def release(event):
    global kreslit, gumovat
    kreslit = False
    gumovat = False
    
    

def motion(event):
    global kreslit, gumovat, xpress, ypress
    if kreslit == True:
        x, y = event.x, event.y
        if y <= farba_y or guma_x + 2*b <= x <= x_max - 8*b:
            if not (y <= 2*b and x >= guma_vsetko_x): 
                c.create_line(x, y, xpress, ypress ,fill = farba_kreslenia, width = hrubka)
                xpress, ypress = x, y
            else:
                kreslit = False
    elif gumovat == True:
        x, y = event.x, event.y
        if y <= farba_y - 2*hrubka or guma_x + 2*b + 2*hrubka <= x <= x_max - 8*b - 2*hrubka:
            c.create_oval(x + 2*hrubka, y + 2*hrubka, x - 2*hrubka, y - 2*hrubka, fill = bg, outline = bg)
        else:
            gumovat = False

            
    
    
c.bind("<ButtonPress>",press)
c.bind("<ButtonRelease>",release)
c.bind("<Motion>",motion)
