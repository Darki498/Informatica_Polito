a = int(input("Inserisci un numero compreso tra 10000 e 99999:\n"))
if a <10000 :
    print("Il numero inserito non è compreso tra 10000 e 99999, riprova")
    exit
elif a >99999 :
    print("Il numero inserito non è compreso tra 10000 e 99999, riprova")
    exit
else :
  print(str(a)[0:1])
  print(str(a)[1:2])
  print(str(a)[2:3])
  print(str(a)[3:4])
  print(str(a)[4:5])