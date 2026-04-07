# Laboratorio 2 Ejercicio 8


def transformar(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "Opción inválida"


print("=== MENÚ ===")
print("1. Convertir a MAYÚSCULAS")
print("2. Convertir a minúsculas")
print("3. Primera letra en mayúscula")

texto = input("Ingrese un texto: ")
opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion.isdigit():
    opcion = int(opcion)
    resultado = transformar(texto, opcion)
else:
    resultado = "Opción inválida"

print("Resultado:", resultado)
