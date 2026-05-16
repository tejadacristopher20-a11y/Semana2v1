# Ejercicio 2:
# Las empresas pierden dinero por errores de redondeo al usar float.
# Se te ha pedido crear un terminal de cobro seguro que garantice precisión bancaria.

# Crea un bucle while que solicite precios de productos de forma indefinida.

# Implementa una estructura try-except específica para ValueError.
# Si el usuario ingresa texto en lugar de un número, muestra un mensaje de advertencia
# y permite que el bucle continúe sin cerrar el programa.

# Utiliza la clase Decimal (del módulo decimal) para procesar los montos con precisión.

# El sistema debe cerrarse solo cuando el usuario ingrese el número 0. Al finalizar,
# muestra el total acumulado usando un f-string.  f””

from decimal import Decimal

totales = Decimal("0")

while True:
    try:
        precio = input("Ingresa el precio de tu producto (0 para salir): ")

        if precio == "0":
            break

        monto = Decimal(precio)
        totales += monto

    except ValueError:
        print("Debes ingresar un número válido.")
        continue

print(f"Total acumulado: ${totales}")
