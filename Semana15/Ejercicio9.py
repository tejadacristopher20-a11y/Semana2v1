# 9. Elaborar una función que reciba un arreglo de números y
# devuelva la suma total, pero solo sumando los números pares.


def sumarPares(listaNumeros):
    suma = 0
    for numero in listaNumeros:
        if numero % 2 == 0:
            suma += numero
    return suma


numeros = []
cantidad = int(input("¿Cuántos números deseas poner para sumar? "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

sumaPares = sumarPares(numeros)
print(f"La suma de los números pares es: {sumaPares}")
