# 8. Crear un programa que almacene 5 productos en un arreglo y
# mediante una función busque un producto específico ingresado por el usuario.


def buscarProducto(listaProductos, productoBuscado):
    for producto in listaProductos:
        if producto.lower() == productoBuscado.lower():
            return True
    return False


productos = ["Arroz", "Leche", "Pan", "Huevos", "Azúcar"]
print("Productos disponibles:")
for producto in productos:
    print(producto)

productoBuscado = input("Ingrese el nombre del producto que desea buscar: ")
if buscarProducto(productos, productoBuscado):
    print(f"El producto '{productoBuscado}' está disponible.")
else:
    print(f"El producto '{productoBuscado}' no está disponible.")
