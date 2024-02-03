import unittest

class Paquete:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

    def __str__(self):
        return f"Paquete de {self.origen} a {self.destino} con peso {self.peso}"

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

class TestCompania(unittest.TestCase):
    def setUp(self):
        self.compania = Compania("FlyBondi", 10)
        self.paquete1 = Paquete("Buenos Aires", "Tokio", 5)
        self.paquete2 = Paquete("Madrid", "Nueva York", 3)
        self.paquete3 = Paquete("Lima", "Santiago", 2)


    def test_transportar(self):
        self.compania.transportar(self.paquete1)
        self.compania.transportar(self.paquete2)
        self.compania.transportar(self.paquete3)
        self.assertEqual(len(self.compania.paquetes), 3)
        self.assertEqual(self.compania.paquetes[0], self.paquete1)
        self.assertEqual(self.compania.paquetes[1], self.paquete2)
        self.assertEqual(self.compania.paquetes[2], self.paquete3)

    def test_reporte(self):
        self.compania.transportar(self.paquete1)
        self.compania.transportar(self.paquete2)
        self.compania.transportar(self.paquete3)
        reporte = self.compania.reporte()
        self.assertEqual(reporte, "Reporte de la compañía FlyBondi:\nTotal de paquetes transportados: 3\nTotal recaudado: 100$")

if __name__ == "__main__":
    unittest.main()