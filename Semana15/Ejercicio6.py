# 6. Crear un programa que genere 10 números aleatorios,
# los guarde en un arreglo y mediante una función indique cuántos son mayores a 50.

import random


def contarMayores(listaNumeros):
    mayores = 0
    for numero in listaNumeros:
        if numero > 50:
            mayores += 1
    return mayores


numeros = [random.randint(1, 100) for _ in range(10)]
print(f"Números generados: {numeros}")
mayoresA50 = contarMayores(numeros)
print(f"Cantidad de números mayores a 50: {mayoresA50}")
