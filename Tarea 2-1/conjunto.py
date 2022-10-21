#Nombres: Juan Espinoza, Camila Fuentes
from lista import *

#enLista: any lista -> bool
#True si x está en L
#ej: enLista(7,lista(5,lista(7,lista(4,None))))->True, enLista(6,lista(5,lista(7,lista(4,None))))->False,
#    enLista(7,listaVacia)->False
def enLista(x,L):  #Funcion auxiliar (se ocupara mas adelante)
    assert esLista(L)
    if vacia(L):
        return False
    elif cabeza(L)==x:
        return True
    else:
        return enLista(x,cola(L))
assert enLista(7,lista(5,lista(7,lista(4,None))))
assert not enLista(6,lista(5,lista(7,lista(4,None))))
assert not enLista(7,listaVacia)

#agregaAlFinal: num lista -> lista
#lista con valores de L y x al final
#ej: agregarAlFinal(1,listaVacia)==lista(1,None)
#ej: agregarAlfinal(3,lista(1,lista(2,None)))==lista(1,lista(2,lista(3,None)))   
def agregarAlFinal(x,L): #Funcion auxiliar (se ocupara mas adelante)
  if vacia(L):
    return lista(x,None)
  else:
    return lista(cabeza(L),agregarAlFinal(x,cola(L)))
assert agregarAlFinal(1,listaVacia)==lista(1,None)
assert agregarAlFinal(3,lista(1,lista(2,None)))==lista(1,lista(2,lista(3,None)))

       
#esConjunto: lista -> bool 
#True si x es un conjunto 
#ej: esConjunto(lista(2,lista(3,lista(1,None))))->True
#ej: esConjunto(lista(2,lista(5,lista(2,None))))->False
def esConjunto(L):
    assert esLista(L)
    if vacia(L): return True
    if enLista(cabeza(L),cola(L))==True: return False
    if enLista(cabeza(L),cola(L))==False: return esConjunto(cola(L))
assert not esConjunto(lista(2,lista(5,lista(2,None))))
assert  esConjunto(lista(2,lista(3,lista(1,None))))
    
#union: lista lista -> lista
#Entrega valores que estan en cada conjunto sin repetirse 
#ej:union(lista(2,lista(9,None))),(lista(2,lista(3,None))))-> lista(2,lista(9,lista(3,None)))
#ej:union(lista(2,lista(5,lista(7,None))),(lista(2,lista(5,None))))->lista(2,lista(5,lista(7,None)))
def union(x,y):
    if vacia(y): 
        return x
    if enLista(cabeza(y),x)==True: 
        return union(x,cola(y))
    if enLista(cabeza(y),x)==False:
        return union(agregarAlFinal(cabeza(y),x),cola(y))
assert union(lista(2,lista(5,lista(7,None))),(lista(2,lista(5,None))))==\
       lista(valor=2, siguiente=lista(valor=5, siguiente=lista(valor=7, siguiente=None)))
assert union(lista(2,lista(9,None)),(lista(2,lista(3,None))))==\
       lista(valor=2, siguiente=lista(valor=9, siguiente=lista(valor=3, siguiente=None)))
 
#inter lista lista -> lista
#todos los valores que estan en x y en y a la vez
#ej: inter(lista(2,lista(5,lista(7,None))),lista(2,lista(5,None)))-> lista(2,lista(5,None))
#ej: inter(lista(1,lista(5,None)),lista(1,None))-> lista(1,None) 
def inter(x,y):
    if vacia(x) or vacia(y):
        return y
    if enLista(cabeza(y),x)==False:
        return inter(x,cola(y))
    if enLista(cabeza(y),x)==True: 
        return lista(cabeza(y),inter(x,cola(y)))
assert inter(lista(2,lista(5,lista(7,None))),lista(2,lista(5,None)))==\
    lista(valor=2, siguiente=lista(valor=5, siguiente=None))
assert inter(lista(1,lista(5,None)),lista(1,None))==\
    lista(valor=1, siguiente=None)
    
#resta: lista lista-> lista
#quita los elementos de x que se encuentran tambien en y    
#ej: resta(lista(7,lista(1,None)),lista(1,None)) -> lista(7,None)
#ej: resta(lista(3,lista(2,None)),lista(1,lista(7,None))) -> lista(3,lista(2,None))
#ej: resta(lista('a',lista('b',None)),lista('b',lista('c',None))) -> lista('a',None)
def resta(x,y):
    assert esLista(x) 
    assert esLista(y)
    if vacia(x) or vacia(y): return x
    if enLista(cabeza(x),inter(x,y))==True:
        return resta(cola(x),y)
    if enLista(cabeza(x),inter(x,y))==False:
        return lista(cabeza(x),resta(cola(x),y))
assert resta(lista(7,lista(1,None)),lista(1,None))==lista(7,None)
assert resta(lista(3,lista(2,None)),lista(1,lista(7,None)))==lista(3,lista(2,None))
assert resta(lista('a',lista('b',None)),lista('b',lista('c',None)))==lista('a',None)
    
#pertenece: any lista-> bool
#True si x pertenece a y, False si no pertenece
#ej pertenece(lista(1,None),lista(7,lista(1,None))) -> True
#ej pertenece(listaVacia, lista(1, None)) -> True
#ej pertenece(lista(2,None),lista(4,lista(3,None))) -> False
def pertenece(x,y):
    if vacia(x):
        return True
    if enLista(cabeza(x),y)==False:
        return False
    if enLista(cabeza(x),y)==True:
        return pertenece(cola(x),y)
assert pertenece(lista(1,None),lista(7,lista(1,None)))==True
assert pertenece(listaVacia, lista(1, None))==True
assert pertenece(lista(2,None),lista(4,lista(3,None)))==False

#leer: str str -> list
#lee valores entregados y los guarda en una lista
def leer(pregunta='valor?',fin='.'):
    valor=input(pregunta)
    if valor==fin:
        return listaVacia
    else:
        return lista(valor,leer(pregunta,fin))
    
#escribir: lista -> 
#escribe los valores de la lista en columna
def escribir(L):
    if L!=None:
        print(cabeza(L))
        escribir(cola(L))