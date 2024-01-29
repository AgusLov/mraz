import sys
from menuprocesoai import carga_instrucciones


class Pedido():
    def __init__(self, id_cliente, id_pedido, cantidad, proceso, stage) -> None:
        self.id_cliente = id_cliente
        self.id_pedido = id_pedido
        self.cantidad = int(cantidad)
        self.proceso = proceso
        self.stage = stage

def cut(pedido):
    print(f"Processing {pedido.cantidad} items with cut process...")

def folded(pedido):
    print(f"Processing {pedido.cantidad} items with folded process...")

def laser(pedido):
    print(f"Processing {pedido.cantidad} items with laser process...")

def main():
    proceso = carga_instrucciones()
    
    id_cliente = input("Colocar id cliente:\n")
    id_pedido = input("Colocar ID del pedido:\n")
    cantidad = input("Cual es la cantidad:\n")

    pedido = Pedido(id_cliente, id_pedido, cantidad, None, 'Started')

    print("Select a stage:")
    print("1. Started")
    print("2. Finished")
    print("3. PPending")

    stage_choice = input("Enter the number of your choice: ")

    if stage_choice == '3':
        print(f"Missing processes: {['Cut', 'Folded', 'Laser'] - {pedido.proceso}}")
        print("Select a missing process:")
        missing_process_choice = input("Enter the number of your choice: ")

        if missing_process_choice in ('1', '2', '3'):
            if missing_process_choice == '1' and 'Cut' not in pedido.proceso:
                cut(pedido)
                pedido.stage = 'PPending'
            elif missing_process_choice == '2' and 'Folded' not in pedido.proceso:
                folded(pedido)
                pedido.stage = 'PPending'
            elif missing_process_choice == '3' and 'Laser' not in pedido.proceso:
                laser(pedido)
                pedido.stage = 'PPending'
            else:
                print("Invalid choice. Exiting...")
                sys.exit(1)
        else:
            print("Invalid choice. Exiting...")
            sys.exit(1)
    else:
        pedido.stage = stage_choice

    print(f"Pedido: id_cliente={pedido.id_cliente}, id_pedido={pedido.id_pedido}, cantidad={pedido.cantidad}, proceso={pedido.proceso}, stage={pedido.stage}")

if __name__ == "__main__":
    main()