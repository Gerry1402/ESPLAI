from baraja import Baraja

class mesa:
    def __init__(self):
        self.cartas = []
        self.total = []
    
    def repartir(self, numero):
        self.cartas += Baraja.repartir(numero)
        self.total=[carta for carta in self.cartas if carta not in self.total]
    
    def __repr__(self):
        return f"{self.cartas}"

Mesa=mesa()
Mesa.repartir(4)