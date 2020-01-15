s = int(input("Pocet sekund: "))

h = s//3600
s = s - h*3600
m = s//60
s = str(s - m*60)
h = str(h)
m = str(m)

print("Cas je " + h + " hodin, " + m + " minut a " + s + " sekund")
