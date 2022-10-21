from ABB import *

def enABB(x,A):
    assert esAB(A)
    if vacio(A): return False
    if x<A.valor: return enABB(x,A.izq)
    if x>A.valor: return enABB(x,A.der)
    return True
  
def insertar(x,A):
  assert esAB(A)
  #si A esta vacío, crear nuevo árbol con x
  if vacio(A): return AB(x,None,None)
  #insertar x a la izquierda o derecha
  v=A.valor
  if x<v: return AB(v, insertar(x,A.izq), A.der)
  if x>v: return AB(v, A.izq, insertar(x,A.der))
  #si x ya existe, devolver el mismo arbol
  return A

#esConjunto: AB -> bool 
#True si el arbol es un conjunto, False si no 
#ej:AB(2,AB(1,None,None),AB(3,None,None))-> True
#ej:=AB(4,AB(2,AB(7,None,None),AB(3,None,None)),AB(6,AB(5,None,None),None))->False
def esConjunto(x):
    assert esAB(x)
    return esABB(x)
assert esConjunto(AB(2,AB(1,None,None),AB(3,None,None)))
assert not esConjunto(AB(4,AB(2,AB(7,None,None),AB(3,None,None)),AB(6,AB(5,None,None),None)))

#sonIguales: AB AB -> AB
#True si los conjuntos contienen los mismos elementos,False si no
#ej:sonIguales(AB(2,AB(1,None,None),AB(3,None,None)),AB(3,AB(2,AB(1,None,None),None),None))->True
#ej:sonIguales(AB(2,AB(1,None,None),AB(7,None,None)),AB(1,None,AB(2,None,AB(3,None,None))))->False
def sonIguales(x, y):
    s1 = []
    s2 = []
    def guardar(a, sset):
        if (a == None):return
        guardar(a.izq, sset)
        sset.append(a.valor)
        guardar(a.der, sset)
    def _sonIguales(x,y):
        guardar(x, s1)
        guardar(y, s2)
        s1.sort()
        s2.sort()
    _sonIguales(x,y)
    return s1 == s2
assert sonIguales(AB(2,AB(1,None,None),AB(3,None,None)),AB(3,AB(2,AB(1,None,None),None),None))
assert sonIguales(AB(2,AB(1,None,None),AB(3,None,None)),AB(1,None,AB(2,None,AB(3,None,None))))  
assert sonIguales (AB(3,AB(2,AB(1,None,None),None),None),AB(1,None,AB(2,None,AB(3,None,None))))
assert not sonIguales(None,AB(3,AB(2,AB(1,None,None),None),None))  
assert not sonIguales(AB(2,AB(1,None,None),AB(3,None,None)),None) 
assert not sonIguales(AB(2,AB(1,None,None),AB(7,None,None)),AB(1,None,AB(2,None,AB(3,None,None))))

#union: AB AB -> AB
#une los dos conjuntos
#ej:union(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(5,None,None)))->\
    #AB(2,AB(1,None,None),AB(3,None,AB(5,None,None)))
#ej: union(AB(2,AB(1,None,None),AB(7,None,None)),AB(2,AB(1,None,None),AB(3,None,None)))==\
    #AB(2,AB(1,None,None),AB(7,AB(3,None,None),None))
