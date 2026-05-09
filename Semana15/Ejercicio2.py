# 2. Desarrollar un programa que permita ingresar 10 nombres en un arreglo y luego,
# mediante una función, muestre solo los nombres que tengan más de 5 caracteres.


def nombresLargos(listanombres):
    print("\nNombres con más de 5 caracteres:")
    for nombre in listanombres:
        if len(nombre) > 5:
            print(nombre)


nombres = []

print("Ingresa 10 nombres:")

for i in range(10):
    nombre = input(f"Ingrese el nombre {i+1}: ")
    nombres.append(nombre)

nombresLargos(nombres)
