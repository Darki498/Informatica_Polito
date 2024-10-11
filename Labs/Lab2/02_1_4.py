newcar = float(input("Inserisci il prezzo dell'auto che vuoi acquistare:\n"))
stima_km = float(input("Inserisci la stima di km che pensi di percorrere in un anno:\n"))
fuel_price = float(input("Inserisci il costo attuale del carburante (in euro): \n"))
efficienza = float(input("Inserisci l'efficienza della macchina km/litri:\n"))
rivendita = float(input("Inserisci la stima del valore di rivendita dell'auto usata dopo 5 anni:\n"))
costo_totale = newcar + ((stima_km/efficienza)*fuel_price) - rivendita
print("Il costo totale è:\n",costo_totale)