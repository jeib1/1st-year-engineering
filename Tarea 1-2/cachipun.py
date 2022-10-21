#Nombre: Juan-Bastián Espinoza
from jugada import *
import random
x=int(input("Ingrese 1(piedra), 2(papel) o 3(tijeras)?"))
y=random.randint(1,3)
print("Ud jugó",jugada(x))
print("Computador jugó", jugada(y))

if jugada(x)==jugada(y): print("Empate")
elif jugada(x)=="piedra":
    if jugada(y)=="papel":
        print("Gana computador")
    if jugada(y)=="tijeras":
        print("Gana Ud")
elif jugada(x)=="papel":
    if jugada(y)=="piedra":
        print("Gana Ud")
    if jugada(y)=="tijeras":
        print("Gana computador")
elif jugada(x)=="tijeras":
    if jugada(y)=="papel":
        print("Gana Ud")
    if jugada(y)=="piedra":
        print("Gana computador")
else:
    print("Gana computador por default")