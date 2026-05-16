# Ejercicio 3
# Un sensor industrial envía lecturas de temperatura. Debes programar la lógica que decida qué
# alertas disparar según los valores recibidos.
# Solicita al usuario 5 lecturas de temperatura (números enteros) y almacenarlas en una lista.

# Itera la lista con un for y utiliza la estructura match-case para evaluar:
# Caso 0: Mostrar "Alerta: Punto de Congelación".
# Caso 100: Mostrar "Alerta: Punto de Ebullición".

# Caso por defecto (_): Usa un Operador Ternario interno para imprimir "Estado: Estable" si
#  la temperatura está entre 10 y 30 grados i, "Estado: Crítico" si está fuera de ese rango.


Temoeraturas = []
for i in range(5):
    temp = int(input(f"Ingrese la lectura de temperatura {i+1}: "))
    Temoeraturas.append(temp)

for temp in Temoeraturas:
    match temp:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(estado)
