palabra = "CANTANDO"

palabraMinuscula = palabra.lower()

palabraRecor = palabraMinuscula.replace("ando", "")

lugarT = palabraRecor.find("t")

print("Palabra en minusculas: ", palabraMinuscula)
print("Palabra sin 'ando': ", palabraRecor)
print("lugar de la letra t: ", lugarT)
