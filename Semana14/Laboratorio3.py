# Control de inventario: for productos, if stock, while menú, select case categoría.

import os

inventario = {
    "Populares": {"Mango": 5, "Guayaba": 3},
    "Comunes": {"Manzana": 10, "Banana": 8, "Pera": 0},
    "Pequeñas": {"Fresas": 6, "Uvas": 2},
}

print("🍓 Bienvenido a Frutería La Bendición 🍓")

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("\n --- MENÚ ---")
    print("1. Ver productos")
    print("2. Comprar producto")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            print("\n Inventario:")

            for categoria, productos in inventario.items():
                print(f"\n {categoria}:")
                for producto, cantidad in productos.items():
                    if cantidad > 0:
                        print(f" - {producto}: {cantidad} disponibles")
                    else:
                        print(f" - {producto}: Agotado.")

            input("\n Presiona ENTER para continuar :)")

        case "2":
            print("\n Elige una categoría:")
            print("1. Populares")
            print("2. Comunes")
            print("3. Pequeñas")

            categori = input("Selecciona: ")

            match categori:
                case "1":
                    categoria = "Populares"
                case "2":
                    categoria = "Comunes"
                case "3":
                    categoria = "Pequeñas"
                case _:
                    print("Opción inválida")
                    input("\n Presiona ENTER para continuar :)")
                    continue

            print(f"\n Productos en {categoria}:")
            for producto, cantidad in inventario[categoria].items():
                print(f"- {producto} ({cantidad})")

            producto = input("¿Qué producto deseas? ")

            if producto in inventario[categoria]:
                if inventario[categoria][producto] > 0:
                    inventario[categoria][producto] -= 1
                    print("Compra realizada :)")
                else:
                    print("Producto agotado")
            else:
                print("Producto no existe")

            input("\n Presiona ENTER para continuar ;)")

        case "3":
            print("Gracias por visitarnos 🙌")
            break

        case _:
            print("Opción inválida")
            input("\n Presiona ENTER para reiniciar  :)")
