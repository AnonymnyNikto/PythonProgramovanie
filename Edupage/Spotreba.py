spotreba = float(input("Spotreba: "))
cena = float(input("Cena paliva: "))
v = float(input("Vzdialenost: "))

palivo = v * (spotreba/100)
cena = str(palivo * cena)

print("Cesta ta bude stat " + cena + "€")
