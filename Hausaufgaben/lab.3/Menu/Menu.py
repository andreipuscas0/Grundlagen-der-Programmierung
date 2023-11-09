import aufgabe1
import Aufgabe_2
import Aufgabe_3

def menu():

    print("[1] Aufgabe 1")
    print("[2] Aufgabe 2")
    print("[3] Aufgabe 3")
    print("[0] Exit")


option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        aufgabe1.draw()
    elif option == 2:
        Aufgabe_2.heart()
    elif option == 3:
        Aufgabe_3.twohouses()
    else:
        break