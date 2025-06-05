class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_en_stock = cantidad_en_stock
    
    def obtener_valor_total(self):
        return self.precio * self.cantidad_en_stock


class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
    
    def mostrar_inventario(self):
        print("=== INVENTARIO ===")
        if not self.productos:
            print("El inventario está vacío")
            return
        
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: ${producto.precio}")
            print(f"Cantidad: {producto.cantidad_en_stock}")
            print(f"Valor total: ${producto.obtener_valor_total()}")
            print("-" * 30)
    
    def calcular_valor_total_inventario(self):
        total = 0
        for producto in self.productos:
            total += producto.obtener_valor_total()
        return total


if __name__ == "__main__":
    inventario = Inventario()
    
    producto1 = Producto("Laptop", 1200.00, 10)
    producto2 = Producto("Mouse", 25.50, 50)
    producto3 = Producto("Teclado", 80.00, 30)
    producto4 = Producto("Monitor", 350.00, 15)
    producto5 = Producto("Auriculares", 45.99, 25)
    
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    inventario.agregar_producto(producto3)
    inventario.agregar_producto(producto4)
    inventario.agregar_producto(producto5)
    
    inventario.mostrar_inventario()
    
    print(f"\nValor total del inventario: ${inventario.calcular_valor_total_inventario()}")
    
    producto_buscado = inventario.buscar_producto("Mouse")
    if producto_buscado:
        print(f"\nProducto encontrado: {producto_buscado.nombre}")
        print(f"Precio: ${producto_buscado.precio}")
        print(f"Cantidad en stock: {producto_buscado.cantidad_en_stock}")
    else:
        print("\nProducto no encontrado")
    
    producto_no_existe = inventario.buscar_producto("Impresora")
    if producto_no_existe:
        print(f"Producto encontrado: {producto_no_existe.nombre}")
    else:
        print("\nBúsqueda de 'Impresora': Producto no encontrado")