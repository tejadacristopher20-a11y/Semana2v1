# Ejercicio 10:
# Pide usuario y contraseña. Si ambos coinciden con valores predefinidos, muestra "Acceso permitido", de lo contrario "Acceso denegado".

usuarioCorrec = "CrisCris"
contraseñaCorrec = "12345"

usuario = input("Ingresa tu usuario: ")
password = input("Ingresa tu contraseña: ")

if usuario == usuarioCorrec and password == contraseñaCorrec:
    print("Acceso permitido")
else:
    print("Acceso denegado")
