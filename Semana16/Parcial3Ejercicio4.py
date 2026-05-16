# Ejercicio 4:
# Un script debe auditar una secuencia de 50 registros, pero debe ignorar registros
# corruptos y detenerse si detecta una amenaza de seguridad.

# Crea un bucle que recorra un rango de 1 a 50.

# Filtro de Omisión: Si el número es múltiplo de 3 (simulando un registro corrupto),
# utiliza la sentencia continua para saltarlo sin imprimir nada.

# Protocolo de Parada: Si el número es igual a 42 (simulando una brecha de seguridad),
#  utiliza break para detener todo el proceso inmediatamente.

# Para todos los demás casos, imprime: "Procesando registro ID: [número]".

for i in range(1, 51):
    if i % 3 == 0:
        continue

    if i == 42:
        print("Amenaza de seguridad detectada. Deteniendo el proceso.")
        break

    print(f"Procesando registro ID: {i}")
