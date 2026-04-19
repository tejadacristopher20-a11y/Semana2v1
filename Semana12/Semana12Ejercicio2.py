# Ejercicio 2:
# Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).

edadX = float(input("Ingresa tu edad: "))

if edadX < 18:
    print("Eres menor ve a jugar Roblox")
elif edadX >= 18 and edadX <= 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")
