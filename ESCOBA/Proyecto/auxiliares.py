from itertools import combinations

def combinaciones(lista):
    return [list(combinacion) for r in range(len(lista) + 1) for combinacion in combinations(lista, r)]