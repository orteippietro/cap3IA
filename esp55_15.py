# Authors: Di Geronimo Pietro 30 August 2023
# {}
# input()
# print(f"")
# Scrivi  un programma in Python che permetta all'utente di inserire il suo nome e stampi il nome in cui tutti i
# caratteri tranne il primo sono sostituiti da *
name = input("Dimmi il tuo nome => ")
print(f"La stampa richiesta è: {name[0]+'*'*(len(name)-1)}")