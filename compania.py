class Compania:

    def __init__(self, nombre):
        self.nombre = nombre
        self.paquetes = []

    def agregar_paquete(self, paquete):
        self.paquetes.append(paquete)

    def generar_reporte(self, fecha):
        contador = 0
        total = 0
        for paquete in self.paquetes:
            if paquete.fecha == fecha:
                contador += 1
                total += paquete.precio
        return f"Reporte de la Compania {self.nombre} para el día {fecha}:\nTotal de paquetes transportados: {contador}\nTotal recaudado: {total}$"