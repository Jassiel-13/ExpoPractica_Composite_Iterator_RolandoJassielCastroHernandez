from abc import ABC, abstractmethod

class Component(ABC):
    """Interfaz base del patrón Composite"""

    @abstractmethod
    def mostrar(self, nivel=0):
        pass

    @abstractmethod
    def crear_iterador(self):
        pass
