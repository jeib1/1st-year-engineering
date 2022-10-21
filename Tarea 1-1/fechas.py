#Nombre: Juan-B. Espinoza C
from fecha import *
fecha1=int(input('fecha1(DDMMAAAA)?'))
fecha2=int(input('fecha2(DDMMAAAA)?'))
if esFecha(fecha1)==False or esFecha(fecha2)==False: print('fecha incorrecta')
if esFecha(fecha1)==False or esFecha(fecha2)==True:
    if esMenor(fecha1,fecha2)==True: 
        print('mayor fecha:', fecha2); print('menor fecha:', fecha1)
        print('diferencia en años',añosTranscurridos(fecha1,fecha2))
    if esMenor(fecha1,fecha2)==False: 
        print('mayor fecha:', fecha1); print('menor fecha:', fecha2)
        print('diferencia en años',añosTranscurridos(fecha1,fecha2))

