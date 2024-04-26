import random

# Crear una nueva baraja española

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

# Crear una nueva baraja española
Baraja = baraja()

# Barajar las cartas
Baraja.barajar()

Mesa=Baraja.repartir(4)

### Crear Jugadores ###

Jugadores = {}
Turnos=['Gerard', 'Fantasma', 'Casper', 'Fantasmilla']
for jugador in Turnos:
    Jugadores[jugador]=0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.cartas = []
        self.por = []
        self.escobas = 0
        self.oros = 0
        self.sietes = 0
        self.numero_cartas = 0
        self.velo = False
    
    def __repr__(self) -> str:
        pass

    def recibir_cartas(self, numero):
        self.mano=Baraja.repartir(numero)
        for carta in self.mano:
            if carta not in self.cartas:
                self.cartas.append(carta)
                self.conocidas.append(carta)

    def descartar_carta(self, carta):
        if carta in self.mano:
            self.mano.remove(carta)
            Mesa.append(carta)
            for jugador in Jugadores.keys():
                if carta not in Jugadores[jugador].conocidas:
                    Jugadores[jugador].conocidas.append(carta)

    def recoger_cartas(self, cartas):
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
            for jugador in Jugadores.keys():
                if carta not in Jugadores[jugador].conocidas:
                    Jugadores[jugador].conocidas.append(carta)

    def __str__(self):
        return f" - {self.nombre} - \nCartas en mano: {self.mano}\nCartas: {self.cartas}\nCartas conocidas: {self.cartas}\nContador: (Escobas: {self.escobas}, Cartas: {self.numero_cartas}, Sietes: {self.sietes}, Oros: {self.oros}, Velo: {self.velo})"

for jugador in Turnos:
    Jugadores[jugador]=Jugador(jugador)

print (len(Baraja))
Jugadores['Gerard'].recibir_cartas(3)
print (Jugadores['Gerard'].mano)
Jugadores['Gerard'].descartar_carta(Jugadores['Gerard'].mano[0])
print (Jugadores['Gerard'].mano)
print (Mesa)
Jugadores['Gerard'].recoger_cartas(Mesa[:2]+[Jugadores['Gerard'].mano[0]])
print (Jugadores['Gerard'])
print (Jugadores['Fantasma'])