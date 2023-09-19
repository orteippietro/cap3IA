# Authors: Di Geronimo Pietro 30 August 2023
# {}
# input()
# print(f"")
# Scrivi  un programma in Python che permetta all'utente di inserire le coordinate di due punti nel piano cartesiano.
# I punti devono essere salvati all'interno di tuple.Stampare la distanza tra i due punti
print("Il punto P1 ha coordinate x1 e y1")
x = float(input("Dammi la coordinata x1 => "))
y = float(input("Dammi la coordinata y1 => "))
p1 = (x, y)
print("Il punto P2 ha coordinate x2 e y2")
x = float(input("Dammi la coordinata x2 => "))
y = float(input("Dammi la coordinata y2 => "))
p2 = (x, y)
#print(f"Valore p1(0) è: {p1(0)} type {type(p1(0))}")
distanza = ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
print(f"La distanza tra i punti P1 e P2 è: {distanza}")