# Ejercicio 5:
# Para cumplir con la normativa de privacidad, debes transformar los nombres de los usuarios,
# invirtiendo su orden y formateando la estructura de las letras.

# Pide al usuario su nombre completo (Nombre y Apellido).

# Conviértelo en una lista usando .split() y utiliza Slicing con paso negativo[::-1])
# para que el apellido aparezca antes que el nombre en una nueva lista.

# Implementa un for anidado:
# El primer bucle recorrerá las palabras de la lista invertida.
# El segundo bucle recorrerá cada letra de esa palabra.

# Imprime las letras de cada palabra separadas por un punto (ejemplo: S.o.r.t.o),
# creando una separación clara entre el apellido y el nombre.

nombreCompleto = input("Ingrese su nombre completo (Nombre Apellido): ")
listaInvertida = nombreCompleto.split()[::-1]

for palabra in listaInvertida:
    for letra in palabra:
        print(letra, end=".")
    print()
