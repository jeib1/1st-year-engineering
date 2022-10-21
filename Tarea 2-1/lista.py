#modulo lista.py
#lista: valor(any) siguiente(lista)
import estructura
estructura.crear("lista","valor siguiente")

#cabeza: lista -> any
#primer valor de una lista
#ej: cabeza(lista(1,lista(2,None)))->1
def cabeza(L):
    assert type(L)==lista
    return L.valor
assert cabeza(lista(1,lista(2,None)))==1

#cola: lista -> lista
#lista sin primer valor
#ej: cola(lista(1,lista(2,None)))->lista(2,None)
#ej: cola(lista(1,None))->None
def cola(L):
    assert type(L)==lista
    return L.siguiente
assert cola(lista(1,lista(2,None)))==lista(2,None)
assert cola(lista(1,None))==None

#escribir: lista ->
#escribe valores de L
#ej: escribir(lista(1,lista(2,None))) escribe 1 2 
def escribir(L):
    if L!=None:
        print(cabeza(L))
        escribir(cola(L))

listaVacia=None

#esLista: any -> bool
#True si L es una lista
#ej: esLista(lista(1,lista(2,None))->True
#    esLista(listaVacia)->True
#    esLista(10)->False
def esLista(L):
    return L==listaVacia or type(L)==lista
assert esLista(lista(1,lista(2,None)))
assert esLista(listaVacia)
assert not esLista(10)


#vacia: lista -> bool
#True si L es una lista vacia
#ej: vacia(lista(1,lista(2,None)))->False, 
#    vacia(listaVacia)->True
def vacia(L):
    assert esLista(L)
    return L==listaVacia
assert not vacia(lista(1,lista(2,None)))
assert vacia(listaVacia)

#largo: lista -> int
#numero de valores de lista L
#ej: largo(lista(10,lista(20,None)))->2
#    largo(listaVacia)->0
def largo(L):
  assert esLista(L)
  if vacia(L):
      return 0
  else:
      return 1 + largo(cola(L))
assert largo(lista(10,lista(20,None)))==2
assert largo(listaVacia)==0

