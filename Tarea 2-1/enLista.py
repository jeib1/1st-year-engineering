from lista import *
L=lista(5,lista(7,lista(4,None)))
#enLista: any lista -> bool
#True si x está en L
#ej: enLista(7,L)->True, enLista(6,L)->False,
#    enLista(7,listaVacia)->False
def enLista(x,L):
    assert esLista(L)
    if vacia(L):
        return False
    elif cabeza(L)==x:
        return True
    else:
        return enLista(x,cola(L))
assert enLista(7,L)
assert not enLista(6,L)
assert not enLista(7,listaVacia)

def enLista(x,L):
    assert esLista(L)
    if vacia(L): return False
    if cabeza(L)==x: return True
    return enLista(x,cola(L))
assert enLista(7,L)
assert not enLista(6,L)
assert not enLista(7,listaVacia)

def enLista(x,L):
    assert esLista(L)
    if vacia(L): return False
    return cabeza(L)==x or enLista(x,cola(L))
assert enLista(7,L)
assert not enLista(6,L)
assert not enLista(7,listaVacia)

def enLista(x,L):
    assert esLista(L)
    return not vacia(L) and (cabeza(L)==x or enLista(x,cola(L)))
assert enLista(7,L)
assert not enLista(6,L)
assert not enLista(7,listaVacia)