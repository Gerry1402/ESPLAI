Jugadores = {}
Equipos = {}

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.jugadores = {}
        self.nombre_jugadores = ''
        self.oros = 0
        self.sietes = 0
        self.numero_cartas = 0
        self.escobas = 0
        self.velo = False
        self.contador = 0
    
    def actualizar_puntuacion (self):
        self.oros = sum([self.jugadores[jugador].oros for jugador in self.jugadores.keys()])
        self.sietes = sum([self.jugadores[jugador].sietes for jugador in self.jugadores.keys()])
        self.numero_cartas = sum([self.jugadores[jugador].numero_cartas for jugador in self.jugadores.keys()])
        self.escobas = sum([self.jugadores[jugador].escobas for jugador in self.jugadores.keys()])
        for jugador in self.jugadores.values():
            if jugador.velo:
                self.velo = True
    
    def nombre_jugadores (self):
        return f'{', '.join(list(self.jugadores.keys())[:-1])} y {list(self.jugadores.keys())[-1]}'        

    def __str__(self):
        return f'{self.nombre}'
    
    def __repr__(self) -> str:
        return f'{self.__str__()}'

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
        self.equipo = None
    
    def conocidas(self, cartas):
        return [carta for carta in self.mano+cartas]
    
    def conocidas(self):
        return self.conocidas

    def __repr__(self) -> str:
        return f'{self.__str__()}'

    def recibir(self, numero, Baraja, Mesa):
        self.mano=Baraja.repartir(numero)
        self.conocidas+=[carta for carta in self.mano+Mesa.total if carta not in self.conocidas]

    def descartar(self, carta, Mesa):
        if carta in self.mano:
            self.mano.remove(carta)
            Mesa.cartas.append(carta)
            Mesa.total.append(carta)

    def recoger(self, cartas, Mesa):
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

    def cero(self):
        self.mano = []
        self.cartas = []
        self.conocidas = []
        self.escobas = 0
        self.oros = 0
        self.sietes = 0
        self.numero_cartas = 0
        self.velo = False
        self.ultimo = False

    def __str__(self):
        if self.equipo != None:
            return f"{self.nombre}"
        else:
            return f"{self.nombre} del equipo {self.equipo}"

numero_equipos = 0
if input('Hay equipos en el juego? [s/n]: ') == 's':
    numero_equipos = int(input('Numero de equipos: '))

while Jugadores == {}:

    numero_jugadores = int(input('Numero de jugadores: '))
    if numero_jugadores not in [2, 3, 4, 6]:
        print ('El numero de jugadores debe ser 2, 3, 4 o 6.')
        continue

    if numero_equipos != 0:
        if numero_jugadores % numero_equipos == 0 and numero_jugadores // numero_equipos > 1:
            for i in range(numero_equipos):
                nombre_equipo = input (f'Nombre del equipo {i+1}: ')
                Equipos[nombre_equipo] = Equipo(nombre_equipo)
                for n in range(numero_jugadores//numero_equipos):
                    nombre_jugador = input(f'Nombre del jugador {n+1}: ')
                    Equipos[nombre_equipo].jugadores[nombre_jugador] = Jugador(nombre_jugador)
                    Equipos[nombre_equipo].jugadores[nombre_jugador].equipo = nombre_equipo
            for i in range(numero_jugadores // numero_equipos):
                for equipo in Equipos.keys():
                    Jugadores[list(Equipos[equipo].jugadores.keys())[i]] = equipo
        else:
            if input ('El numero de jugadores debe ser mayor y múltiplo del numero de equipos. ¿Desea jugar en solitario? [s/n]: ') == 'n':
                continue
            else:
                for i in range(numero_jugadores):
                    nombre_jugador = input('Nombre del jugador '+str(i+1)+': ')
                    Jugadores[nombre_jugador] = Jugador(nombre_jugador)
    
    else:
        for i in range(numero_jugadores):
            nombre_jugador = input('Nombre del jugador '+str(i+1)+': ')
            Jugadores[nombre_jugador] = Jugador(nombre_jugador)

Orden = list(Jugadores.keys())