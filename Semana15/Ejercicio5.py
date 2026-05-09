# 5. Diseñar una función que reciba un arreglo de números
# y retorne un nuevo arreglo solo con los números positivos usando un bucle y condicionales.


def numerosPositivos(listaNumeros):
    positivos = []
    for numero in listaNumeros:
        if numero > 0:
            positivos.append(numero)
    return positivos


numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

positivos = numerosPositivos(numeros)
print(f"Los números positivos son: {positivos}")
