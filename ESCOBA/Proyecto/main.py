import jugadores
from auxiliares import combinaciones, binomio_newton, medio
from mesa import Mesa
from jugadores import Jugadores, Orden, numero_jugadores
from baraja import etiquetar

def probabilidades (Persona, Siguiente, numero_mesa):
    total=binomio_newton(40-len(Mesa.total),len(Jugadores[Siguiente].mano))
    posible= binomio_newton(40-len(Mesa.total) - 4 + sum([1 for carta in Jugadores[Persona].conocidas if carta.valor == 15 - numero_mesa]),len(Jugadores[Siguiente].mano))
    return (total-posible)/total

def comprobar_velo(Persona):
    for jugador in Orden:
        if Jugadores[jugador].velo:
            velo=True
        if jugador == Persona:
            for carta in Jugadores[jugador].mano:
                if carta.valor == 7 and carta.palo == 'Oro':
                    velo=False

def comprobar_tirada(Persona):
    Jugadores[Persona].conocidas= Mesa.total+Jugadores[Persona].mano
    Opciones=[]
    for combinacion in combinaciones(Mesa.cartas):
        numeros_combinacion_mesa=sum([carta.valor for carta in combinacion])
        if numeros_combinacion_mesa>15:
            continue
        Opciones += [combinacion+[carta] for carta in Jugadores[Persona].mano if carta.valor+numeros_combinacion_mesa == 15]
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
     ## calcular si vale la pena ir a por algun punto ##
    for jugador in Orden:
        if jugador!= Persona:
            sietes.append(Jugadores[jugador].sietes)
            oros.append(Jugadores[jugador].oros) 
            cartas.append(Jugadores[jugador].numero_cartas)
    Sietes = 4 - sum(sietes) >= max(sietes) - Jugadores[Persona].sietes and Jugadores[Persona].sietes <= 2
    Oros = 10 - sum(oros) >= max(oros) - Jugadores[Persona].oros and Jugadores[Persona].oros <= 5
    Cartas = 40 - sum(cartas) >= max(cartas) - Jugadores[Persona].numero_cartas and Jugadores[Persona].numero_cartas <= 20
    opciones=comprobar_tirada(Persona)
    ## estab;ecida la prioridad, calcular la opcion mas rentable##
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
                cuatro.append([opcion, Puntuacion*2])
            elif calificacion['+15']:
                masquince.append([opcion, Puntuacion*1.5])
            elif calificacion['Reescoba'] != False:
                reescoba.append([opcion, Puntuacion*(1-calificacion['Reescoba'])])
            elif calificacion['Preparada'] != False:
                preparada.append([opcion, Puntuacion*1.5])
            else:
                preparada.append([opcion, Puntuacion])
    ## lista 'buenas' es la opcion a escoger por defecto, para el resto se ha calculado la rentabilidad ##
    finalista=None
    puntuacion=0
    if len(buenas) > 0:
        lista = buenas
    else:
        if len(cuatro) > 0:
            lista = cuatro
        else:
            if len(masquince) > 0 or len(preparada) > 0:
                lista = masquince + preparada
            else:
                lista = reescoba
    for opcion in lista:
        if opcion[-1]>puntuacion:
            puntuacion=opcion[-1]
            finalista=opcion[0]
    return finalista

def dejar_carta_mesa(Persona):
    resumen = []
    opciones=[]
    if len(Jugadores[Persona].mano) == 1:
        return 0
    ## Cualcular el siguiente jugador ##
    for index, persona in enumerate(Orden):
            if persona == Persona:
                i=index+1
                if i == len(Orden):
                    i=0
    siguiente = Orden[i]
    for index, carta in enumerate(Jugadores[Persona].mano):
        numeros_cartas_mesa = [carta.valor for carta in Mesa.cartas]
        if sum(numeros_cartas_mesa) + carta.valor == 4:
            return index
        elif carta.valor in numeros_cartas_mesa and carta.valor > 7:
            return index
        reescobas=[False]
        for combinacion in combinaciones(Mesa.cartas+[carta]):
            numeros_combinacion_mesa = sum([carta_mesa.valor for carta_mesa in combinacion])
            if numeros_combinacion_mesa < 15 and numeros_combinacion_mesa > 4 and numeros_combinacion_mesa not in reescobas:
                if len(combinacion) == len(Mesa.cartas) + 1:
                    reescobas[0] = True
                reescobas.append(numeros_combinacion_mesa)
        opciones.append(reescobas)
    for opcion in opciones:
        posibilidades = []
        if opcion[0]:
            escoba=probabilidades(Persona, siguiente, int(min(opcion[1:])))
            resumen.append([True, escoba])
            continue
        for numero in opcion[1:]:
            posibilidades.append(probabilidades(Persona, siguiente, numero))
        if posibilidades != []:
            maximo_probabilidad = max(posibilidades)
            resumen.append([False, maximo_probabilidad])
    posibilidades = 1
    posibilidades_escoba = 1
    escoba=True
    if resumen == []:
        for index, carta in enumerate(Jugadores[Persona].mano):
            if carta.palo != 'oro':
                return index
    for index, opcion in enumerate(resumen):
        if not opcion[0] and opcion[1] < posibilidades:
            resultado = index
            posibilidades = opcion[1]
            escoba = False
        elif escoba and opcion[1] < posibilidades_escoba:
            posibilidades_escoba = opcion[1]
            resultado = index
    return resultado

