h = int(input("Pocet hodin: "))
m = int(input("Pocet minut: "))
s = int(input("Pocet sekund: "))

s = str(s + 60*m + 3600*h)

print("Cas v sekundach je " + s)
