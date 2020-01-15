strana_a = input("Zadaj stranu a: ")
strana_b = input("Zadaj stranu b: ")
strana_c = input("Zadaj stranu c: ")

strana_b = float(strana_b)
strana_c = float(strana_c)
strana_a = float(strana_a)
objem = strana_a * strana_b * strana_c
povrch = 2 * (strana_a * strana_b + strana_a * strana_c + strana_c * strana_b )
objem = int(objem)
povrch = int(povrch)


print ("Objem je ", objem, " a povrch je ", povrch)
