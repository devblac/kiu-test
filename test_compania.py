import unittest
from paquete import Paquete
from compania import Compania

class TestCompania(unittest.TestCase):
    def setUp(self):
        self.compania = Compania("FlyBondi", 10)
        self.paquete1 = Paquete("Buenos Aires", "Tokio", 5)
        self.paquete2 = Paquete("Madrid", "Nueva York", 3)
        self.paquete3 = Paquete("Lima", "Santiago", 2)

    def test_nombre(self):
        self.assertEqual(self.compania.nombre, "FlyBondi")

    def test_precio(self):
        self.assertEqual(self.compania.precio, 10)

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
        self.assertEqual(reporte, "Reporte de la compañía FlyBondi:\nTotal de paquetes transportados: 3\nTotal recaudado: $100")

if __name__ == "__main__":
    unittest.main(verbosity=2)
