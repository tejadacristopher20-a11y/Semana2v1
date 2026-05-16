# Ejercicio 1
# Se trabaja para una empresa de envíos. Recibes códigos de rastreo con el formato AÑO-CATEGORÍA-PAÍS
# (ejemplo: 2024-TECNOLOGIA-ES). Tu tarea es automatizar la clasificación de estos paquetes siguiendo estas instrucciones:

# Solicita al usuario una etiqueta de rastreo mediante input(). ( escriba en la consola )

# Realiza una validación de seguridad: si la entrada está vacía ("") o es None, el programa debe informar el error y finalizar.

# Utilizando Slicing, extrae la sección central (la categoría) y muéstrala en pantalla.

# Aplica el Operador Ternario para imprimir: "Ruta Local" si el código termina en las siglas de tu país (ejemplo: "SV"),
# o "Ruta Internacional" en cualquier otro caso.


while True:

    codigo = input(
        "Ingrese el código de rastreo (ejemplo: 2000-CATEGORÍA-SV) o 'salir' para terminar: "
    )

    if codigo.lower() == "salir":
        print("Programa finalizado.")
        break

    if codigo == "" or codigo is None:
        print("Error: El código de rastreo no puede estar vacío.")
        continue

    primerGuion = codigo.find("-")
    segundoGuion = codigo.find("-", primerGuion + 1)

    if primerGuion == -1 or segundoGuion == -1:
        print("Error: El formato del código no es válido.")
        continue

    categoria = codigo[primerGuion + 1 : segundoGuion]
    print("Categoría:", categoria)

    ruta = "Ruta Local" if codigo.endswith("SV") else "Ruta Internacional"
    print(ruta)
