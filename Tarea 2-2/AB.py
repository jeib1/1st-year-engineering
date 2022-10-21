#AB: valor(any), izq(AB), der(AB)
from estructura import crear
crear("AB","valor izq der")

A=AB(5, \
     AB(6,AB(3,None,None),AB(2,None,None)),\
     AB(1,AB(6,None,None),None))

arbolVacio=None
    
#esAB: any -> bool
#True si x es un AB
#ej: esAB(A)->True
#ej: esAB(arbolVacio)->True
def esAB(x):
  return x==arbolVacio or type(x)==AB
assert esAB(A)
assert esAB(arbolVacio)
assert not esAB(1)

#vacio: AB -> bool
#True is A es un arbol vacio
#ej: vacio(A)->False
#    vacio(arbolVacio)->True
def vacio(A):
  assert esAB(A)
  return A==arbolVacio
assert vacio(arbolVacio)
assert not vacio(A)

#valores: AB -> int
#cantidad de valores de A
#ej: valores(A) -> 6
#ej: valores(arbolVacio) -> 0
def valores(A):
  assert esAB(A)
  if vacio(A): 
    return 0
  else:
    return 1 + valores(A.izq) + valores(A.der)
assert valores(A)==6
assert valores(arbolVacio)==0

#altura: AB -> int
#numero de niveles de A
#ej: altura(A) -> 3
#ej: altura(arbolVacio) -> 0
def altura(A):
  assert esAB(A)
  if vacio(A): 
      return 0
  else:
      return 1+max(altura(A.izq),altura(A.der))
assert altura(A)==3
assert altura(arbolVacio)==0





