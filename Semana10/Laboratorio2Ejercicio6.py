# Laboratorio 2 Ejercicio 6


def transformarYcontar(texto, opcion):
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        return "Opción inválida"

    cantidad = len(resultado)

    return resultado, cantidad


texto = input("Ingrese un texto: ")
opcion = int(input("Ingrese una opción (1, 2 o 3): "))

resultado = transformarYcontar(texto, opcion)

if resultado == "Opción inválida":
    print(resultado)
else:
    texto_final, cantidad = resultado
    print("Texto transformado:", texto_final)
    print("Cantidad de caracteres:", cantidad)
