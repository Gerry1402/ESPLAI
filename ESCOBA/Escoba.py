
Baraja={}
Numeros=['As','2','3','4','5','6','7','Sota','Caballo','Rey']
Palos=['oro','copa','espada','basto']
equivalencias={'As':'1','Sota':'8','Caballo':'9','Rey':'10'}
for i in Numeros:
    for j in Palos:
        Carta=i+' de '+j+'s'
        if i in equivalencias:
            i=equivalencias[i]
        Valor=[int(i),j]
        Baraja[Carta]=Valor
contrincantes=input('Especificar numero de contrincantes\n')
print ('Cartas en la mesa. Especificar individualmente. Primero numero y luego palo')
Mesa=[]
for i in range (1,5):
    numero=input('Seleccionar '+', '.join(Numeros)+'\n')
    palo=input('Seleccionar '+', '.join(Palos)+'\n')
    Mesa.append([numero, palo])
## ESCOBA ##

