##. Define un bloque de texto de 3 lineas usando comillas triples (puedes usar un fragmento del poema de la guia).
# 2. Cuenta cuantas veces aparece la letra "a" en todo el bloque de texto.
# 3. Divide el bloque de texto por sus saltos de linea (splitlines) para convertirlo en una lista de oraciones independientes.

medioPoema = """Ella amará a otro hombre.
Yo voy lejos, andando hacia el olvido.
Y puede suceder que alguien me nombre,
pero ella fingirá no haber oído."""

ConteoA = medioPoema.count("a")

saltosParrafos = medioPoema.splitlines()

print("Numero de a que tiene el poema: ", ConteoA)
print("Poema dividido por saltos: ", saltosParrafos)
