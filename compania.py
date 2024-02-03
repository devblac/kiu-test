class Compania:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.paquetes = []

    def transportar(self, paquete):
        self.paquetes.append(paquete)

    def reporte(self):
        total_paquetes = 0
        total_dinero = 0
        for paquete in self.paquetes:
            total_paquetes += 1
            dinero = self.precio * paquete.peso
            total_dinero += dinero
        return f"Reporte de la compañía {self.nombre}:\nTotal de paquetes transportados: {total_paquetes}\nTotal recaudado: {total_dinero}$"