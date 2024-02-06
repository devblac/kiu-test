import unittest
from cliente import Cliente
from paquete import Paquete
from compania import Compania
class TestCompania(unittest.TestCase):

    def setUp(self):
        self.compania = Compania("FlyBondi")
        self.cliente1 = Cliente("Juan")
        self.cliente2 = Cliente("Ana")

    def test_agregar_paquete(self):
        paquete1 = Paquete(self.cliente1, self.compania, "Buenos Aires", "Córdoba", "06/02/2024")
        paquete2 = Paquete(self.cliente2, self.compania, "Córdoba", "Buenos Aires", "07/02/2024")
        self.compania.agregar_paquete(paquete1)
        self.compania.agregar_paquete(paquete2)
        self.assertEqual(len(self.compania.paquetes), 2)
        self.assertEqual(self.compania.paquetes[0], paquete1)
        self.assertEqual(self.compania.paquetes[1], paquete2)

    def test_generar_reporte(self):
        paquete1 = Paquete(self.cliente1, self.compania, "Buenos Aires", "Córdoba", "06/02/2024")
        paquete2 = Paquete(self.cliente2, self.compania, "Córdoba", "Buenos Aires", "06/02/2024")
        paquete3 = Paquete(self.cliente1, self.compania, "Buenos Aires", "Rosario", "07/02/2024")
        self.compania.agregar_paquete(paquete1)
        self.compania.agregar_paquete(paquete2)
        self.compania.agregar_paquete(paquete3)
        reporte = self.compania.generar_reporte("06/02/2024")
        self.assertEqual(reporte, "Reporte de la Compania FlyBondi para el día 06/02/2024:\nTotal de paquetes transportados: 2\nTotal recaudado: 20$")

if __name__ == "__main__":
    unittest.main()
