import random
from carta import Carta

tipo = ['Oro', 'Copa', 'Espada', 'Basto']
numeros = list(range(1, 11))

class mazo:
    def __init__(self):
        self.cartas = []
        self.cartas = [Carta(valor, palo) for valor in numeros for palo in tipo]

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir(self, cantidad):
        if cantidad > len(self.cartas):
            raise ValueError("No hay suficientes cartas en la baraja")
        else:
            return [self.cartas.pop() for _ in range(cantidad)]

def etiquetar(cartas):
    if isinstance(cartas, list):
        return ', '.join([str(carta) for carta in cartas])
    else:
        return str(cartas)

Baraja=mazo()
Baraja.mezclar()