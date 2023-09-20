# Authors: Di Geronimo Pietro 30 Agosto 2023
# Scrivi un programma in Python che permetta all'utente di inserire due numeri qualsiasi.
# uCrea un dizionario in cui salvi la media aritmetica e la media geometrica.
# Stampare il dizionario
#{}
#()
#[]
#("")
#print(f"")
#print("")
num1 = float(input("Inserisci num1 => "))
num2 = float(input("Inserisci num2 => "))
mediaa = (num1+num2)/2
mediag = (num1*num2)**0.5
dizionario = {"num1":num1, "num2":num2, "mediaa":mediaa, "mediag":mediag}
print(f"Il mum1 inserito  è: {dizionario['num1']}")
print(f"Il mum2 inserito  è: {dizionario['num2']}")
print(f"La media aritmetica dei numeri inseriti è: {dizionario['mediaa']}")
print(f"La media geometrica dei numeri inseriti è: {dizionario['mediag']}")
print(f"Il dizionario richiesto è: {dizionario}")