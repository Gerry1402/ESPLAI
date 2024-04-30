from baraja import Baraja
from mesa import Mesa
from baraja import etiquetar

Jugadores={}

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.cartas = []
        self.conocidas = []
        self.escobas = 0
        self.oros = 0
        self.sietes = 0
        self.numero_cartas = 0
        self.velo = False
        self.ultimo = False
        self.contador = 0
    
    def conocidas(self, cartas):
        return [carta for carta in self.mano+cartas]
    
    def conocidas(self):
        return self.conocidas

    def __repr__(self) -> str:
        pass

    def recibir(self, numero):
        self.mano=Baraja.repartir(numero)
        self.conocidas+=[carta for carta in self.mano+Mesa.total if carta not in self.conocidas]

    def descartar(self, carta):
        if carta in self.mano:
            self.mano.remove(carta)
            Mesa.cartas.append(carta)
            Mesa.total.append(carta)

    def recoger(self, cartas):
        if len(cartas) == len (Mesa.cartas) + 1:
            self.escobas += 1
        for carta in cartas:
            if carta.valor == 7:
                self.sietes += 1
            if carta.palo == 'Oro':
                self.oros += 1
            if carta.valor == 7 and carta.palo == 'Oro':
                self.velo = True
            self.numero_cartas += 1
            self.cartas.append(carta)
            if carta in self.mano:
                self.mano.remove(carta)
                Mesa.total.append(carta)
            if carta in Mesa.cartas:
                Mesa.cartas.remove(carta)

    def __str__(self):
        return f" - {self.nombre} - \nCartas en mano: {etiquetar(self.mano)}\nCartas: {etiquetar(self.cartas)}\nCartas conocidas: {etiquetar(self.conocidas)}\nContador: (Escobas: {self.escobas}, Cartas: {self.numero_cartas}, Sietes: {self.sietes}, Oros: {self.oros}, Velo: {self.velo})"

numero_jugadores=int(input('Numero de jugadores (en orden): '))

for i in range(numero_jugadores):
    nombre_jugador=input('Nombre del jugador '+str(i+1)+': ')
    Jugadores[nombre_jugador]=Jugador(nombre_jugador)

Orden = list(Jugadores.keys())