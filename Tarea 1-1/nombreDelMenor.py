#Nombre: Juan-B. Espinoza C
from fecha import *

#nombreDelMenor:
#Crea un dialogo donde se recojen fechas de nacimiento y nombres, calcula la edad e indica c

def nombreDelMenor():
    j='J' #nombre '0' para mandar la funcion 
    def nombremenor(j,f0):
        a=str(input('nombre?'))
    
        if a=='fin':
            print('fin de los datos')
        else:
            f=int(input('Fecha de nacimiento(DDMMAAAA)?'))
            if esFecha(f)==False or esMenor(6102020,f)==True or f==6102020: # f0=6102020 se tomara este valor como 'maximo' para las fechas
                print('fecha incorrecta'); nombremenor(j,f0)
    
            else:
                print()
                print('edad:',añosTranscurridos(f,6102020))    #Edad al 6 de octubre de 2020
                if f0==6102020:
                    print('nombre del menor:', a,', fecha de nacimiento del menor:', f)
                    nombremenor(a,f)
                elif esMenor(f,f0)==True:
                    print()
                    print('nombre del menor:', j ,'fecha de nacimiento del menor:', f0)
                    nombremenor(j,f0)
                elif esMenor(f,f0)==False:
                    print()
                    print('nombre del menor:', a,', fecha de nacimiento del menor:', f)
                    nombremenor(a,f)      
    nombremenor(j,6102020)         