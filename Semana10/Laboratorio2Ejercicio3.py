# Laboratorio 2 Ejercicio 3


def transformarTexto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opcion invalida"


texto = input("Ingrese un texto: ")
numero = int(input("Elija una opción (1,2 o 3): "))

resultado = transformarTexto(texto, numero)
print("Resultado:", resultado)
