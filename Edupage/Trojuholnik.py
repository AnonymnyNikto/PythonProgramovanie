x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

max_ = max(x,y,z)

if x + y + z - max_ > max_:
    if x == y == z:
        print("Trojuholnik je rovnostranny")
    elif x == y or x == z or y == z:
        print("Trojuholnik je rovnoramenny")
        if x**2 + y**2 + z**2 - max_**2 == max_**2:
            print("Trojuholnik je pravouhly")
    elif x**2 + y**2 + z**2 - max_**2 == max_**2:
        print("Trojuholnik je pravouhly")
    else:
        print("Trojuholnik je iny")
    
    
else:
    print("Trojuholnik neexistuje")
