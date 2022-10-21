#Nombre: Juan-B. Espinoza C
#modulo fecha

#dia: int -> int
#dia de fecha de la forma DDMMAAAA
#ej: dia(18091810) -> 18
def dia(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha//1000000
assert dia(18091810)==18

#mes: int -> int
#mes de fecha de la forma DDMMAAAA
#ej: mes(18091810) -> 9
def mes(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha//10000%100
assert mes(18091810)==9

#año: int -> int
#año de fecha de la forma DDMMAAAA
#ej: año(18091810) -> 1810
def año(fecha): 
    assert type(fecha)==int and fecha>=0
    return fecha%10000
assert año(18091810)==1810

#bisiesto: int -> bool
#True si año x es bisiesto (False si no)
#ej: bisiesto(2019) -> False (no es divisible por 4)
#ej: bisiesto(2020) -> True  (divisible por 4)
#ej: bisiesto(1900) -> False (divisible por 100)
#ej: bisiesto(2000) -> True  (divisible por 400)
def bisiesto(x):
    assert type(x)==int and x>=0
    return x%4==0 and x%100!=0 or x%400==0
assert not bisiesto(2019)
assert bisiesto(2020)
assert not bisiesto(1900)
assert bisiesto(2000)

#diasDelMes: int -> int
#Dias que tiene un mes de un respectivo año
#ej: diasDelMes(2,2020) -> 29
#ej: diasDelMes(2,2021) -> 28
#ej: diasDelMes(4,2020) -> 30
#ej: diasDelMes(1,2020) -> 31
def diasDelMes(mes,año):
     assert type(mes)==int and mes>0 and mes<13
     assert type(año)==int and año>=0
     if bisiesto(año)==True and mes==2:
         return 29
     elif mes==2: return 28
     elif mes==4 or mes==6 or mes==9 or mes==11:
         return 30
     elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
         return 31
assert diasDelMes(2,2016)==29
assert diasDelMes(2,2021)==28
assert diasDelMes(4,2020)==30
assert diasDelMes(1,2010)==31

#esFecha: int -> bool
#True si fecha pertenece a una fecha real en el calendario gregoriano de la forma DDMMAAAA, False si no lo es
#ej: esFecha(26051998) -> True
#ej: esFecha(30022020) -> False
def esFecha(fecha):
    assert type(fecha)==int and fecha>=0
    if 1<=mes(fecha)<=12 and 0<=año(fecha)<=9999 and dia(fecha)<=diasDelMes(mes(fecha),año(fecha)): 
        return True
    else: return False
assert esFecha(26051998)
assert not esFecha(30022020)

#añosTranscurridos: int int -> int
#Numero de años completos transcurridos entre dos fechas
#ej: añosTranscurridos(26051998,22082001) -> 3
#ej: añosTranscurridos(26111976,3021987) -> 10
def añosTranscurridos(fecha1,fecha2):
    assert type(fecha1)==int and fecha1>=0
    assert type(fecha2)==int and fecha2>=0
    if año(fecha1)==año(fecha2): return año(fecha1)-año(fecha2)
    if año(fecha1)>año(fecha2):
        if mes(fecha1)==mes(fecha2):
            if dia(fecha1)==dia(fecha2): return año(fecha1)-año(fecha2)
            if dia(fecha1)>dia(fecha2): return año(fecha1)-año(fecha2)
            if dia(fecha1)<dia(fecha2): return año(fecha1)-año(fecha2)-1 #Existe esta resta de 1 porque no se logra completar los 365 dias de un año
        if mes(fecha1)<mes(fecha2): return año(fecha1)-año(fecha2)-1
        if mes(fecha1)>mes(fecha2): return año(fecha1)-año(fecha2)
    if año(fecha1)<año(fecha2):
        if mes(fecha1)==mes(fecha2):
            if dia(fecha1)>dia(fecha2): return año(fecha2)-año(fecha1)-1
            if dia(fecha1)==dia(fecha2): return año(fecha2)-año(fecha1)
            if dia(fecha1)<dia(fecha2): return año(fecha2)-año(fecha1)
        if mes(fecha1)<mes(fecha2): return año(fecha2)-año(fecha1)
        if mes(fecha1)>mes(fecha2): return año(fecha2)-año(fecha1)-1
assert añosTranscurridos(26061998,22082001)==3
assert añosTranscurridos(26111976,3021987)==10

#esMenor: int int -> bool
#True si fecha1 es anterior cronologicamente a la fecha2, false si es igual o mayor.
#ej: esMenor(23092001,23092001) -> False
#ej: esMenor(7092004,28072010) -> True
#ej: esMenor(22082001,26052001) -> False
def esMenor(fecha1,fecha2):
    assert type(fecha1)==int and fecha1>=0
    assert type(fecha2)==int and fecha2>=0
    if año(fecha1)==año(fecha2):
        if mes(fecha1)==mes(fecha2):
            if dia(fecha1)==dia(fecha2): return False
            if dia(fecha1)>dia(fecha2): return False
            if dia(fecha1)<dia(fecha2): return True
        if mes(fecha1)>mes(fecha2): return False
        if mes(fecha1)<mes(fecha2): return True
    if año(fecha1)>año(fecha2): return False    
    if año(fecha1)<año(fecha2): return True 
assert not esMenor(23092001,23092001)
assert esMenor(7092004,28072010) 
assert not esMenor(22082001,26052001)