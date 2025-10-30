from Objetos.figura import Figura
class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.color = "rojo"