def union(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(y): return x
    if vacio(x): return y
    if enABB(y.valor,x)==True: return union(x,y.izq) and union(x,y.der)
    if enABB(y.valor,x)==False: return  union(union(insertar(y.valor,x),y.izq),y.der)    
assert union(AB(2,AB(1,None,None),AB(7,None,None)),AB(2,AB(1,None,None),AB(4,None,None)))==\
    AB(valor=2, izq=AB(valor=1, izq=None, der=None), der=AB(valor=7, izq=AB(valor=4, izq=None, der=None), der=None))
assert union(AB(2,AB(1,None,None),AB(7,None,None)),AB(2,AB(1,None,None),AB(3,None,None)))==\
    AB(valor=2, izq=AB(valor=1, izq=None, der=None), der=AB(valor=7, izq=AB(valor=3, izq=None, der=None), der=None))
assert union(AB(4,AB(1,None,None),AB(7,None,None)),AB(5,AB(1,None,None),AB(8,None,None)))==\
     AB(valor=4, izq=AB(valor=1, izq=None, der=None), der=AB(valor=7, izq=AB(valor=5, izq=None, der=None), der=AB(valor=8, izq=None, der=None)))

#inter: AB AB -> AB
#intersecta los dos conjuntos 
#ej:inter(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(5,None,None)))->
    #AB(valor=2, izq=AB(valor=1, izq=None, der=None), der=None)
#ej:inter(AB(2,AB(1,None,None),AB(7,None,None)),AB(5,AB(1,None,None),AB(7,None,None)))->\
    #AB(valor=7, izq=AB(valor=1, izq=None, der=None), der=None)
def inter(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(x): return x
    if vacio(y): return y 
    if enABB(y.valor,x)==True: return AB(y.valor,inter(x,y.izq),inter(x,y.der))
    if enABB(y.valor,x)==False: return union(inter(x,y.izq),inter(x,y.der))
assert inter(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(5,None,None)))==\
    AB(valor=2, izq=AB(valor=1, izq=None, der=None), der=None)


   

#resta: AB AB -> AB
#resta los elementos de los dos conjuntos
#ej:resta(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(5,None,None)))->\
   # AB(valor=3, izq=None, der=None)
#ej:resta(AB(2,AB(1,None,None),AB(7,None,None)),AB(5,AB(1,None,None),AB(7,None,None)))->\
    # AB(valor=2, izq=None, der=None)
def resta(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(x): return x
    if vacio(y): return x
    if enABB(x.valor,y)==False: return AB(x.valor,resta(x.izq,y),resta(x.der,y))
    if enABB(x.valor,y)==True: return union(resta(x.izq,y),resta(x.der,y))  
assert resta(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(5,None,None)))==\
    AB(valor=3, izq=None, der=None)
assert resta(AB(2,AB(1,None,None),AB(7,None,None)),AB(5,AB(1,None,None),AB(7,None,None)))==\
    AB(valor=2, izq=None, der=None)

#pertenece: any AB -> bool
#True si x pertenece al conjunto y, False si no
#ej:pertenece(2,AB(2,AB(1,None,None),AB(3,None,None)))->True
#ej: pertenece(AB(5,AB(1,None,None),AB(7,None,None)),AB(2,AB(1,None,None),AB(3,None,None)))-> False
def pertenece(x,y):
    if type(x)==int:
        return enABB(x,y)
    if esAB(x)==True:
        if inter(x,y)==x:
            return True
        else: return False
assert pertenece(2,AB(2,AB(1,None,None),AB(3,None,None)))
assert not pertenece(5,AB(2,AB(1,None,None),AB(3,None,None)))
assert pertenece(AB(2,AB(1,None,None),AB(3,None,None)),AB(2,AB(1,None,None),AB(3,None,None)))
assert not pertenece(AB(5,AB(1,None,None),AB(7,None,None)),AB(2,AB(1,None,None),AB(3,None,None)))

#leer: str str -> AB
#lee valores entregados y los guarda en un arbol binario
def leer(pregunta='elemento?',fin='.',x=arbolVacio):
    valor=input(pregunta)
    if valor==fin:
        return x
    else:
        return leer(pregunta,fin,x=agregar(valor,x))

#escribir: AB-> 
#escribe los valores del arbol binario
def escribir(x):
    assert esAB(x)
    if vacio(x): return
    escribir(x.izq)
    print(x.valor)
    escribir(x.der)

def SI(A,f=enABB):
    assert esAB(A)
    if vacio(A): return True
    v=A.valor; I=A.izq; D=A.der
    if vacio(I) and vacio(D): return True
    if vacio(I): return f(v,D)==False and SI(D,f)
    if vacio(D): return f(v,I)==False and SI(I,f)
    if vacio(I): return f(v,I)==True and SI(D,f)
    if vacio(D): return f(v,I)==True and SI(I,f)
    return f(v,I) and f(v,D) and SI(I,f) and SI(D,f)

    




