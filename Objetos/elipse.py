from Objetos.figura import Figura
class Elipse(Figura):
    def __init__(self, radio_mayor, radio_menor):
        super().__init__()
        self.radio_mayor = radio_mayor
        self.radio_menor = radio_menor
        self.color = "amarillo"