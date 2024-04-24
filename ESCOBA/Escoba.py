import numpy
from itertools import chain, combinations
import sys

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

def Repartir_Mesa(Restantes,Numero_Mesa):
    Mesa=numpy.random.choice(Restantes, Numero_Mesa, False)
    for carta in Mesa:
        Restantes.remove(carta)
        numero=carta.split(' ')[0]
        for jugador in Orden_Tiradas_Jugadores:
            Jugadores[jugador]['Conocidas'][numero]+=1
    return Mesa

def Repartir_Jugador(Restantes,Numero_Jugador):
    Jugador=numpy.random.choice(Restantes, Numero_Jugador, False)
    for carta in Jugador:
        Restantes.remove(carta)
        numero=carta.split(' ')[0]
        Jugadores[jugador]['Conocidas'][numero]+=1
    return Jugador

def comprobar_escoba_mano(Mesa):
    treinta=False
    quince=False
    for carta in Mesa[1:]:
        numero=Baraja[Mesa[0]][0]
        if numero+Baraja[carta][0]==15:
            print('Escoba de mano')
            Mesa=[]
    return Mesa

def comprobar_tirada(Persona):
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

def calificar_opciones(Opciones):
    Calificaciones={}
    numero_mesa=0
    for opcion in Opciones:
        Calificaciones[opcion]={'Escoba':False, 'Velo':False,'Sietes':0,'Oros':0,'Cartas':0, '-4':False, '+15':False}
        cartas=opcion.split(' + ')
        if len(cartas)==len(Mesa)+1:
            Calificaciones[opcion]['Escoba']=True
        if '7 de oros' in cartas:
            Calificaciones[opcion]['Velo']=True
        for carta in cartas:
            Calificaciones[opcion]['Cartas']+=1
            if '7' in carta:
                Calificaciones[opcion]['Sietes']+=1
            if 'oro' in carta:
                Calificaciones[opcion]['Oros']+=1
        for carta in Mesa:  # Comprueba el numero que se dejaria en la mesa
            if carta not in cartas:
                numero_mesa+=Baraja[carta][0]
        if numero_mesa==4:
            Calificaciones[opcion]['-4']=True
        elif numero_mesa>15:
            Calificaciones[opcion]['+15']=True
        if numero_mesa==4 or numero_mesa>15:
            if str(15-numero_mesa) in Equivalencias:
                numero=Equivalencias[str(15-numero_mesa)]
            else:
                numero=str(15-numero_mesa)
            print (numero)
            Calificaciones[opcion]['Reescoba']=4-Jugadores[jugador]['Conocidas'][numero]
    return Calificaciones

Numeros=['As','2','3','4','5','6','7','Sota','Caballo','Rey']
Palos=['oro','copa','espada','basto']
Numero_cartas_jugador=3
Numero_cartas_mesa=4
Orden_Tiradas_Jugadores=['Gerard','Fantasma','Casper','Fantasmilla'] # Orden de las tiradas (El ultimo es el repartidor)
Jugadores={}
for jugador in Orden_Tiradas_Jugadores:
    Jugadores[jugador]={}
    Jugadores[jugador]['Conocidas']={}
    Jugadores[jugador]['Contador']={}
    Jugadores[jugador]['Contador']['Escoba']=0
    Jugadores[jugador]['Contador']['Velo']=False
    Jugadores[jugador]['Contador']['Sietes']=0
    Jugadores[jugador]['Contador']['Oros']=0
    Jugadores[jugador]['Contador']['Cartas']=0
    for numero in Numeros:
        Jugadores[jugador]['Conocidas'][numero]=0
    print (jugador, Jugadores[jugador]['Conocidas'])

Equivalencias={} # Equivalencias de los numeros
for i in range(len(Numeros)):
    if Numeros[i]==str(i+1):
        continue
    Equivalencias[Numeros[i]]=str(i+1)
    Equivalencias[str(i+1)]=Numeros[i]

Repartidor=Orden_Tiradas_Jugadores[-1]
Baraja, Restantes=Baraja_Cartas (Numeros, Palos,Equivalencias) # Creacion de la baraja
Mesa=Repartir_Mesa(Restantes,Numero_cartas_mesa) # Reparticion de la mesa
print('Mesa: '+', '.join(Mesa))
Mesa=comprobar_escoba_mano(Mesa) # Comprobacion de escoba de mano
print('Mesa: '+', '.join(Mesa))
Cartas_jugadores=Jugadores
Rondas=range(1,int((len(Baraja)-Numero_cartas_mesa)/(Numero_cartas_jugador*len(Jugadores))+1)) # Numero de rondas
for ronda in Rondas:
    for jugador in Cartas_jugadores.keys():
        Cartas_jugadores[jugador]=Repartir_Jugador(Restantes,Numero_cartas_jugador) # Reparticion de las cartas de cada jugador
        print (jugador+': '+', '.join(Cartas_jugadores[jugador]))
    for turno in range(1,Numero_cartas_jugador+1):
        for jugador in Orden_Tiradas_Jugadores:
            Opciones_Recoger_Jugador=comprobar_tirada(jugador)
            Valor_opciones_jugador=calificar_opciones(Opciones_Recoger_Jugador)
            for valor_opcion in Valor_opciones_jugador.keys():
                print(valor_opcion, Valor_opciones_jugador[valor_opcion])
            sys.exit()

print(Opciones_Recoger_Jugador)