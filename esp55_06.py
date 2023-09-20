#Programma by Pietro Di Geronimo 26 Agosto 2023
# Scrivi un programma in Python che assegnata una parola a una variabile stringa, stampi prima solo i caratteri dispari
# e poi i catteri pari
#{}
#()
#[]
#("")
#print(f"")
 #print("")
stringatest = "Alessia"
print(f"Il valore di stringatest è:  '{stringatest}'")
print(f"I caratteri con posizione dispari di stringatest sono '{stringatest[::2]}'")
print(f"I caratteri con posizione pari di stringatest sono '{stringatest[1::2]}'")
stringatest = "Federica"
print(f"Il valore di stringatest è:  '{stringatest}'")
print(f"I caratteri con posizione dispari di stringatest sono '{stringatest[::2]}'")
print(f"I caratteri con posizione pari di stringatest sono '{stringatest[1::2]}'")
stringatest = "0123456789"
print(f"Il valore di stringatest è:  '{stringatest}'")
print(f"I caratteri con posizione dispari di stringatest sono '{stringatest[::2]}'")
print(f"I caratteri con posizione pari di stringatest sono '{stringatest[1::2]}'")