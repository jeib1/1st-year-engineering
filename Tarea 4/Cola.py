#Nombre: Juan-Bastian Espinoza
#__c: list
class Cola:
    #__init__:  -> Cola
    #crea objeto de clase Cola
    #devuelve referencia
    #ej: c=Cola(n=3) -> referencia a objeto de clase Cola de n elementos como maximo
    def __init__(self,n):
        self.__c=[]
        self.__n=n
        
    #poner: any ->
    #agrega x a la Cola referenciada por self
    #ej: c.poner(1)
    #ej: c.poner(2)
    #ej: c.poner(3)
    def poner(self,x):
        assert not(self.llena())
        self.__c += [x]
    
            
    #sacar: -> any
    #extrae y entrega el primer valor de la cola (si es que hay un valor)
    #ej: c.sacar() -> 1
    def sacar(self):
        A=self.__c[0]
        self.__c=self.__c[1:len(self.__c)]
        return A
    
    #valores: -> str
    #entrega string con los valores de la cola separados por espacios    
    #ej: c.valores() -> '2 3'
    def valores(self):
        A=''
        for i in range(len(self.__c)):
            if i==len(self.__c)-1:              
                A=A+str(self.__c[i])
            else: A=A+str(self.__c[i])+' '
        return A
    
    #largo: -> int
    #entrega el numero de valores que estan en la cola
    #ej: c.largo() -> 2
    def largo(self):
        return len(self.__c)
    
    #vacia: -> bool
    #True si la cola no tiene valores
    #ej: c.vacia() -> False
    def vacia(self):
        return self.__c == []
    
    #llena: -> bool
    #True si la cola esta llena (tiene n valores dentro)
    #ej: c.llena() -> False
    def llena(self):
        return len(self.__c)==self.__n
    
class TestCola: 
  def __init__(self): 
    self.q=Cola(3)
  def test(self):
    assert self.q.vacia()
    assert self.q.largo()==0
    self.q.poner(11)
    assert not self.q.vacia()
    self.q.poner(22)
    assert not self.q.llena()
    self.q.poner(33)
    assert self.q.largo()==3
    assert self.q.llena()
    assert self.q.valores()=='11 22 33'
    assert self.q.sacar()==11
    assert self.q.largo()==2
    assert self.q.valores()=='22 33'
    assert not self.q.vacia()

t=TestCola() #crea objeto de clase TestCola 
t.test()     #prueba metodos de clase Cola

