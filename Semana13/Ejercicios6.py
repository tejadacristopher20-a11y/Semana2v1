# 6. Números primos en rango
# Pide un número n.
# Usa for para recorrer del 1 a n.
# Dentro, usa otro for con if para verificar si cada número es primo.
# Repite con while hasta que el usuario ingrese 0.

n = -1

while n != 0:
    n = int(input("Ingresa un número (0 para salir): "))

    if n != 0:
        print("Números primos del 1 al", n)

        for i in range(2, n + 1):
            primo = True

            for j in range(2, i):
                if i % j == 0:
                    primo = False

            if primo:
                print(i)
