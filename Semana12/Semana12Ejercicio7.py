# Ejercicio 7:
# Solicita el monto de una compra y aplica:
# Más de 100: 20% de descuento
# Entre 50 y 100: 10% de descuento
# Menos de 50: sin descuento

monto = float(input("Ingresa el monto de la compra para su descuento: "))

if monto > 100:
    descuento = monto * 0.20
elif monto >= 50:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print("Descuento:", descuento)
print("Total a pagar:", total)
