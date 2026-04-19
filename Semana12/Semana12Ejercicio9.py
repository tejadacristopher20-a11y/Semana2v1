# Ejercicio 9:
# Solicita un año y determina si es bisiesto.

añoX = int(input("Ingresa un año: "))

if (añoX % 4 == 0 and añoX % 100 != 0) or (añoX % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
