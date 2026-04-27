# 2. Contador de positivos y negativos
# Con while, permite ingresar números hasta que el usuario escriba 0.
# Dentro, usa if para contar cuántos son positivos y negativos.
# Al final, usa un for para mostrar un resumen de resultados.

positivos = 0
negativos = 0
numero = 1

while numero != 0:
    numero = int(input("Ingresa un número (0 para salir del bucle y ver resumen): "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("Resumen de resultados:")

for i in range(1):
    print("Cantidad de positivos:", positivos)
    print("Cantidad de negativos:", negativos)
