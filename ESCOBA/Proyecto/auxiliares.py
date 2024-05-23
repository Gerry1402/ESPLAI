from itertools import combinations
from math import factorial

def combinaciones(lista):
    return [list(combinacion) for r in range(len(lista) + 1) for combinacion in combinations(lista, r)]

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

def medio (string,laterales,ancho):
    resultado=(list(laterales)*((100 // len(laterales)) + 1))[:ancho]
    if len(string) == 0:
        return ''.join(resultado)
    empezar = (ancho // 2) - (len(string) // 2)
    resultado[empezar - 1] = ' '
    resultado[empezar + len(string)] = ' '
    for i in range(len(string)):
        resultado[empezar + i] = string[i]
    return ''.join(resultado)