class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.prendido = False
        self.velocidad = 0

    def prender(self):
        self.prendido = True
        return f"El {self.modelo} prende el motor"

    def apagar(self):
        self.prendido = False
        self.velocidad = 0
        return f"El {self.modelo} apaga el motor"

    def aceleracion_y_frenado(self, accion, velocidad):
        verbos = {"acelerar": ("acelera", velocidad), "frenar": ("frena", -velocidad)}
        verbo, cambio = verbos[accion]
        self.velocidad += cambio
        return f"El {self.modelo} {verbo} y va a {self.velocidad} km/h"

    def direccion(self, tipo):
        return f"Tiene direccion {tipo}"

    def climatizador(self, estado):
        return f"El aire acondicionado esta {estado}"

    def seguridad(self):
        return "Trae cinturones y bolsas de aire"

    def faros(self, estado):
        return f"Los faros estan {estado}"

    def ventanas(self, estado):
        return f"Las ventanas estan {estado}"

    def espejos(self, estado):
        return f"Los espejos estan {estado}"
