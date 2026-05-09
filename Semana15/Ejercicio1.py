# 1. Crear una función que reciba una lista de números y retorne la cantidad de números pares
# e impares utilizando un bucle y estructuras condicionales.


def contar_pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares


lista = []

cantidad = int(input("¿Cuántos números deseas ingresar? "))

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numero)

pares, impares = contar_pares_impares(lista)

print(f"\nCantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
