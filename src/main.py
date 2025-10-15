from src.menu import Menu
from src.menu_item import MenuItem

def main():
    menu_principal = Menu("Menú Principal")

    desayunos = Menu("Desayunos")
    comidas = Menu("Comidas")
    postres = Menu("Postres")

    desayunos.agregar(MenuItem("Hotcakes", 60))
    desayunos.agregar(MenuItem("Café", 25))

    comidas.agregar(MenuItem("Hamburguesa", 85))
    comidas.agregar(MenuItem("Refresco", 30))

    postres.agregar(MenuItem("Pastel de Chocolate", 70))
    postres.agregar(MenuItem("Helado", 50))

    menu_principal.agregar(desayunos)
    menu_principal.agregar(comidas)
    menu_principal.agregar(postres)

    print("🍽️ Estructura del Menú Compuesto")
    print("---------------------------------")
    menu_principal.mostrar()

    print("\n🔁 Recorriendo con el Iterador:")
    for item in menu_principal.crear_iterador():
        if isinstance(item, MenuItem):
            print(f"  - {item.nombre} (${item.precio})")

if __name__ == "__main__":
    main()
