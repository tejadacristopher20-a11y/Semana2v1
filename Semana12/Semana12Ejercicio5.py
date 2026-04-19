# Ejercicio 5:
# Solicita dos números y una operación (+, -, *, /) y realiza el cálculo usando if, elif y else.

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa una operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
    print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    print("Resultado:", numero1 / numero2)
else:
    print("Operación no válida")
