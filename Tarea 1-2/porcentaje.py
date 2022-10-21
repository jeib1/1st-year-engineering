#Nombre: Juan-Bastián Espinoza
#porcentaje: int int -> float
#porcentaje de x con respecto a y redondeado a un decimal
#ej: porcentaje(2,3)->66.7
def porcentaje(x,y):
    return (round(1000*x/y)/10)
assert porcentaje(2,3)==66.7
