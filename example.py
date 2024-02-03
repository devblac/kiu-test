from paquete import Paquete
from compania import Compania

compania = Compania("FlyBondi", 10)

paquete1 = Paquete("Buenos Aires", "Tokio", 5)
paquete2 = Paquete("Madrid", "Nueva York", 3)
paquete3 = Paquete("Lima", "Santiago", 2)

compania.transportar(paquete1)
compania.transportar(paquete2)
compania.transportar(paquete3)

reporte = compania.reporte()
print(reporte)
