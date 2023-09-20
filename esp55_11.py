#Programma by Pietro Di Geronimo 28 Agosto 2023
# Scrivi un programma in Python che 
# 1) Inizializzi la lista x = [0, 1, 2, 3, 5, 6, 7, 8]
# 2) Crei due nuove liste contenenti ciascuna una delle due metà della lista 
# 3) Aggiungi il valore 5 alla lista contenente la prima metà
#{}
#()
#[]
#("")
#print(f"")
#print("")
x = [0, 1, 2, 3, 5, 6, 7, 8]
print(f"Il contenuto della lista x è {x}")
print(f"Il valore di int(len(x)/2) è: {int(len(x)/2)}")
nuova_lista_1 = x[:int(len(x)/2)]
nuova_lista_2 = x[int(len(x)/2):]
print(f"Il contenuto di nuova_lista_1 {nuova_lista_1}")
print(f"Il contenuto di nuova_lista_2 {nuova_lista_2}")
nuova_lista_1.append(5)
print(f"Il contenuto di nuova_lista_1 è adesso: {nuova_lista_1}")