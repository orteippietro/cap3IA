#Programma by Pietro Di Geronimo 27 Agosto 2023
# Scrivi un programma in Python che assegnata una parola di almeno 8 lettere a una variabile stringa, stampi tuttala parolacon un carattere ? al
# posto della terza lettera
#{}
#()
#[]
#("")
#print(f"")
#print("")
strigatest = "0123456789"
print(f"stringatest ha il seguente valore: {strigatest}")
print(f"Il risultato richesto è: {strigatest[:2]+'?'+strigatest[4:]}")