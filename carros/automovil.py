from vehiculo import Vehiculo


class Automovil(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def seguridad(self):
        return "Trae ABS, airbags y control de estabilidad"

    def direccion(self, tipo):
        return f"Tiene direccion {tipo} muy sport"
