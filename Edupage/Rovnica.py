a = float(input("a = "))
b = float(input("b = "))


if a == 0 and b != 0 :
    print("Rovnica nema riesenie")
elif a == 0 and b == 0:
    print("Rovnica ma nekonecno riesenii")
else:
    x = -b/a
    print (str(x))



