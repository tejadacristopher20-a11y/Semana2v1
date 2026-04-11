nombre = "Cristopher David Salmeron Tejada"

nombreCase = nombre.casefold()

nombreEspacios = nombreCase.replace(" ", "")

nombreIsal = nombreEspacios.isalpha()

print("Nombre: ", nombreCase)
print("solo tiene letras: ", nombreIsal)
