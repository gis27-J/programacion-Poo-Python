from vehiculo import Vehiculo


class Furgoneta(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diiesel")

    def ventanas(self, estado):
        return f"Las ventanas estan {estado} y atras hay espacio para carga"

    def seguridad(self):
        return "Trae sensors de reversa y airbags"
