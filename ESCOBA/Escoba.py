import numpy
from itertools import chain, combinations

def combinaciones(lista):
    s = list(lista)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def Baraja_Cartas (Numeros, Palos,Equivalencias):
    Baraja={}
    Cartas=[]
    for j in Palos:
        for i in Numeros:
            Carta=i+' de '+j+'s'
            Cartas.append(Carta)
            if i in Equivalencias:
                i=Equivalencias[i]
            Valor=[int(i),j]
            Baraja[Carta]=Valor
    return Baraja, Cartas

def transformar_numeros(Cartas,Baraja):
    numeros=[]
    palos=[]
    for carta in Cartas:
        numeros.append(Baraja[carta][0])
        palos.append(Baraja[carta][1])
    return numeros, palos

def Repartir_Mesa(Restantes,Numero_Mesa):
    Mesa=numpy.random.choice(Restantes, Numero_Mesa, False)
    for carta in Mesa:
        Restantes.remove(carta)
    return Mesa

def Repartir_Jugador(Restantes,Numero_Jugador):
    Jugador=numpy.random.choice(Restantes, Numero_Jugador, False)
    for carta in Jugador:
        Restantes.remove(carta)
    return Jugador

def comprobar_mesa(Mesa):
    treinta=False
    quince=False
    numeros, palos = transformar_numeros(Mesa, Baraja)
    for combinacion in combinaciones(numeros):
        if sum(combinacion)==15:
            quince=True
        elif sum(combinacion)==30:
            treinta=True
        if treinta and quince:
            print('Escoba de mano')
            Mesa=[]
    return Mesa

#Holaa
## ESCOBA ##
Numeros=['As','2','3','4','5','6','7','Sota','Caballo','Rey']
Palos=['oro','copa','espada','basto']
Equivalencias={'As':'1','Sota':'8','Caballo':'9','Rey':'10'}
Baraja, Restantes=Baraja_Cartas (Numeros, Palos,Equivalencias)
Mesa=Repartir_Mesa(Restantes,4)
Jugador=Repartir_Jugador(Restantes,3)
Mesa=comprobar_mesa(Mesa)
Contrincantes={'Contrincante_1':[], 'Contrincante_2':[], 'Contrincante_3':[]}
for contrincante in Contrincantes.keys():
    Contrincantes[contrincante]=Repartir_Jugador(Restantes,3)