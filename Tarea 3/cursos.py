#Nombre:Juan Espinoza

from Conjunto import *

A=leerConjunto('cursoA')
B=leerConjunto('cursoB')
C=leerConjunto('cursoC')

c=inter(B,C)
d=inter(A,C)
e=resta(union(union(A,B),C),inter(A,B))
f=resta(e,c)
g=resta(f,d)
print('Alumnos en solo 1 curso:')
grabarConjunto(g,'uncurso')
print(len(g))
print()
print('Alumnos en solo 2 cursos:')
grabarConjunto(resta(union(union(inter(A,B),inter(B,C)),inter(A,C)),inter(inter(A,B),C)),'doscursos')
print(len(resta(union(union(inter(A,B),inter(B,C)),inter(A,C)),inter(inter(A,B),C))))
print()
print('Alumnos en los 3 cursos (simultaneamente):')
grabarConjunto(inter(inter(A,B),C),'trescursos')
print(len(inter(inter(A,B),C)))
print()
print('Alumnos en algun curso:')
grabarConjunto(union(union(A,B),C),'algunCurso')
print(len(union(union(A,B),C)))