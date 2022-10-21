import random

alan=['alan',3.1]
chelo=['chelo',4.3]
pancho=['pancho',2.8]
juan=['juan',2.9]
edu=['edu',3.7]
ian=['ian',5]
wnes=[alan,pancho,juan,edu,ian,chelo]
k=3

def prom(team,a=0):
    for n in range(0,len(team)):
        a+=team[n][1]
    return a/len(team)

def roster(team):
    for n in range(0,len(team)):
        print(team[n][0],',','nota:',team[n][1])

def mm(wnes):
    RED=[]
    BLA=[]
    while len(RED)!=k and len(BLA)!=k:
        RED.append(wnes.pop(random.randint(0,len(wnes)-1)))
        BLA.append(wnes.pop(random.randint(0,len(wnes)-1)))
    if (prom(RED)-prom(BLA))**2<0.6:
        print('EQUIPO ROJO')
        roster(RED)
        print('Promedio:',prom(RED))
        print()
        print('EQUIPO NEGRO')
        roster(BLA)
        print('Promedio:',prom(BLA))
    else: mm(wnes)
mm(wnes)
    

    
    
