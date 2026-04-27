# 1 Números pares en rango
# Pide al usuario un número n.
# Usa un for para recorrer de 1 a n.
# Usa un if para imprimir solo los números pares.
# Repite todo con while hasta que el usuario ingrese 0.

n = -1

while n != 0:
    n = int(input("Ingresa un número (0 para salir del bucle): "))

    if n != 0:
        print("Números pares del 1 al", n)

        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)