def opcion_a_escoger (Persona):
    if escoger_opcion_recogida(Persona) == None:
        print (f'No hay opciones para {Persona}, se descartará {Jugadores[Persona].mano[dejar_carta_mesa(Persona)]}')
        Jugadores[Persona].descartar(Jugadores[Persona].mano[dejar_carta_mesa(Persona)])
        for jugadores in Orden:
            if jugadores!= Persona:
                Jugadores[jugadores].ultimo = False
            else:
                Jugadores[jugadores].ultimo = True
    else:
        print (f'{Persona} escoge {etiquetar(escoger_opcion_recogida(Persona))}')
        Jugadores[Persona].recoger(escoger_opcion_recogida(Persona))

def empate_o_no_empate(tipo_puntos):  ## retorna [Valor_maximo, jugadores_con_valor_maximo]
    resultado = []
    puntos = {}
    for jugador in Orden:
        if 'setenta' in tipo_puntos:
            puntos[jugador] = Jugadores[jugador].sietes
        elif 'oros' in tipo_puntos:
            puntos[jugador] = Jugadores[jugador].oros
        elif 'cartas' in tipo_puntos:
            puntos[jugador] = Jugadores[jugador].numero_cartas
        elif 'contador' in tipo_puntos:
            puntos[jugador] = Jugadores[jugador].contador
    resultado = [max(puntos.values())]
    for jugador in Orden:
        if puntos[jugador] == max(puntos.values()):
            resultado.append(jugador)
    return resultado

def calcular_puntuacion():
    tríada = {'las setenta': 0, 'los oros': 0, 'las cartas': 0}
    for tanto in tríada:
        tríada[tanto] = empate_o_no_empate(tanto)
    velo = ''
    frase = {'las setenta': 'sietes', 'los oros': 'oros', 'las cartas': 'cartas'}
    for jugador in Orden:
        if Jugadores[jugador].sietes == tríada['las setenta'][0] and len(tríada['las setenta']) == 2:
            Jugadores[jugador].contador += 1
        if Jugadores[jugador].oros == tríada['los oros'][0] and len(tríada['los oros']) == 2:
            Jugadores[jugador].contador += 1
        if Jugadores[jugador].numero_cartas == tríada['las cartas'][0] and len(tríada['las cartas']) == 2:
            Jugadores[jugador].contador += 1
        if Jugadores[jugador].velo:
            Jugadores[jugador].contador += 1
            velo = jugador
        Jugadores[jugador].contador += Jugadores[jugador].escobas
        print (f'{jugador} ha realizado {Jugadores[jugador].escobas} escobas')
    Ganador = empate_o_no_empate('contador')
    for tanto in tríada:
        if len(tríada[tanto]) > 2:
            print ('\n' + f'{', '.join(tríada[tanto][1:-1])} y {tríada[tanto][-1]} han empatado en {tanto} con {tríada[tanto][0]} {frase[tanto]}')
        else:
            print ('\n' + f'{tríada[tanto][1]} ha ganado {tanto}')
    print ('\n' + f'{velo} ha ganado el velo' + '\n')
    if len(Ganador) > 2:
        print (medio('GANADORES','-_',100) + '\n')
        print (medio(f'{', '.join(Ganador[1:-1])} y {Ganador[-1]}',' ',100) + '\n')
    else:
        print (medio('GANADOR','-_',100)+'\n')
        print (medio(f'{Ganador[1]}',' ',100) + '\n')
    print ('-_'*50)

numero_cartas_mesa = 4
numero_cartas_jugador = 3
Rondas= list(range(1, int((40-numero_cartas_mesa)/(numero_cartas_jugador*numero_jugadores))+1))
Mesa.repartir(numero_cartas_mesa)
print ('*'*100)
print (medio('EMPIEZA LA PARTIDA','-',100)+'\n')
for ronda in Rondas:
    if ronda == Rondas[-1]:
        texto = 'RONDA FINAL'
    else:
        texto = f'RONDA {ronda}'
    print ('\n' + medio(texto,'-',100) + '\n')
    for jugador in Orden:
        Jugadores[jugador].recibir(numero_cartas_jugador)
    print ('- '*50)
    for turno in range(numero_cartas_jugador):
        for jugador in Orden:
            print ('Cartas de la mesa: ',etiquetar(Mesa.cartas))
            print (f'Cartas {jugador}: ', etiquetar(Jugadores[jugador].mano))
            opcion_a_escoger(jugador)
            print ('- '*50)
            #if input('Continuar con la partida? [s/n]: ') == 'n':
                #quit()
    if ronda == Rondas[-1]:
        print (medio('FIN DE LA PARIDA','-',100)+'\n')
        print ('*'*100)
        for jugador in Orden:
            if Jugadores[jugador].ultimo:
                print ('\n' + f'{jugador} ha sido el último en recoger cartas' + '\n')
                Jugadores[jugador].recoger(Mesa.cartas)
        print (medio('PUNTUACIÓN','-',100) + '\n')
        calcular_puntuacion()