import numpy
from itertools import chain, combinations
import random
import sys

def combinaciones(lista):
    s = list(lista)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

#####################################   CREACION DE LA BARAJA   ###############################################
Palos=['Oro','Copa','Espada','Basto']
nombres_valores = {1: "As", 8: "Sota", 9: "Caballo", 10: "Rey"}
Numeros=range(1, 11)
Jokers=0

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __repr__(self):
        nombre_valor = nombres_valores.get(self.valor, str(self.valor))
        return f"{nombre_valor} de {self.palo.lower}s"

class baraja:
    def __init__(self):
        self.cartas = []
        for palo in Palos:
            for valor in Numeros:
                self.cartas.append(Carta(valor, palo))
    
    def barajar(self):
        random.shuffle(self.cartas)
    
    def repartir(self, cantidad):
        if cantidad > len(self.cartas):
            raise ValueError("No hay suficientes cartas en la baraja")
        else:
            return [self.cartas.pop() for _ in range(cantidad)]
        
###########################################################################################################

def jugadores():
    Jugadores={}
    nombre_valor = nombres_valores.get(self.valor, str(self.valor))
    for jugador in Orden_Tiradas_Jugadores:
        Jugadores[jugador]={}
        Jugadores[jugador]['Conocidas']={}
        Jugadores[jugador]['Contador']={}
        Jugadores[jugador]['Cartas']=[]
        for contador in Contadores:
            Jugadores[jugador]['Contador'][contador]=0
        for numero in Numeros:
            Jugadores[jugador]['Conocidas'][nombres_valores.get(self.valor, str(self.valor))]=0
    return Jugadores

def comprobar_escoba_mano(Mesa):
    quince=False
    cont=Mesa[0].valor
    numero=cont
    for carta in Mesa[1:]:
        cont+=carta.valor
        if numero+carta.valor==15:
            quince=True
    if cont==30 and quince:
        return []
    return Mesa

def comprobar_tirada(Persona):
    Opciones=[]
    Cartas_mano=Jugadores[Persona]['Cartas']
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

def calificar_opciones(Persona):
    Opciones=comprobar_tirada(Persona)
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
        if numero_mesa>4 and numero_mesa<15:
            if str(15-numero_mesa) in Equivalencias:
                numero=Equivalencias[str(15-numero_mesa)]
            else:
                numero=str(15-numero_mesa)
            print (numero_mesa, numero)
            Calificaciones[opcion]['Reescoba']=4-Jugadores[jugador]['Conocidas'][numero]
    return Calificaciones

def prioridad_tirada(Persona):
    Opciones=comprobar_tirada(Persona)
    if len(Opciones)==0:
        return []
    if len(Opciones)==1:
        return Opciones[0]
    Calificaciones={}
    for opcion in Opciones:
        Calificaciones[opcion]={'Escoba':False, 'Velo':False,'Sietes':0,'Oros':0,'Cartas':0, '-4':False, '+15':False}
        cartas=opcion.split(' + ')
        if len(cartas)==len(Mesa)+1:
            Calificaciones[opcion]['Escoba']=True
        if '7 de oros' in cartas:
            Calificaciones[opcion]['Velo']=True
        for carta in cartas:
            Calificaciones[opcion]['Cartas']+=1

Orden_Tiradas_Jugadores=['Gerard','Fantasma','Casper','Fantasmilla'] # Orden de las tiradas (El ultimo es el repartidor)
Contadores=['Escoba','Velo','Sietes','Oros','Cartas'] # Contador de los elementos de la escoba
Numero_cartas_jugador=3
Numero_cartas_mesa=4
Jugadores=jugadores() # Creacion de los jugadores
Repartidor=Orden_Tiradas_Jugadores[-1]
Rondas=range(1,int((len(Baraja)-Numero_cartas_mesa)/(Numero_cartas_jugador*len(Jugadores))+1)) # Numero de rondas
Baraja=baraja().barajar()# Creacion de la baraja
print('Mesa: '+', '.join(Mesa))
print('Mesa: '+', '.join(Mesa))
Mesa=Baraja.repartir(Numero_cartas_mesa) # Reparticion de la mesa
Mesa=comprobar_escoba_mano(Mesa) # Comprobacion de escoba de mano
for ronda in Rondas:
    for jugador in Orden_Tiradas_Jugadores:
        Jugadores[jugador]['Cartas']=Baraja.repartir(Numero_cartas_jugador)
        print(jugador, Jugadores[jugador]['Cartas'])
    for turno in range(1,Numero_cartas_jugador+1):
        for jugador in Orden_Tiradas_Jugadores:
            Valor_tiradas_jugador=calificar_opciones(jugador)
            for valor_opcion in Valor_tiradas_jugador.keys():
                print(valor_opcion, Valor_tiradas_jugador[valor_opcion])
            sys.exit()

print(Opciones_Recoger_Jugador)