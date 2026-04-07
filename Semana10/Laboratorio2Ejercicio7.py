# Laboratorio 2 Ejercicio 7


def transformarSecuencia(texto, listaOpciones):
    for opcion in listaOpciones:
        if opcion == 1:
            texto = texto.upper()
        elif opcion == 2:
            texto = texto.lower()
        elif opcion == 3:
            texto = texto.capitalize()
        else:
            return "Opción inválida"

    return texto


texto = input("Ingrese un texto: ")

numeros = input("Ingrese opciones separadas por espacio (ej: 1 2 3): ")

listaOpciones = []
for n in numeros.split():
    if n.isdigit():
        listaOpciones.append(int(n))
    else:
        print("Error: solo números válidos")
        exit()


resultado = transformarSecuencia(texto, listaOpciones)

print("Resultado final:", resultado)
