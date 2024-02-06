from paquete import Paquete
from compania import Compania
from cliente import Cliente

compania = Compania("FlyBondi")
cliente1 = Cliente("Juan")
cliente2 = Cliente("Ana")
paquete1 = Paquete(cliente1, compania, "Buenos Aires", "Córdoba", "06/02/2024")
paquete2 = Paquete(cliente2, compania, "Córdoba", "Buenos Aires", "07/02/2024")
paquete3 = Paquete(cliente1, compania, "Buenos Aires", "Rosario", "07/02/2024")

compania.agregar_paquete(paquete1)
compania.agregar_paquete(paquete2)
compania.agregar_paquete(paquete3)

reporte = compania.generar_reporte("06/02/2024")
reporte2 = compania.generar_reporte("07/02/2024")
print("Reporte 1:\n", reporte)
print("Reporte 2:\n", reporte2)
