# 8. Patrón de asteriscos
# Pide un número.
# Usa for para imprimir un triángulo de asteriscos.
# Usa if para que solo imprima filas impares.
# Repite con while hasta que el usuario ingrese 0.

numero = -1

while numero != 0:
    numero = int(input("Ingresa un número (0 para salir): "))

    if numero != 0:
        print("Triángulo de asteriscos:")

        for i in range(1, numero + 1):
            if i % 2 != 0:
                print("*" * i)
