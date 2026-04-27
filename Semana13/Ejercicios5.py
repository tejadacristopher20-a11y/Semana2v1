# 5. Validación de contraseña
# Con while, pide una contraseña hasta que sea correcta.
# Usa if para verificar si coincide.
# Después, usa for para mostrar cuántos intentos fallidos hubo.

passwordCorrect = "Cris200"
password = ""
intentos = 0

while password != passwordCorrect:
    password = input("Ingresa tu contraseña secreta: ")

    if password == passwordCorrect:
        print("Bienvenido a tu cuenta de Steam")
    else:
        print("Contraseña incorrecta")
        intentos += 1

print("Intentos fallados: ")

for i in range(intentos):
    print(i + 1)
