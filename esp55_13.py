# Scrivi un programma in Python in cui si inizializzi un dizionario che realizzi una rubrica telefonica.
# usa il nome come chiave del dizionario e il numero telefonico come valore.
# Stampare il numero telefonico di un elemento della rubica. 
# Aggiungere un elemento alla rubrica e stampare di nuovo la rubrica
#{}
#()
#[]
#("")
#print(f"")
#print("")

# Inizializzazione del dizionario
rubrica = {"Matteo":"095448741",
"Luca":"095441381",           
"Lucia":"095397456",
"Antonio":"0254401236"}
print(f"Attualmente rubrica ha i seguenti valori: {rubrica}")
print(f"Il numero di telefono di Matteo è: {rubrica['Matteo']}")
rubrica["Michele"] = "040555444333"
print(f"Ora rubrica ha i seguenti valori: {rubrica}")