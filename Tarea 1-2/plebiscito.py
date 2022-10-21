#Nombre: Juan-Bastián Espinoza
from porcentaje import *
a=int(input("apruebo?"))
r=int(input("rechazo?"))
b=int(input("blanco?"))
n=int(input("nulos?"))
print()
print("resultados en porcentajes")
print("apruebo:",porcentaje(a,a+r+b+n))
print("rechazo:",porcentaje(r,a+r+b+n))
print("blancos",porcentaje(b,a+r+b+n))
print("nulos:",porcentaje(n,a+r+b+n))
print("Porcentajes sin blancos y nulos")
print("apruebo:",porcentaje(a,a+r))
print("rechazo:",porcentaje(r,a+r))

