# Ejercicio 3:
# Ingresa una nota del 0 al 10 y muestra:
# 9-10: Excelente
# 7-8: Bueno
# 6: Aprobado
# 0-5: Reprobado

notaX = int(input("Ingresa tu nota: "))

if 9 <= notaX <= 10:
    print("Tu nota es Excelente")
elif 7 <= notaX < 9:
    print("Tu nota es Buena")
elif 6 <= notaX:
    print("Aprobaste por la minima")
elif 0 <= notaX < 6:
    print("Reprobaste mano")
else:
    print("Nota inválida")
