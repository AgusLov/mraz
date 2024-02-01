class EmpresaMetalurgica:
    def __init__(self):
        self.inventario = {
            "GALVANIZADA": 0,
            "NEGRA": 0,
            "ACERO INOXIDABLE": 0
        }

    def consultar_producto(self, producto):
        if producto not in self.inventario:
            print("El producto no existe.")
            return
        print(f"Cantidad de {producto} en el inventario: {self.inventario[producto]}")

    def agregar_producto(self, producto, cantidad):
        if producto not in self.inventario:
            print("El producto no existe.")
            return
        self.inventario[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de {producto} al inventario.")

    def quitar_producto(self, producto, cantidad):
        if producto not in self.inventario:
            print("El producto no existe.")
            return
        if cantidad > self.inventario[producto]:
            print(f"No hay suficientes unidades de {producto} en el inventario.")
            return
        self.inventario[producto] -= cantidad
        print(f"Se han quitado {cantidad} unidades de {producto} del inventario.")

    def main(self):
        while True:
            accion = input("Ingrese 'consultar' para ver el inventario, 'agregar' para agregar unidades, 'quitar' para quitar unidades, o 'salir' para terminar el programa: ").lower()
            if accion == "consultar":
                producto = input("Ingrese el producto a consultar (GALVANIZADA, NEGRA, ACERO INOXIDABLE): ").upper()
                self.consultar_producto(producto)
            elif accion == "agregar":
                producto = input("Ingrese el producto al que desea agregar unidades (GALVANIZADA, NEGRA, ACERO INOXIDABLE): ").upper()
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                self.agregar_producto(producto, cantidad)
            elif accion == "quitar":
                producto = input("Ingrese el producto del que desea quitar unidades (GALVANIZADA, NEGRA, ACERO INOXIDABLE): ").upper()
                cantidad = int(input("Ingrese la cantidad a quitar: "))
                self.quitar_producto(producto, cantidad)
            elif accion == "salir":
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    empresa = EmpresaMetalurgica()
    empresa.main()