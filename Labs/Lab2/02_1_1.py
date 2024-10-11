import math 
a = float(input("inserisci il primo numero:\n"))
b = float(input("inserisci il secondo numero:\n"))
print("La somma dei due numeri inseriti è:")
print(a+b)
print("La differenza tra i due numeri inseriti è:")
print(a-b)
print("il prodotto tra i due numeri inseriti è:")
print(a*b)
print("Il valore medio tra i due numeri inseriti è:")
if (a+b) < 0:
  print(-(a+b)/2)
else:
  print((a+b)/2)
print("Il valore assoluto della differenza tra i due numeri inseriti è:")
if (a-b)<0:
  print(-(a-b))
else:
  print(a-b)
print("Il numero più grande è:")
print(max(a,b))
print("Il numero più piccolo è:")
print(min(a,b))