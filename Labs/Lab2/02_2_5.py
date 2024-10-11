numero_matricola_1 = str(input("Inserisci il primo numero di matricola:\n"))
numero_matricola_2 = str(input("Inserisci il secondo numero di matricola:\n"))
if not ( len(numero_matricola_1) == len(numero_matricola_2) == 7 and numero_matricola_1[0:1] == numero_matricola_2[0:1] == "s") :
  exit("numero matricola sbagliato")
#if len(numero_matricola_1) != len(numero_matricola_2) != 7 or numero_matricola_1[0:1] != numero_matricola_2[0:1] != "s":
#  exit("numero matricola sbagliato")
#oppure altro metodo
#if len(numero_matricola_1) == len(numero_matricola_2) == 7 and numero_matricola_1[0:1] == numero_matricola_2[0:1] == "s":
#   pass
#else
#   exit("numero matricola sbagliato")
#poi ovviamente la parte sotto andrebbe fixata
else:
  Numero_matricola_int_1 = int(numero_matricola_1[1:])
  Numero_matricola_int_2 = int(numero_matricola_2[1:])
if Numero_matricola_int_1 > Numero_matricola_int_2 :
   print(numero_matricola_1,"\t",numero_matricola_2)
else :
   print(numero_matricola_2,"\t",numero_matricola_1)