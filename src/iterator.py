class CompositeIterator:
    """Iterador compuesto que recorre todos los elementos del menú."""

    def __init__(self, elementos):
        self.elementos = elementos
        self.posicion = 0
        self.sub_iterador = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.sub_iterador:
            try:
                return next(self.sub_iterador)
            except StopIteration:
                self.sub_iterador = None

        if self.posicion >= len(self.elementos):
            raise StopIteration

        elemento = self.elementos[self.posicion]
        self.posicion += 1

        if hasattr(elemento, "crear_iterador"):
            self.sub_iterador = iter(elemento.crear_iterador())

        return elemento
