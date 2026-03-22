# Ejercicio 3

#  Solicitar frase
frase = input("Ingrese una frase: ")

# Eliminar los espacios
fraseSinEspacios = frase.replace(" ", "")

# Contar las letras
cantidad = len(fraseSinEspacios)

# mostrar
print("Cantidad de letras (sin espacios):", cantidad)
