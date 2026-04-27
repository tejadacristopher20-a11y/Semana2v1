# 7. Promedio de notas
# Con while, permite ingresar notas hasta que el usuario escriba -1.
# Usa if para ignorar notas inválidas (menores a 0 o mayores a 10).
# Luego usa for para recorrer las notas válidas y calcular el promedio.

notas = []
nota = 0

while nota != -1:
    nota = float(input("Ingresa una nota (-1 para salir): "))

    if nota >= 0 and nota <= 10:
        notas.append(nota)

suma = 0

for n in notas:
    suma += n

if len(notas) > 0:
    promedio = suma / len(notas)
    print("El promedio es:", promedio, "Vamosss")
else:
    print("No se ingresaron notas válidas")
