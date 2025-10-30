from Objetos.figura import Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        self.color = "naranja"