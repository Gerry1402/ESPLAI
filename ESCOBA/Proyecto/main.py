import jugadores
from auxiliares import combinaciones
from mesa import Mesa
from jugadores import Jugadores
from jugadores import Orden
from baraja import etiquetar
from math import factorial

def binomio_newton(x, y):
    if y == 1 or y == x:
        return 1
    elif y > x:
        return 0
    else:
        a = factorial(x)
        b = factorial(y)
        div = a // (b * factorial(x - y))
        return div

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

def calificar_opciones(Persona):
    calificaciones =[]
    Opciones=comprobar_tirada(Persona)
    for opcion in Opciones:
        calificaciones.append({'Escoba':False, 'Velo':False,'Sietes':0,'Oros':0,'Cartas':0, '-4':False, '+15':False})
        if len(opcion) == len(Mesa.cartas) + 1:
            calificaciones[-1]['Escoba'] = True
        for carta in opcion[:-1]:
            if carta.valor == 7:
                calificaciones[-1]['Sietes'] += 1
            if carta.palo == 'Oro':
                calificaciones[-1]['Oros'] += 1
            if carta.valor == 7 and carta.palo == 'Oro':
                calificaciones[-1]['Velo'] = True
            calificaciones[-1]['Cartas'] += 1
        numero_mesa = sum([carta.valor for carta in Mesa.cartas if carta not in opcion])
        for index, persona in enumerate(Orden):
            if persona == Persona:
                i=index+1
                if i == len(Orden):
                    i=0
        if numero_mesa==4:
            calificaciones[-1]['-4'] = True
        elif numero_mesa>15:
            calificaciones[-1]['+15'] = True
        elif 0<numero_mesa and numero_mesa<4:
            calificaciones[-1]['Preparada'] = probabilidades(Persona, Orden[i], numero_mesa)
        if numero_mesa>4 and numero_mesa<15:
            calificaciones[-1]['Reescoba'] = probabilidades(Persona, Orden[i], numero_mesa)
        print(calificaciones[-1])
    return calificaciones

def escoger_opcion(Persona):
    resultado={'Velo': [], 'Escoba': [], 'Sietes': [],'Oros': [], 'Cartas': [], '-4': [], '+15': []}
    Oros=1
    Cartas=1
    Sietes=1
    opciones=comprobar_tirada(Persona)
    calificaciones=calificar_opciones(Persona)
    for i, calificacion in enumerate(calificaciones):
        if calificacion['Velo'] == True:
            resultado['Velo'].append(opciones[i])
        if calificacion['Escoba'] == True:
            resultado['Escoba'].append(opciones[i])
        if calificacion['Sietes'] == Sietes:
            resultado['Sietes'].append(opciones[i])
        elif calificacion['Sietes'] > Sietes:
            resultado['Sietes']=[opciones[i]]
            Sietes=calificacion['Sietes']
        if calificacion['Oros'] == Oros:
            resultado['Oros'].append(opciones[i])
        elif calificacion['Oros'] > Oros:
            resultado['Oros']=[opciones[i]]
            Oros=calificacion['Oros']
        if calificacion['Cartas'] == Cartas:
            resultado['Cartas'].append(opciones[i])
        elif calificacion['Cartas'] > Cartas:
            resultado['Cartas']=[opciones[i]]
            Cartas=calificacion['Cartas']
        if calificacion['-4'] == True:
            resultado['-4'].append(opciones[i])
        if calificacion['+15'] == True:
            resultado['+15'].append(opciones[i])
    sietes = []
    oros = []
    cartas = []
    for jugador in Orden:
        if jugador!= Persona:
            sietes.append(Jugadores[jugador].sietes)
            oros.append(Jugadores[jugador].oros) 
            cartas.append(Jugadores[jugador].cartas)
    Sietes = 4 - sum(sietes) >= max(sietes) - Jugadores[Persona].sietes and Jugadores[Persona].sietes < 2
    Oros = 10 - sum(oros) >= max(oros) - Jugadores[Persona].oros and Jugadores[Persona].oros < 5
    Cartas = 40 - sum(cartas) >= max(cartas) - Jugadores[Persona].Cartas and Jugadores[Persona].Cartas < 20
    return resultado

for jugador in Orden:
    print ('Cartas de la mesa: ',etiquetar(Mesa.cartas))
    # print('Cartas en mano de '+jugador+': '+', '.join(etiquetar(Jugadores[jugador].mano)))
    # print('Cartas conocidas por '+jugador+': '+', '.join(etiquetar(Jugadores[jugador].conocidas)))
    print (f'Cartas {jugador}: ', etiquetar(Jugadores[jugador].mano))
    tiradas = escoger_opcion(jugador)
    print(tiradas)
    # print ('Opciones disponibles para recoger cartas: '+' - '.join([', '.join(etiquetar(opcion)) for opcion in tiradas]))
    try:
        Jugadores[jugador].recoger(tiradas['Cartas'][0])
    except:
        print ('No hay opciones disponibles para recoger cartas')
    print (len(Jugadores[jugador].conocidas))