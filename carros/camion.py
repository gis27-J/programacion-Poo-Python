from vehiculo import Vehiculo


class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "diiesel")

    def ventanas(self, estado):
        return f"Las ventanas estan {estado} y solo tiene ventanas en la cabina"

    def espejos(self, estado):
        return f"Los espejos estan {estado} y son grandes para ver los puntos ciegos"
