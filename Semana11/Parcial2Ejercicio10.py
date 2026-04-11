# Ejercicio 10
# 1. Toma la cadena "Python2026".
# 2. Verifica si el texto es estrictamente alfanumérico (solo letras y números, sin espacios ni símbolos).
# 3. Si lo es, convierte el texto a minúsculas y luego separa la palabra de los números reemplazando "2026" por una cadena vacia "".

palabra = "Python2026"

palabraIsa = palabra.isalnum()

print("La palabra solo es numero y texto: ", palabraIsa)

palabraMinuscula = palabra.lower()

palabraRemplas = palabraMinuscula.replace("2026", "")

print("Palabra final: ", palabraRemplas)
