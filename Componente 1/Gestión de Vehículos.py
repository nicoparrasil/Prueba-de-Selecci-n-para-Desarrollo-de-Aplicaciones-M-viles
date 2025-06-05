class Vehiculo:
    def __init__(self, marca, modelo, tiempo, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.tiempo = tiempo
        self.kilometraje = kilometraje
    
    def mostrar_info(self):
        print("=== INFORMACION DEL VEHICULO ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tiempo: {self.tiempo}")
        print(f"Kilometraje: {self.kilometraje} km")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, tiempo, kilometraje, numero_puertas):
        super().__init__(marca, modelo, tiempo, kilometraje)
        self.numero_puertas = numero_puertas
    
    def mostrar_info(self):
        print("=== INFORMACION DEL COCHE ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"tiempo: {self.tiempo}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Numero de puertas: {self.numero_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tiempo, kilometraje, cilindrada):
        super().__init__(marca, modelo, tiempo, kilometraje)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        print("=== INFORMACION DE LA MOTOCICLETA ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"tiempo: {self.tiempo}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Cilindrada: {self.cilindrada} cc")


if __name__ == "__main__":
    mi_coche = Coche("Toyota", "Corolla", 2020, 45000, 4)
    mi_moto = Motocicleta("Honda", "CBR600RR", 2019, 12000, 600)
    coche_deportivo = Coche("Lamborghini", "Gallardo", 2015, 8000, 2)
    
    mi_coche.mostrar_info()
    print()
    mi_moto.mostrar_info()
    print()
    coche_deportivo.mostrar_info()
    
    vehiculos = [mi_coche, mi_moto, coche_deportivo]
    
    print("\nTodos los vehiculos:")
    for vehiculo in vehiculos:
        vehiculo.mostrar_info()
        print()