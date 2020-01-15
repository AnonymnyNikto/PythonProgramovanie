s = round(float(input("Vasa vyplata? ")),2)

suma = ["b500","b200","b100","b50","b20","b10","b5","b2","b1","b0.5","b0.2","b0.1","b0.05","b0.02","b0.01"]
ciastka = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
index = 0

def bankovky(suma,s,ciastka,index):
    while s != 0:
        b100 = s // ciastka[index]
        s = s - b100*ciastka[index]
        index += 1
        global s

bankovky(suma,s,ciastka,index)
print (s)
        
