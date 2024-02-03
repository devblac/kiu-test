import unittest
from paquete import Paquete

class TestPaquete(unittest.TestCase):
    def setUp(self):
        self.paquete = Paquete("Buenos Aires", "Tokio", 5)

    def test_origen(self):
        self.assertEqual(self.paquete.origen, "Buenos Aires")

    def test_destino(self):
        self.assertEqual(self.paquete.destino, "Tokio")

    def test_peso(self):
        self.assertEqual(self.paquete.peso, 5)

    def test_str(self):
        self.assertEqual(str(self.paquete), "Paquete de Buenos Aires a Tokio con peso 5")

if __name__ == "__main__":
    unittest.main(verbosity=2)