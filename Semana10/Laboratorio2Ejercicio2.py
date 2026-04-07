# Laboratorio 2 Ejercicio 2


def opcionPalabra(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())
    else:
        print("Opcion invalida")


palabra = input("Ingrese una palabra: ")
numero = int(input("Elija una opción (1, 2 0 3): "))

opcionPalabra(palabra, numero)
