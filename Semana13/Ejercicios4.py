# 4. Suma de números impares
# Con while, pide números hasta que se ingrese 0.
# Usa if para sumar solo los números impares.
# Luego usa for para imprimir cada número impar ingresado.

numeros_impares = []
suma = 0
numero = 1

while numero != 0:
    numero = int(
        input("Ingresa un número (0 para ver suma y numeros impares ingresados): ")
    )

    if numero % 2 != 0:
        numeros_impares.append(numero)
        suma += numero

print("Suma de números impares:", suma)
print("Números impares ingresados:")

for num in numeros_impares:
    print(num)
