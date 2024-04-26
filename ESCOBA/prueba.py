import random

### Crear una nueva baraja española ###

Palos = ['Oro', 'Copa', 'Espada', 'Basto']
Numeros = list(range(1, 11))
Jokers=0

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __repr__(self):
        nombres_valores = {1: "As", 8: "Sota", 9: "Caballo", 10: "Rey"}
        nombre_valor = nombres_valores.get(self.valor, str(self.valor))
        return f"{nombre_valor} de {self.palo.lower()}s"

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

    def __len__(self):
        return len(Palos)*len(Numeros)+Jokers

Baraja = baraja()
Baraja.barajar()

### Crear Jugadores ###

Jugadores = {}
Turnos=['Gerard', 'Fantasma', 'Casper', 'Fantasmilla']

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
    
    def __repr__(self) -> str:
        pass

    def recibir(self, numero):
        self.mano=Baraja.repartir(numero)
        for carta in self.mano:
            if carta not in self.conocidas:
                self.conocidas.append(carta)

    def descartar(self, carta):
        if carta in self.mano:
            self.mano.remove(carta)
            Mesa.append(carta)

    def recoger(self, cartas):
        for carta in cartas:
            if carta.valor == 7:
                self.sietes += 1
            if carta.palo == 'Oro':
                self.oros += 1
            if carta.valor == 7 and carta.palo == 'Oro':
                self.velo = True
            self.numero_cartas += 1
            if carta in self.mano:
                self.mano.remove(carta)
                self.cartas.append(carta)
            if carta in Mesa:
                Mesa.remove(carta)
                self.cartas.append(carta)

    def __str__(self):
        return f" - {self.nombre} - \nCartas en mano: {self.mano}\nCartas: {self.cartas}\nCartas conocidas: {self.cartas}\nContador: (Escobas: {self.escobas}, Cartas: {self.numero_cartas}, Sietes: {self.sietes}, Oros: {self.oros}, Velo: {self.velo})"

for jugador in Turnos:
    Jugadores[jugador]=Jugador(jugador)

print (len(Baraja.cartas))
Mesa=Baraja.repartir(4)
Jugadores['Gerard'].recibir(3)
print (Jugadores['Gerard'].mano)
Jugadores['Gerard'].descartar(Jugadores['Gerard'].mano[0])
print (Jugadores['Gerard'].mano)
print (Mesa)
Jugadores['Gerard'].recoger(Mesa[:2]+[Jugadores['Gerard'].mano[0]])
print (Jugadores['Gerard'])
print (Jugadores['Fantasma'])