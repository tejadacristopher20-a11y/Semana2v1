# Ejercicio 12
# 1. Toma el nombre de archivo "Sunombre.txt".
# 2. Remueve el sufijo ".txt" y posteriormente remueve el prefijo "ING. ".
# 3. Toma el texto que quede limpio, convertido a minúsculas.

archivo = "ING.CristopherDavid.txt"

archivoLimpio = archivo.replace(".txt", "").replace("ING.", "")

archivoConfidencial = archivoLimpio.lower()

print("El archivo ultra secreto se llama: ", archivoConfidencial)
