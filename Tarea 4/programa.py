#Nombre: Juan-Bastian Espinoza

from tkinter import *
from Cola import *

f=Cola(5) #cola de espera de 5 

def boton(): #para el boton 'Caja'
    if f.largo()>0: #verificar si hay clientes en la cola
        _enCaja.config(text=f.sacar()) #sacarel primer valor de la cola y mostrarlo en el Label “en Caja
        _cola.config(text=f.valores()) #mostrar el contenido de la cola
        _cupos.config(text=5-f.largo()) #mostrar el cupo actualizado
        if f.llena()==False: #mostrar el estado de la cola (“vacia” u “ok”)
            if f.vacia():
                _estadoCola.config(text="vacia")
            else: 
                _estadoCola.config(text='ok')
        
def enter(x): #para el entry 'llega'
    if not f.llena(): #verificar si hay cupos disponibles
        f.poner(_llega.get()) #agregar el cliente a la cola y mostrar el contenido de la cola
        _cola.config(text=f.valores())
        _cupos.config(text=5-f.largo()) #mostrar el cupo actualizado
        if f.llena()==False: #mostrar el estado de la cola (“ok” o “llena”)
            _estadoCola.config(text='ok')
        if f.llena()==True:
            _estadoCola.config(text='llena')
#crear ventana    
v=Tk()
#definir y diagramar marco 1
marco1=Frame(v) 
Caja=Label(marco1,text="Caja",width=10)
enCaja=Label(marco1,text="en Caja",width=8)
cola=Label(marco1,text="Cola",width=18)
cupos=Label(marco1,text="cupos",width=8)
llega=Label(marco1,text="llega")
estadoCola=Label(marco1,text="estado cola",width=13)
Caja.pack(side=LEFT)
enCaja.pack(side=LEFT)
cola.pack(side=LEFT)
cupos.pack(side=LEFT)
llega.pack(side=LEFT)
estadoCola.pack(side=LEFT)
#definir y diagramar marco 2
marco2=Frame(v)
_Caja=Button(marco2,text="atender",command=boton,width=10)
_enCaja=Label(marco2,text="",width=8)
_cola=Label(marco2,text=f.valores(),width=18)
_cupos=Label(marco2,text=5-f.largo(),width=8)
_llega=Entry(marco2,width=5)
_llega.bind("<Return>",enter)
_estadoCola=Label(marco2,text="vacia",width=13)
_Caja.pack(side=LEFT)
_enCaja.pack(side=LEFT)
_cola.pack(side=LEFT)
_cupos.pack(side=LEFT)
_llega.pack(side=LEFT)
_estadoCola.pack(side=LEFT)
#diagramar y mostar ventana
marco1.pack()
marco2.pack()
v.mainloop()