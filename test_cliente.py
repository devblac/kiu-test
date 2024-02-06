import unittest
from cliente import Cliente
from compania import Compania

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("Juan")
        self.compania = Compania("AeroCarga")

    def test_enviar_paquete(self):
        paquete = self.cliente.enviar_paquete(self.compania, "Buenos Aires", "Córdoba", "06/02/2024")

        self.assertEqual(paquete.cliente, self.cliente)
        self.assertEqual(paquete.compania, self.compania)
        self.assertEqual(paquete.origen, "Buenos Aires")
        self.assertEqual(paquete.destino, "Córdoba")
        self.assertEqual(paquete.fecha, "06/02/2024")

        self.assertEqual(len(self.cliente.paquetes), 1)
        self.assertEqual(self.cliente.paquetes[0], paquete)

        self.assertEqual(len(self.compania.paquetes), 1)
        self.assertEqual(self.compania.paquetes[0], paquete)
        
if __name__ == "__main__":
    unittest.main()
