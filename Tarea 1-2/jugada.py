#Nombre: Juan-Bastián Espinoza
#jugada: int -> str
#'piedra','papel' o 'tijeras' si n es 1, 2 o 3 respectivamente
#ej:jugada(1)->'piedra',jugada(2)-'papel',jugada(3)->'tijeras'
def jugada(x):
    if x==1:
        return "piedra"
    elif x==2:
        return "papel"
    elif x==3:
        return "tijeras"
    else :
        return "jugada inválida"
assert jugada(1)=="piedra"
assert jugada(2)=="papel"
assert jugada(3)=="tijeras"

