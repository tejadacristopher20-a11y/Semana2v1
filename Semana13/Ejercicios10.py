# 10. Suma acumulativa con límite
# Con while, pide números hasta que la suma supere 100.
# Usa if para ignorar números negativos.
# Luego usa for para mostrar todos los números válidos ingresados.

numeros_validos = []
suma = 0

while suma <= 100:
    numero = int(input("Ingresa un número: "))

    if numero >= 0:
        numeros_validos.append(numero)
        suma += numero

print("La suma superó 100")
print("Números válidos ingresados:")

for n in numeros_validos:
    print(n)
