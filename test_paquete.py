import unittest
from cliente import Cliente
from compania import Compania
from paquete import Paquete
class TestPaquete(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Ana")
        self.compania = Compania("AeroCarga")
        self.paquete = Paquete(self.cliente, self.compania, "Córdoba", "Buenos Aires", "07/02/2024")

    def test_str(self):
        self.assertEqual(str(self.paquete), "Paquete de Ana enviado por AeroCarga desde Córdoba hasta Buenos Aires el día 07/02/2024 por 10$")

if __name__ == "__main__":
    unittest.main()
