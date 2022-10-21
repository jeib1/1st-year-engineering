#Nombre:Juan Espinoza

#esConjunto: list -> bool
#True si es conjunto (sin elementos repetidos), False si no lo es
#ej: esConjunto([1,2,3,4,5]) -> True
#ej: esConjunto([67,1,1432]) -> True
#ej: esConjunto(['A','A','X']) -> False
def esConjunto(L):    
    A=[]
    assert type(L)==list
    indices=range(len(L))
    for i in indices:
        if L.count(L[i])==1:
            A=A+[1]
        else: A=A+[0]
    if A.count(0)==0:
        return True
    else: return False
assert esConjunto([1,2,3,4,5])
assert esConjunto([67,1,1432])
assert not esConjunto(['A','A','X'])

#iguales: list list -> bool 
#True, si ambos conjuntos son iguales sin importar el orden, False si son distintos
#ej: iguales([11,33],[33,11]) -> True
#ej: iguales(['tarea','tres'],['tarea','tres']) -> True
#ej: iguales([3,1,4,5],[3,1,4]) -> False
def iguales(L,R):    
    assert esConjunto(L)
    assert esConjunto(R)
    L.sort()
    R.sort()
    return L==R
assert iguales([11,33],[33,11])
assert iguales(['tarea','tres'],['tarea','tres'])
assert not iguales([3,1,4,5],[3,1,4])

#union: list list -> list  
#Une dos conjuntos y retorna el conjunto union sin elementos repetidos
#ej: union([1,2],[1,5]) -> [1, 2, 5]
#ej: union([],[1]) -> [1]
#ej: union(['a','x','y'],['z']) -> ['a','x','y','z']
def union(L,R):   
    assert esConjunto(L)
    assert esConjunto(R)
    indices=range(len(L))
    for i in indices:
        if (L[i] in R)==True:
            R
        elif (L[i] in R)==False: R=R+[L[i]]
    assert esConjunto(R)
    R.sort()
    return R
assert union([1,2],[1,5])==[1, 2, 5]
assert union([],[1])==[1]
assert union(['a','x','y'],['z'])==['a','x','y','z']

#inter: list list -> list   
#retorna los elementos en comun de dos conjuntos
#ej: inter([4, 7, 8],[4]) -> [4]
#ej: inter(['q','w','e'],[]) -> []
#ej: inter([2001,2002,2003],[2001,2002,2003,2004]) -> [2001,2002,2003]
def inter(L,R):   
    A=[]
    assert esConjunto(L)
    assert esConjunto(R)
    indices=range(len(L))
    for i in indices:
        if (L[i] in R)==True:
            A=A+[L[i]]
        elif (L[i] in R)==False: A
    assert esConjunto(A)
    return A
assert inter([4, 7, 8],[4])==[4]
assert inter(['q','w','e'],[])==[]
assert inter([2001,2002,2003],[2001,2002,2003,2004])==[2001,2002,2003]

#resta: list list -> list
#resta los elementos de R que posee L
#ej: resta([4, 7, 8],[4]) -> [7,8]
#ej: resta(['z','x','c','v'],['u']) -> ['z','x','c','v']
#ej: resta([2001,2002,2003],[2001,2002,2003,2004]) -> []
def resta(L,R):
    A=[]
    assert esConjunto(L)
    assert esConjunto(R)
    indices=range(len(L))
    for i in indices:
        if (L[i] in inter(L,R))==True:
            A
        elif (L[i] in inter(L,R))==False: 
            A=A+[L[i]]
    assert esConjunto(A)
    return A
assert resta([4, 7, 8],[4])==[7,8]
assert resta(['z','x','c','v'],['u'])==['z','x','c','v']
assert resta([2001,2002,2003],[2001,2002,2003,2004])==[]

#pertenece: any list -> bool  
#True si x se encuentra dentro de A  
#ej: pertence([2],[[2],3]) -> True
#ej: pertenece([22,44,66],[11,22,44,66,99]) -> True
#ej: pertenece('hola',['ciao','hello','hola'])  -> True
#ej: pertenece(98,[33,66,99]) -> False
def pertenece(x,A):
    if type(x)==list:
        return x==inter(x,A)
    else: return x in A
assert pertenece(2,[2,3])
assert pertenece([22,44,66],[11,22,44,66,99])
assert pertenece('hola',['ciao','hello','hola'])    
assert not pertenece(98,[33,66,99])

#sea primos.txt un archivo de texto con los primeros 3 primos (uno por linea)

#leerConjunto: str -> list
#conjunto con líneas de archivo de nombre x        
#ej: leerConjunto('primos') -> [2,3,5]
def leerConjunto(x):
    V=[]
    A=open(x+'.txt','r')
    for linea in A:    
        if linea[len(linea)-1]=='\n':  #se agrega esta condicion ya que la ultima letra de la ultima linea se cortaba
            V=V+[linea[0:-1]]          #ej: 'juan' quedaba en la lista como 'jua' al estar al final.
        else: V=V+[linea]
    A.close()
    return V
#grabarConjunto: list str ->
#archivo de nombre x con valores de conjunto en L (uno por linea)
#ej: grabarConjunto([2,3,5,7],'primos_') -> #crea primos_.txt con 2, 3, 5 y 7 en lineas distintas 
def grabarConjunto(L,x):
    A=open(x+'.txt','w')
    indices=range(len(L))
    for i in indices:  
        A.write(str(L[i])+'\n')    
        