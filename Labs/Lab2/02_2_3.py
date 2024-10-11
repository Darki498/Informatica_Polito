import math 
a = float(input("inserisci il primo numero:\n"))
b = float(input("inserisci il secondo numero:\n"))
print("Somma:\t\t\t",a+b)
print("Differenza:\t        ",a-b)
print("Prodotto:\t\t",a*b)
if (a+b) < 0:
  print("Valore medio:\t\t",-(a+b)/2)
else:
  print("Valore medio:\t\t",(a+b)/2)
if (a-b)<0:
  print("Valore assoluto:\t",-(a-b))
else:
  print("Valore assoluto:\t",a-b)
print("Numero più alto:\t",max(a,b))
print("Numero più piccolo:\t",min(a,b))