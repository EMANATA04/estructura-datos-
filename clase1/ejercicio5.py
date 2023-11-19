"""
Debes hacer un ejercicio donde por medio de un método, el vehículo de marcha y haga un consumo de combustible a medida que este funcione,
cuando llegue a los niveles de combustible definidos en el mensaje anterior, muestre la advertencia y si esta llega a cero, detenga la marcha 
Solución: solución 5 - Plantea tu propia solución y comparte la en clase
"""
class Vehiculo:
    def __init__(self, tipo, marca, combustible):
        self.tipo = tipo
        self.combustible = combustible
        self.marca = marca
        self.encendido = False

    def encender(self):
        if self.combustible >= 10:
            self.encendido = True
            print(f"El {self.tipo} se ha encendido.")
        else:
            print(f"Advertencia: El {self.tipo} necesita ir a la gasolinera. Debe tener minimo un 10% para arrancar.")

    def apagar(self):
        self.encendido = False
        print(f"El {self.tipo} se ha apagado.")

    def avanzar(self, distancia):
        if self.encendido:
            consumo = distancia * 0.50  # Consumo estimado por distancia
            if self.combustible > consumo:
                self.combustible -= consumo
                print(f"{self.tipo} avanzó {distancia} unidades. Combustible restante: {self.combustible:.2f} galones")
                if self.combustible < 5: #Unidades que salta para avanzar el carro
                    print(f"Advertencia: El {self.tipo} necesita ir a la gasolinera.")
                if self.combustible <= 0: