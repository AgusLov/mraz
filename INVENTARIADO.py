class EmpresaMetalurgica:
    def __init__(self):
        self.inventario = {
            "GALVANIZADA": 1000,
            "NEGRA": 2000,
            "ACERO INOXIDABLE": 3000
        }

    def consultar_producto(self, producto):
        if producto not in self.inventario:
            print("El producto no existe.")
            return
        print(f"Cantidad de {producto} en el inventario: {self.inventario[producto]}")
        ingreso_material = input("¿Desea agregar cantidades a los tipos de productos? (S/N): ").upper()
        while ingreso_material != "S" and ingreso_material != "N":
            print("Opción no válida.")
            ingreso_material = input("¿Desea agregar cantidades a los tipos de productos? (S/N): ").upper()
        if ingreso_material == "S":
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            self.inventario[producto] += cantidad
            print(f"Se han agregado {cantidad} unidades de {producto} al inventario.")

    def main(self):
        producto = input("Ingrese el producto a consultar (GALVANIZADA, NEGRA, ACERO INOXIDABLE): ").upper()
        self.consultar_producto(producto)
        print(f"La cantidad actual de unidades del producto {producto} es: {self.inventario[producto]}")

if __name__ == "__main__":
    empresa = EmpresaMetalurgica()
    empresa.main()