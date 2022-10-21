def imprimirmatriz(): 
  print("   A  B  C  D  E  F  G  H ")
  for i in range(0,8):
    print(" ",i,M[i])
    
def conversion(Numero):
  if (Numero == 0):
    return("A")
  if (Numero == 1):
    return("B")
  if (Numero == 2):
    return("C")
  if (Numero == 3):
    return("D")
  if (Numero == 4):
    return("E")
  if (Numero == 5):
    return("F")
  if (Numero == 6):
    return("G")
  if (Numero == 7):
    return("H")
  return ""
linea=""

import random

M = [0]*8
P= [0]*8
for i in range(0,8):
  M[i]= [0]*8
  P[i]= [0]*8
n='viva pinochet'
for k in range(0,5):                        
  pos_i = random.randint(0,7)                   
  pos_j = random.randint(0,7)                  
  if (M[pos_i][pos_j]==1):                     
    while (M[pos_i][pos_j]==1):                     
      pos_i = random.randint(0,7)                       
      pos_j = random.randint(0,7)                       
  M[pos_i][pos_j]=1       

linea=""
for i in range(0,8):
    linea = linea + conversion(i) + "  "

print("      "+linea)
for i in range(0,8):
  print(" ",i,M[i])
    
intentos = 0
aciertos = 0
Y="ABCDEFGH"

while (aciertos < 5) and (intentos < 12):  

  x=int(input("INGRESE UN NUMERO DEL 0 AL 7: "))
  if  (x<0 or x >=8):
    print("ERROR: INGRESAR NUMERO DEL 0 AL 7")
    x=int(input("INGRESE UN NUMERO DEL 0 AL 7: "))

  Y=input("Ingrese una letra A - H : ")
  if Y<'A' or Y>'H':
    print("ERROR: INGRESAR NUMERO NUEVAMENTE ")
    Y=input("Ingrese una letra A - H : ")
    
  if (Y == "A"):
    y=0
    print(n)
  if (Y  == "B"):
    y=1
  if (Y  == "C"):
    y=2
  if (Y  == "D"):
    y=3
  if (Y  == "E"):
    y==4
  if (Y  == "F"):
    y=5
  if (Y  == "G"):
    y=6
  if (Y  == "H"):
    y=7

  if (M[x][y]==1):
    aciertos = aciertos + 1
    M[x][y] = 3 
  
    print("ACERTO A UN BARCO")
  elif (M[x][y]==0):
    M[x][y] = 2
    print("TIRO AL AGUA")  
  imprimirmatriz()
  intentos = intentos +1
if (aciertos == 5):
  print("Ganó: Acertó en los 2 unos en ",intentos,"intentos")
else:
  print("No Ganó: Acertó ",aciertos," en unos en ",intentos,"intentos")
