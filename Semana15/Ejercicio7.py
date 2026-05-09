# 7. Desarrollar una función que reciba un arreglo de edades
# y determine cuántas personas son mayores de edad utilizando if y un ciclo.


def contarMayoresDeEdad(listaEdades):
    mayoresDeEdad = 0
    for edad in listaEdades:
        if edad >= 18:
            mayoresDeEdad += 1
    return mayoresDeEdad


edades = []
cantidad = int(input("¿Cuántas edades deseas ingresar? "))
for i in range(cantidad):
    edad = int(input(f"Ingrese la edad {i+1}: "))
    edades.append(edad)

mayoresDeEdad = contarMayoresDeEdad(edades)
print(f"Cantidad de personas mayores de edad: {mayoresDeEdad}")
