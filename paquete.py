class Paquete:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __str__(self):
        return f"Paquete de {self.origen} a {self.destino} con peso {self.peso}"