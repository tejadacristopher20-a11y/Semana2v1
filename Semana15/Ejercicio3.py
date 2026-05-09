# 3. Crear una función que reciba un arreglo de notas y devuelva el promedio.
#  Además, usando if, indicar si el grupo aprueba o reprueba.


def promedioNo(listaNotas):
    suma = 0
    for nota in listaNotas:
        suma += nota
    promedio = suma / len(listaNotas)
    return promedio


notas = []

cantidad = int(input("¿Cuántas notas deseas ingresar? "))

for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = promedioNo(notas)

print(f"\nEl promedio del grupo es: {promedio:.2f}")

if promedio >= 6:
    print("El grupo aprueba ya pueden celebrar")
else:
    print("El grupo reprueba, a estudiar más")
