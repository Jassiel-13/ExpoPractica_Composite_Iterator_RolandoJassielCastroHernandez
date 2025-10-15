from src.component import Component
from src.iterator import CompositeIterator

class Menu(Component):
    """Elemento compuesto del menú (puede contener submenús o ítems)"""

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"> {self.nombre}")
        for elemento in self.elementos:
            elemento.mostrar(nivel + 1)

    def crear_iterador(self):
        return CompositeIterator(self.elementos)
