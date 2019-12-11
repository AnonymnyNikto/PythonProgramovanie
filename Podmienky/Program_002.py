import tkinter
import random

x_max, y_max = 1000, 600

c = tkinter.Canvas(width = x_max, height = y_max)
c.pack()


for _ in range(101):
    dlzka = random.randrange(10,590)
    sirka = random.randrange(10,990)
    if sirka<=500 and dlzka>300:
        farba = "green"
    elif sirka<=500 and dlzka<=300:
        farba = "yellow"
    elif sirka>500 and dlzka>300:
        farba = "red"
    elif sirka>500 and dlzka<=300:
        farba = "blue"
    c.create_line(500,300,sirka,dlzka,fill = farba)
