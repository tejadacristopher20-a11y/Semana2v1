# Laboratorio 2 Ejercicio 4


def transformar_lista(lista, opcion):
    resultado = []

    for palabra in lista:
        if opcion == 1:
            resultado.append(palabra.upper())
        elif opcion == 2:
            resultado.append(palabra.lower())
        elif opcion == 3:
            resultado.append(palabra.capitalize())
        else:
            return "Opción inválida"

    return resultado


# Pedir palabras al usuario
texto = input("Ingrese palabras separadas por espacio: ")
lista_palabras = texto.split()

opcion = int(input("Ingrese una opción (1, 2 o 3): "))

resultado = transformar_lista(lista_palabras, opcion)

print("Resultado:", resultado)
