# Authors: Di Geronimo Pietro 30 August 2023
# {}
# input()
# print(f"")
# Scrivi  un programma in Python che permetta all'utente di inserire due numeri interi e crei la lista contenente
# 1) La somma dei quadrati dei due numeri
# 2) Il quadrato della somma dei due numeri
# 3) La differenza tra i quadrati dei due numeri
# 4) Il quadrato della differenza dei due numeri
num1 = int(input("Inserisci il primo numero => "))
num2 = int(input("Inserisci il primo numero => "))
lista = []
lista.append(num1**2+num2**2)
lista.append((num1+num2)**2)
lista.append(num1**2-num2**2)
lista.append((num1-num2)**2)
print(f"Il contenuto della lista è: {lista}")