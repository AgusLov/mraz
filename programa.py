class Pedido():
    def __init__(self,id_cliente,id_pedido,cantidad,proceso) -> None:
        self.id_cliente = id_cliente
        self.id_pedido = id_pedido
        self.cantidad = cantidad
        self.proceso = proceso



id_cliente = input("Colocar id cliente:\n")
id_pedido = input("Colocar ID del pedido:\n")
proceso = input("Cual sera el proceso:\n")
cantidad = input("Cual es la cantidad:\n")

pedido = Pedido(id_cliente,id_pedido,cantidad,proceso)


