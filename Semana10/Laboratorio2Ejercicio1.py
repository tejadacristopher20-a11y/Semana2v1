# Laboratorio 2 Ejercicio 1


def opcionTexto(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "Opcion invalida"


texto = input("Ingrese un texto: ")
numero = int(input("Elija una opción (1, 2 0 3): "))

resultado = opcionTexto(texto, numero)
print("Resultado:", resultado)
