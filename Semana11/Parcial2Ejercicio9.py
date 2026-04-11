# Ejercicio 9
# 1. Toma la cadena "Any time y Anytime".
# 2. Reemplaza todas las apariciones de "Any time" (con espacio) por "Always".
# 3. Convierte todo el texto resultante a mayusculas.

txt = "Any time y Anytime"

txtRempla = txt.replace("Any time", "Always")

txtMayuscula = txtRempla.upper()

print("Texto modificado: ", txtRempla)
print("nuevo texto en mayusculas: ", txtMayuscula)
