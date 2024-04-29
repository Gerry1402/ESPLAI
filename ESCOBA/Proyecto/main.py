import jugadores
from auxiliares import combinaciones, binomio_newton
from mesa import Mesa
from jugadores import Jugadores, Orden
from baraja import etiquetar

def probabilidades (Persona, Siguiente, numero_mesa):
    total=binomio_newton(40-len(Mesa.total),len(Jugadores[Siguiente].mano))
    posible= binomio_newton(40-len(Mesa.total) - 4 + sum([1 for carta in Jugadores[Persona].conocidas if carta.valor == 15 - numero_mesa]),len(Jugadores[Siguiente].mano))
    return (total-posible)/total

def comprobar_tirada(Persona):
    Jugadores[Persona].conocidas= Mesa.total+Jugadores[Persona].mano
    Opciones=[]
    for combinacion in combinaciones(Mesa.cartas):
        numeros_combinacion_mesa=sum([carta.valor for carta in combinacion])
        if numeros_combinacion_mesa>15:
            continue
        opcion = [combinacion+[carta] for carta in Jugadores[Persona].mano if carta.valor+numeros_combinacion_mesa == 15]
        Opciones += opcion
    return Opciones

def calificar_opcion(Persona, opcion):
        calificacion={'Escoba':False, 'Velo':False,'Sietes':0,'Oros':0,'Cartas':0, '4':False, '+15':False, 'Reescoba':False, 'Preparada': False}
        if len(opcion) == len(Mesa.cartas) + 1:
            calificacion['Escoba'] = True
        for carta in opcion[:-1]:
            if carta.valor == 7:
                calificacion['Sietes'] += 1
            if carta.palo == 'Oro':
                calificacion['Oros'] += 1
            if carta.valor == 7 and carta.palo == 'Oro':
                calificacion['Velo'] = True
            calificacion['Cartas'] += 1
        numero_mesa = sum([carta.valor for carta in Mesa.cartas if carta not in opcion])
        for index, persona in enumerate(Orden):
            if persona == Persona:
                i=index+1
                if i == len(Orden):
                    i=0
        if numero_mesa==4:
            calificacion['4'] = True
        elif numero_mesa>15:
            calificacion['+15'] = True
        elif 0<numero_mesa and numero_mesa<4:
            calificacion['Preparada'] = probabilidades(Persona, Orden[i], numero_mesa)
        if numero_mesa>4 and numero_mesa<15:
            calificacion['Reescoba'] = probabilidades(Persona, Orden[i], numero_mesa)
        return calificacion

def escoger_opcion_recogida(Persona):
    buenas = []
    cuatro = []
    masquince = []
    reescoba = []
    preparada = []
    sietes = []
    oros = []
    cartas = []
    for jugador in Orden:
        if jugador!= Persona:
            sietes.append(Jugadores[jugador].sietes)
            oros.append(Jugadores[jugador].oros) 
            cartas.append(Jugadores[jugador].numero_cartas)
    Sietes = 4 - sum(sietes) >= max(sietes) - Jugadores[Persona].sietes and Jugadores[Persona].sietes <= 2
    Oros = 10 - sum(oros) >= max(oros) - Jugadores[Persona].oros and Jugadores[Persona].oros <= 5
    Cartas = 40 - sum(cartas) >= max(cartas) - Jugadores[Persona].numero_cartas and Jugadores[Persona].numero_cartas <= 20
    opciones=comprobar_tirada(Persona)
    for opcion in opciones:
        calificacion = calificar_opcion(Persona, opcion)
        if Sietes and Oros and Cartas:
            Puntuacion = (calificacion['Sietes']/4 + calificacion['Oros']/10 + calificacion['Cartas']/40)/3
        elif Sietes and Oros:
            Puntuacion = (calificacion['Sietes']/4 + calificacion['Oros']/10)/2
        elif Sietes and Cartas:
            Puntuacion = (calificacion['Sietes']/4 + calificacion['Cartas']/40)/2
        elif Oros and Cartas:
            Puntuacion = (calificacion['Oros']/10 + calificacion['Cartas']/40)/2
        elif Sietes:
            Puntuacion = calificacion['Sietes']/4
        elif Oros:
            Puntuacion = calificacion['Oros']/10
        elif Cartas:
            Puntuacion = calificacion['Cartas']/40
        else:
            Puntuacion = 0
        
        if calificacion['Escoba'] or calificacion['Velo']:
            if calificacion['Escoba']:
                Puntuacion += 1
            if calificacion['Velo']:
                Puntuacion += 2
            buenas.append([opcion,Puntuacion])
        else:
            if calificacion['4']:
                cuatro.append([opcion, Puntuacion*1.2])
            if calificacion['+15']:
                masquince.append([opcion, Puntuacion])
            if calificacion['Reescoba'] != False:
                reescoba.append([opcion, Puntuacion*(1-calificacion['Reescoba'])])
            if calificacion['Preparada'] != False:
                preparada.append([opcion, Puntuacion*0.8])
    finalista=None
    puntuacion=0
    if len(buenas) > 0:
        lista=buenas
    else:
        lista= cuatro + masquince + reescoba + preparada
    for opcion in lista:
        if opcion[-1]>puntuacion:
            puntuacion=opcion[-1]
            finalista=opcion[0]
    return finalista


numero_cartas_mesa=4
numero_cartas_jugador = 3
Rondas= range(1, int((40-numero_cartas_mesa)/numero_cartas_jugador)+1)

Mesa.repartir(numero_cartas_mesa)
for ronda in Rondas:
    if ronda == Rondas[-1]:
        print ('Ronda final')
    else:
        print (f'Ronda {ronda}:')
    for jugador in Orden:
        Jugadores[jugador].recibir(numero_cartas_jugador)
    for jugador in Orden:
        print ('Cartas de la mesa: ',etiquetar(Mesa.cartas))
        print (f'Cartas {jugador}: ', etiquetar(Jugadores[jugador].mano))
        print (escoger_opcion_recogida(jugador))
        if input('Continuar con la partida? [s/n]: ') == 'n':
            quit()