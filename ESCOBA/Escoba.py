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

def transformar_cartas(Cartas,Baraja):
    transformadas=[]
    for carta in Cartas:
        transformadas.append([Baraja[carta][0],Baraja[carta][1]])
    return transformadas

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
    cartas= transformar_cartas(Mesa, Baraja)
    for combinacion in combinaciones(cartas):
        numeros=[]
        for carta in combinacion:
            numeros.append(carta[0])
        if sum(numeros)==15 and len(numeros)==2:
            quince=True
        elif sum(numeros)==30 and len(numeros)==4:
            treinta=True
        if treinta and quince:
            print('Escoba de mano')
            Mesa=[]
    return Mesa

def comprobar_tirada(Persona,Mesa):
    Opciones=[]
    Cartas_mano=Cartas_jugadores[Persona]
    for combinacion in combinaciones(Mesa):
        numeros_combinacion_mesa=[]
        for carta in combinacion:
            numeros_combinacion_mesa.append(Baraja[carta][0])
        if sum(numeros_combinacion_mesa)>15:
            continue
        for carta in Cartas_mano:
            c=Baraja[carta]
            if c[0]+sum(numeros_combinacion_mesa)==15:
                Opciones.append(carta+' + '+' + '.join(combinacion))
    return Opciones

#Holaa
## ESCOBA ##
Numeros=['As','2','3','4','5','6','7','Sota','Caballo','Rey']
Palos=['oro','copa','espada','basto']
Equivalencias={'As':'1','Sota':'8','Caballo':'9','Rey':'10'}
Equivalencias_inversas={}
for clave in Equivalencias.keys():
    Equivalencias_inversas[Equivalencias[clave]]=clave
Baraja, Restantes=Baraja_Cartas (Numeros, Palos,Equivalencias)
Mesa=Repartir_Mesa(Restantes,4)
print('Mesa: ',Mesa)
Mesa=comprobar_mesa(Mesa)
print('Mesa: ',Mesa)
Jugadores={'Gerard':[],'Fantasma':[], 'Casper':[], 'Fantasmilla':[]}
Cartas_jugadores=Jugadores
Orden_Tiradas=['Jugador','Fantasma','Casper','Fantasmilla']
for jugador in Cartas_jugadores.keys():
    Cartas_jugadores[jugador]=Repartir_Jugador(Restantes,3)
    print (jugador+': ',Cartas_jugadores[jugador])
#while len(Restantes)>0:
Opciones_Jugador=comprobar_tirada('Gerard',Mesa)
print(Opciones_Jugador)