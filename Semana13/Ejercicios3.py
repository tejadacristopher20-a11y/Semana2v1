# 3. Tabla de multiplicar filtrada
# Pide un número.
# Con for, genera su tabla del 1 al 10.
# Usa if para mostrar solo resultados mayores a 20.
# Repite con while hasta que el usuario escriba -1.

numero = 0

while numero != -1:
    numero = int(input("Ingresa un número (-1 para salir): "))

    if numero != -1:
        print("Tabla de multiplicar de", numero)

        for i in range(1, 11):
            resultado = numero * i

            if resultado > 20:
                print(numero, "x", i, "=", resultado)
