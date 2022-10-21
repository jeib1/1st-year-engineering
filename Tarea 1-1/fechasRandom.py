#Nombre: Juan-B. Espinoza C
import random
from fecha import *

#fechaRandom: -> int
#Entrega fecha aleatoria correcta entre entre el 1 de enero  de 1900  y  el  31  de  diciembre  de  2020
#ej: fechaRandom() -> 26051998
#ej: fechaRandom() -> 22082001
def fechaRandom():
    D=random.randint(1,31)
    M=random.randint(1,12)
    A=random.randint(1900,2020)
    Dx=D*1000000
    Mx=M*10000
    if esFecha(Dx+Mx+A)==True: #Se verifica si efectivamente es fecha
        return Dx+Mx+A
    if esFecha(Dx+Mx+A)==False: return fechaRandom()
assert esFecha(fechaRandom())

#menorFecha: int -> 
#Escribe cual es la fecha menor de un conjunto aleatorio de N fechas
#ej: menorFecha(3) -> 2081961; 23062016; 6061906; menor 7061928
def menorFecha(N):
    assert type(N)==int and N>0
    def menoR(N, Fmenor):
        if N==1:
            a=fechaRandom()
            print(a)
            if esMenor(a,Fmenor)==True: 
                assert esFecha(a)  #Se verifica si efectivamente es fecha
                print ('menor',a)
            if esMenor(a,Fmenor)==False:
                assert esFecha(Fmenor)  #Se verifica si efectivamente es fecha
                print ('menor',Fmenor)
        if N>1:
            a=fechaRandom()
            print(a)
            if esMenor(a,Fmenor)==True:
                menoR(N-1, a)
            if esMenor(a,Fmenor)==False:
                menoR(N-1, Fmenor)  
    return menoR(N, 1012021)