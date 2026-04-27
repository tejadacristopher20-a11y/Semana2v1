# 9. Juego de adivinar número
# Genera un número secreto.
# Con while, permite intentos hasta acertar.
# Usa if para dar pistas (mayor o menor).
# Luego usa for para mostrar todos los intentos realizados.

import random

numero_secreto = random.randint(1, 10)
intento = 0
intentos = []

while intento != numero_secreto:
    intento = int(input("Adivina el número (1 al 10): "))
    intentos.append(intento)

    if intento < numero_secreto:
        print("El número es mayor")
    elif intento > numero_secreto:
        print("El número es menor")
    else:
        print("¡Correcto!")

print("Todos los intentos realizados:")

for i in intentos:
    print(i)
