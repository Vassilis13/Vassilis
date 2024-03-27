
# Funktion
def main():
# Ausgabe
    print('Hallo')
# Variablen
    text = "Hallo Funktion"
    print(text)
# Array (Liste)
    Liste=[1,2,3]
    print(Liste)
    verschieden_datentypen=[1, 3.15, "hallo"]
    print(verschieden_datentypen)
    Liste.append(6)
    print(Liste)
#Nur ein bestimmtes Element
    print(Liste[0])
    Liste.remove(2)
    print(Liste)
    Liste.clear()
    print (Liste)

def ausgabe():
    eingabe = input("Gebe eine Zahl ein ")
    print(eingabe)
def schleifen():
    eingabe1 = int(input("Gebe eine Zahl ein: \n"))
    eingabe2 = int(input("Gebe ein Zahl ein: \n"))
    while eingabe1 > eingabe2:
        print(eingabe1)
        eingabe1 -=1

def ifschleife():
    liste=[1,2,3,4,5]

    for x in liste:
        print("erster durchlauf" ,x)


# Schreibe eine Funktion mit einer Liste die 5 Zahlen enthält.
# Anschließend sollen die Elemente der Liste um 1 erhöht werden und die Liste soll dann ausgegeben werden

def aufgabe():
    liste=[1,2,3,4,5]
    for x in liste:
        print(liste)

#Schreibe eine Funktion die eine Zahle als Userinput annimmt und in eine Variable speichert:
#Die Zahl soll um 1 verringert werden und dann auf dem Bildschirm ausgegeben werden

def usereingabe():
    usereingabe = int(input("Gebe eine Zahl ein \n"))
    while  usereingabe > 0:
        print(usereingabe)
        usereingabe -=1

def vergleichzahlen():
    zahl1 = int(input("Erste Zahl? \n"))
    zahl2 = int(input("Zweite Zahl \n"))
    if zahl1 == zahl2:
        print("zahl ist richtig")
    if zahl1 > zahl2:
        print("zahl1 ist größer")
    if zahl1 < zahl2:
        print("zahl2 ist größer")
    a = input("weiter?")
    if a == "ja":
        vergleichzahlen()

def usereingabe():
    x = int(input("Erste Zahl? \n"))
    y = int(input("zweite Zahl? \n"))
    if x > y:
        return x
    else:
        return y
def ausgabe3(zahl: int):
    print(zahl)


#Schreibe 2 Funktionen
def list()
    in



if __name__ == '__main__':
    galgen()



