numero_telefonico = int(input("Inserisci il tuo numero telefonico:\n"))
if numero_telefonico <1000000000 or numero_telefonico >9999999999 :
  exit("il numero inserito non è un numero telefonico da 10 cifre")
else:
  numero_telefonico = str(numero_telefonico)
  print("("+numero_telefonico[0:3]+")"+" "+numero_telefonico[3:6]+"-"+numero_telefonico[6:])