import tkinter
import random

def zobraz_odpoveda(meno):
    c.create_rectangle(50,50,650,150,fill="white", width=0)
    return c.create_text(70,100,font = 'Arial 36', text="Odpovedá: " + meno, fill = "red", anchor = "w")

def stvorec(x,y,meno,farba):
    c.create_rectangle((x-1)*100+50,(y+1)*100,x*100+50,(y+2)*100,fill=farba)
    c.create_text(x*100,y*100+150,text=meno)

def najdi_ziaka(stlpec,riadok):
    a = (riadok-1)*6+(stlpec-1)
    return ziaci[a] if (0 <= a and a < len(ziaci)) else None

def zobraz_ziaka(stlpec,riadok):
    meno = najdi_ziaka(stlpec,riadok)
    if (not meno is None):
            farba = "red" if (meno in chybaju) else "gray" if (meno in odpovedali) else "white" 
            stvorec(stlpec,riadok,meno,farba)
def zobraz_triedu():
    zobraz_odpoveda(odpoveda)
    for riadok in range(1,pocet_riadkov):
        for stlpec in range(1,7):
           zobraz_ziaka(stlpec, riadok)

def chyba(event):
    riadok=event.y//100-1
    stlpec=(event.x-50)//100+1
    if (0 < stlpec and stlpec < 7 and 0 < riadok):
        meno = najdi_ziaka(stlpec,riadok)
        if (not meno is None):
            if meno in chybaju:
                chybaju.remove(meno)
            else:
                chybaju.append(meno)
            zobraz_ziaka(stlpec, riadok)
def najdi_odpovedajucich():
    global odpoveda
    odpovedajuci = ziaci.copy()
    for i in chybaju:
        if i in odpovedajuci:
            odpovedajuci.remove(i)
    for i in odpovedali:
        if i in odpovedajuci:
            odpovedajuci.remove(i)
    return odpovedajuci

def loteria(event):
    global odpovedali, odpoveda
    odpovedajuci = najdi_odpovedajucich()
    if len(odpovedajuci) == 0:
        odpovedali = []
        odpovedajuci = najdi_odpovedajucich()
    if len(odpovedajuci) > 0:
        odpoveda = random.choice(odpovedajuci)   
        odpovedali.append(odpoveda)
        open(trieda + "\\odpovede.txt", 'w').write('\n'.join(odpovedali))
        zobraz_triedu()
        c.update()

def koniec(event):
    root.destroy()

trieda = input("Ktora trieda? ")
ziaci = open(trieda + "\\ziaci.txt").read().splitlines()
odpovedali = open(trieda + "\\odpovede.txt").read().splitlines()
chybaju = []
odpoveda = ""


root = tkinter.Tk()
root.title(trieda)
root.attributes("-topmost", True)

c = tkinter.Canvas(width=1200,height=1000,bg="white")
c.pack()


pocet_riadkov = (len(ziaci)+5)//6+1
zobraz_triedu()   

c.bind("<Button-1>",chyba)
c.bind_all("<Return>",loteria)
c.bind_all("<Escape>",koniec)

tkinter.mainloop()

exit(0)
