from vehiculo import Vehiculo
from automovil import Automovil
from furgoneta import Furgoneta
from camion import Camion

auto_deportivo = Automovil("Deportivo negro", "negro", "4.0", 2, 2)
van_blanca = Furgoneta("Van de reparto", "blanca", "2.2", 4, 3)
volqueta = Camion("Volqueta blanca", "blanco", "7.0", 2, 3)

print(auto_deportivo.prender())
print(auto_deportivo.aceleracion_y_frenado("acelerar", 120))
print(auto_deportivo.aceleracion_y_frenado("frenar", 60))
print(auto_deportivo.apagar())
print(auto_deportivo.direccion("asistida"))
print(auto_deportivo.climatizador("encendido"))
print(auto_deportivo.seguridad())
print(auto_deportivo.faros("encendidos"))
print(auto_deportivo.ventanas("abiertas"))
print(auto_deportivo.espejos("plegados"))

print(van_blanca.prender())
print(van_blanca.ventanas("cerradas"))
print(van_blanca.seguridad())

print(volqueta.prender())
print(volqueta.ventanas("cerradas"))
print(volqueta.espejos("abiertos"))
