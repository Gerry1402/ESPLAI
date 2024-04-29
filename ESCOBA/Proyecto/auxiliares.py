from itertools import combinations
from math import factorial
from mesa import Mesa
from jugadores import Jugadores

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