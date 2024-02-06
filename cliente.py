from paquete import Paquete

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.paquetes = []

    def enviar_paquete(self, compañía, origen, destino, fecha):
        paquete = Paquete(self, compañía, origen, destino, fecha)
        self.paquetes.append(paquete)
        compañía.agregar_paquete(paquete)
        return paquete