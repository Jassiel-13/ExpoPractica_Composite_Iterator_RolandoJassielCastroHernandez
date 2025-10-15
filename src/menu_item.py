from src.component import Component

class MenuItem(Component):
    """Elemento individual del menú (hoja del árbol)"""

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self, nivel=0):
        print("  " * nivel + f"- {self.nombre} - ${self.precio}")

    def crear_iterador(self):
        return iter([self])
