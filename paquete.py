class Paquete:
    precio = 10

    def __init__(self, cliente, compania, origen, destino, fecha):
        self.cliente = cliente
        self.compania = compania
        self.origen = origen
        self.destino = destino
        self.fecha = fecha

    def __str__(self):
        return f"Paquete de {self.cliente.nombre} enviado por {self.compania.nombre} desde {self.origen} hasta {self.destino} el día {self.fecha} por {self.precio}$"