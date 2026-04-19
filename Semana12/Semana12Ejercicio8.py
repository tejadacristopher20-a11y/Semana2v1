# Ejercicio 8:
# Pide tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

lado1 = float(input("Ingresa el primer lado: "))
lado2 = float(input("Ingresa el segundo lado: "))
lado3 = float(input("Ingresa el tercer lado: "))

if lado1 == lado2 == lado3:
    print("Triángulo equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triángulo isósceles")
else:
    print("Triángulo escaleno")
