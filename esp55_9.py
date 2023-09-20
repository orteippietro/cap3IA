#Programma by Pietro Di Geronimo 27 Agosto 2023
# Scrivi un programma in Python che dati due punti espressi come tuple:
# 1) stampa la distanza tra i due punti
# posto della terza lettera
#{}
#()
#[]
#("")
#print(f"")
#print("")

punto_1 , punto_2 = (0,0), (0,2)
print(f"Il punto_1 ha cordinate x = {punto_1[0]}, y = {punto_1[1]}")
print(f"Il punto_2 ha cordinate x = {punto_2[0]}, y = {punto_2[1]}")
distanza = ((punto_2[0]-punto_1[0])**2+(punto_2[1]-punto_1[1])**2)**0.5
print(f"La distanza tra il punto_1 e il punto_2 è: {distanza}")