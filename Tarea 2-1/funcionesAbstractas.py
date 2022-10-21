#modulo funcionesAbstractas
from lista import *

#mapa: lista(X) (X->Y) -> lista(Y)
#lista con f(valor1),f(valor2), . . .
#ej: mapa(lista(1,lista(2,None)),lambda x:x+1)->lista(2,lista(3,None))
def mapa(L,f):
  assert esLista(L)
  if vacia(L):
      return listaVacia
  else:
      return lista(f(cabeza(L)),mapa(cola(L),f))
assert mapa(lista(1,lista(2,None)),lambda x:x+1)==lista(2,lista(3,None))

#filtro: lista(X) (X->bool) -> lista(X)
#lista con valores de L tales que f(valor) es True
#ej: filtro(lista(1,lista(2,None)),lambda x:x>1)->lista(2,None)
def filtro(L,f):
  assert esLista(L)
  if vacia(L): 
      return listaVacia
  elif f(cabeza(L)):
    return lista(cabeza(L),filtro(cola(L),f))
  else:
    return filtro(cola(L),f)
assert filtro(lista(1,lista(2,None)),lambda x:x>1)==lista(2,None)

#reductor:lista(X) (X X->X) X -> X
#f(...f(f(valor,valor1),valor2))...)
#ej: reductor(lista(1,lista(2,None)),lambda x,y: x+y,0)->3
def reductor(L,f,valor):
  assert esLista(L)
  if vacia(L):
      return valor
  else:
      return reductor(cola(L),f,f(valor,cabeza(L)))
assert reductor(lista(1,lista(2,None)),lambda x,y: x+y,0)==3


