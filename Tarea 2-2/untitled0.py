# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:49:24 2021

@author: skate
"""

############################################################
############################################################ 

import estructura

#nodo: valor(any) izq(nodo) der(nodo)
estructura.crear('nodo', 'valor izq der')
nodoVacio = None

# obtenerValor: nodo -> int
# devuelve el numero en la raiz del arbol (que debe ser no vacio)
def obtenerValor(raiz):
    assert not vacio(raiz)
    return raiz.valor

# ramaIzq: nodo -> nodo
# devuelve subarbol izquierdo del arbol (que debe ser no vacio)
def ramaIzq(raiz):
    assert not vacio(raiz)
    return raiz.izq

# ramaDer: nodo -> nodo
# devuelve subarbol derecho del arbol (que debe ser no vacio)
def ramaDer(raiz):
    assert not vacio(raiz)
    return raiz.der

# vacio: nodo -> bool
# devuelve True si el arbol esta vacio
def vacio(raiz):
    return raiz == nodoVacio

############################################################
############################################################ 

# mapaArbol: (X -> Y) nodo(X) -> nodo(Y) 
def mapaArbol(f, raiz):
    if raiz==None:
        return nodoVacio
    else:
        return nodo((f(obtenerValor(raiz)), mapaArbol(f, ramaIzq(raiz)), mapaArbol(f, ramaDer(raiz))))


def mapa(f, raiz):
    if vacio(raiz):
        return nodoVacio
    else:
        return nodo(f(obtenerValor(raiz)), mapa(f,ramaIzq(raiz)),mapa(f,ramaIzq(raiz)))
