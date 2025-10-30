from Objetos.figura import Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        self.color = "azul"
