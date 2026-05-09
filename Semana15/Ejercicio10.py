# 10. Diseñar un programa que permita ingresar 6 números
# en un arreglo y mediante una función ordenarlos de menor a mayor usando ciclos e instrucciones condicionales.


def ordenarNumeros(listaNumeros):
    for i in range(len(listaNumeros)):
        for j in range(i + 1, len(listaNumeros)):
            if listaNumeros[i] > listaNumeros[j]:
                listaNumeros[i], listaNumeros[j] = listaNumeros[j], listaNumeros[i]
    return listaNumeros


numeros = []
for i in range(6):
    print("Ingresa 6 números para ordenar:")
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numerosOrdenados = ordenarNumeros(numeros)
print("Números ordenados de menor a mayor:")
for numero in numerosOrdenados:
    print(numero)
