# si tenemos una variable y necesitamos comprobar si cumple

clima = "caliente"  ## clima por defecto
# entrada = input("¿Como esta el clima? ")

## print("El clima es: ", entrada)

numeroComparar = 7

if numeroComparar >= 21:
    print("Debes de tarbajar para comprar un terreno ")
else:
    print("Debes cuidad tus rodillas")

# if es el camino principal
# else es por defecto en caso del if no sea true
## If es para tomar una decicion

numero = 50


if numero > 24 and numero < 30:
    print("El numero es mayor a 24 y menor a 30")
elif numero > 30:
    print("El numero es mayor a 30")
elif numero > 35:
    print("El numero es mayor a 35 cliente vip")
else:
    print("El numero es menor a 24")

## En un rango de numero entre 10 y 100 vamos a verificar un segmento
# 18 mayor de edad
# 25 adulto joven
# 40 adulto
# 60 adulto mayor

edad = int(input("ungrese su edad: "))
edadNumero = int(edad)

if edadNumero >= 18 and edadNumero < 25:
    print("Eres menor de edad")
elif edadNumero >= 25 and edadNumero < 40:
    print("Eres adulto joven de edad")
elif edadNumero >= 40 and edadNumero < 60:
    print("Eres adulto de edad")
elif numero >= 100:
    print("Marciano")
else:
    print("Desconicido")


def cambiarformato(edad):
    if edad.isdigit():
        return int(edad)
    else:
        print("La edad debe ser un numero valido.")


if edadNumero.type() == int:
    if edadNumero >= 18 and edadNumero < 25:
        print("Eres mayor de edad")
    if edadNumero >= 25 and edadNumero < 40:
        print("Eres un adulto joven")
    if edadNumero >= 40 and edadNumero < 80:
        print("Eres un adulto")
    if edadNumero >= 100:
        print("Marciano")
    else:
        print("no encontrado")
