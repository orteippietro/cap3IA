#Programma by Pietro Di Geronimo 26 Agosto 2023
# Scrivi un programma in Python in cui:
# 1) Inizializzi 2 variabili "prima" e "seconda" con dei valori diversi a tua scelta
# 2) Stampi i valori delle variabili usando una sola f-string
# 3) Scambi i valori delle due variabili
# 4) Stampi i nuovi valori delle variabili usando una sola f-string
#{}
#()
#[]
#("")
#print(f"")
#print("")
prima = "Alessia"
seconda = "Federica"
print(f"Attualmente i valori di prima e seconda sono rispettivamente {prima} , {seconda}")
prima, seconda = seconda, prima
print(f"Adesso i valori di prima e seconda sono rispettivamente {prima} , {seconda}")