#Programma by Pietro Di Geronimo 27 Agosto 2023
# Scrivi un programma in Python nel quale assegni alla variabile lista_voti una lista con tytti i tuoi voti 
# (almeno 6 voti) e stampi:
# 1) La lista senza il primo e l'ultimo voto 
# 2) Sostituire il quarto voto con un 10
# 3) Stampare i primi 3 voti della lista
#{}
#()
#[]
#("")
#print(f"")
#print("")
lista_voti = [0,1,2,3,4,5,6,7,8,9]
print(f"I valori iniziali di lista_voti sono: {lista_voti}")
print(f"La lista senza il primo e l'ultimo voto è: {lista_voti[1:-1]}")
lista_voti[3] = 10
print(f"I valori di lista_voti sono adesso: {lista_voti}")
print(f"I primi tre voti della lista sono: {lista_voti[:3]}")