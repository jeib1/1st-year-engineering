from AB import *
A=AB(4, \
  AB(2,AB(1,None,None),AB(3,None,None)),\
  AB(6,AB(5,None,None),None))

#comparar: X X -> int
#-1 si x<y, 1 si x>y, 0 si x==y
#ej: comparar(4,7)->-1, comparar("hola","chao")->1
def comparar(x,y):
    if x<y: return -1
    if x>y: return 1
    return 0
assert comparar(4,7)==-1
assert comparar("hola","chao")==1

#mayor: AB(X) -> X
#mayor valor de A
#ej: mayor(A)->6, mayor(A.izq)->3, mayor(A.der)->6
def mayor(A):
    assert type(A)==AB
    if vacio(A.der): return A.valor
    return mayor(A.der)
assert mayor(A)==6
assert mayor(A.izq)==3
assert mayor(A.der)==6

#menor: AB(X) -> X
#menor valor de A
#ej: menor(A)->1, menor(A.izq)->1, menor(A.der)->5
def menor(A):
    assert type(A)==AB
    if vacio(A.izq): return A.valor
    return menor(A.izq)
assert menor(A)==1
assert menor(A.izq)==1
assert menor(A.der)==5

#esABB: AB(X) (X X->int) -> bool
#True is A es un ABB
#ej:  esABB(A)->True
#     esABB(AB(1,AB(2,None,None),AB(3,None,None))) -> False
def esABB(A,f=comparar):
    assert esAB(A)
    if vacio(A): return True
    v=A.valor; I=A.izq; D=A.der
    if vacio(I) and vacio(D): return True
    if vacio(I): return f(v,menor(D))<0 and esABB(D,f)
    if vacio(D): return f(v,mayor(I))>0 and esABB(I,f)
    return f(v,mayor(I))>0 and f(v,menor(D))<0 and esABB(I,f) and esABB(D,f)
assert esABB(A)
assert not esABB(AB(1,AB(2,None,None),AB(3,None,None)))

#buscar: X AB(X) (X X->int) -> X
#valor de A que contiene x (None si no está)
def buscar(x,A,f=comparar):
  assert esABB(A,comparar)
  def _buscar(x,A,comparar):
    if vacio(A): return None
    c=f(x,A.valor)
    if c<0: return _buscar(x,A.izq,f)
    if c>0: return _buscar(x,A.der,f)
    return A.valor
  return _buscar(x,A,f) 
assert buscar(3,A)==3
assert buscar(7,A)==None

#agregar: X AB(X) (X X -> int) -> AB(X)
#nuevo ABB igual a A pero con x
#ej: agregar(2,arbolVacio) -> AB(2,None,None)
#ej: agregar(1,AB(2,None,None)) ->
#    AB(2,AB(1,None,None),None) insertar a la izq
#ej: agregar(3,AB(2,None,None)) ->
#    AB(2,None,AB(3,None,None)) insertar a la der
#ej: agregar(2,AB(2,None,None))->AB(2,None,None) ya existía
def agregar(x,A,f=comparar):
  assert esAB(A)
  #si A esta vacío, crear nuevo árbol con x
  if vacio(A): return AB(x,None,None)
  #insertar x a la izquierda o derecha
  v=A.valor
  c=f(x,v)
  if c<0: return AB(v, agregar(x,A.izq,f), A.der)
  if c>0: return AB(v, A.izq, agregar(x,A.der,f))
  #si x ya existe, devolver el mismo arbol
  return A
assert agregar(2,arbolVacio)==AB(2,None,None)
assert agregar(1,AB(2,None,None))== \
                  AB(2,AB(1,None,None),None)
assert agregar(3,AB(2,None,None))== \
                  AB(2,None,AB(3,None,None))
assert agregar(2,AB(2,None,None))==AB(2,None,None)

#borrar: X AB(X) (X X->int) -> AB(X)
#nuevo ABB sin x
#ej: borrar(2,A)->AB(4,AB(1,None,AB(3,None,None)),AB(6,AB(5,None,None),None))
def borrar(x,A,f=comparar):
  assert esAB(A)
  if vacio(A): return arbolVacio
  v=A.valor
  c=f(x,v)
  #si x es <, borrar de árbol izquierdo
  if c<0: return AB(v,borrar(x,A.izq,f),A.der)
  #si x es >, borrar de árbol derecho
  if c>0: return AB(v,A.izq,borrar(x,A.der,f))
  #si x es igual, distinguir 3 casos
  #caso1: si árbol izquierdo vacío, devolver árbol derecho
  if vacio(A.izq): return A.der
  #caso2: si árbol derecho vacío, devolver árbol izquierdo
  if vacio(A.der): return A.izq
  #caso3: si árboles no son vacíos reemplazar x por mayor
  # del árbol izquierdo (y borrar mayor del árbol izquierdo)
  m=mayor(A.izq)  
  return AB(m,borrar(m,A.izq,f),A.der)
assert borrar(2,A)==AB(4,AB(1,None,AB(3,None,None)),AB(6,AB(5,None,None),None))
assert borrar(4,A)==AB(3,AB(2,AB(1,None,None),None),AB(6,AB(5,None,None),None))

#cambiar: X AB(X) (X X -> int) -> AB(X)
#nuevo ABB igual a A reemplazando
#ej: cambiar(2,arbolVacio) -> arbolVacio
#ej: cambiar(2,AB(2,None,None)) ->AB(2,None,None)
#ej: cambiar(3,A) -> A
def cambiar(x,A,f=comparar):
  assert esAB(A)
  if vacio(A): return arbolVacio
  v=A.valor
  c=f(x,v)
  if c<0: return AB(v, cambiar(x,A.izq,f), A.der)
  if c>0: return AB(v, A.izq, cambiar(x,A.der,f))
  return AB(x,A.izq,A.der)
assert cambiar(2,arbolVacio) == arbolVacio
assert cambiar(2,AB(2,None,None)) == AB(2,None,None)
assert cambiar(3,A) == A
    
#escribir: AB(X) (X->) ->
#escribe valores de A en orden ascendente
#ej: escribir(A) escribe 1 2 3 4 5 6
def escribir(A,print=print):
    assert esAB(A)
    if vacio(A): return
    escribir(A.izq,print)
    print(A.valor)
    escribir(A.der,print)
#escribir(A)

#leer: (->X) X (X X->int) -> AB(X)
#ABB con valores que se leen y terminan con fin
#ej: leer()->AB('b',AB('a',None,None),AB('c',None,None))
#            si se lee b c a . 
def leer(input=lambda:input('valor?'),fin='',comparar=comparar,A=arbolVacio):
    valor=input()
    if comparar(valor,fin)==0: return A
    return leer(input,fin,comparar,agregar(valor,A,comparar))
#assert leer()==AB('b',AB('a',None,None),AB('c',None,None))
#assert leer(lambda :int(input('numero?')),0)==AB(1,None,AB(2,None,None))