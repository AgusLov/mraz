
def carga_instrucciones():
    cont = 0
    finproceso = False
    while cont < 8 and not finproceso:
        print("Select a process:")
        print("1. Guillotina")
        print("2. Laser")
        print("3. Plegado")

        stage_choice = int(input("Enter the number of your choice: "))  # Convertir la entrada a entero
        proceso = []

        # Cambiar el bucle while para verificar la entrada correcta
        while stage_choice not in [1, 2, 3]:
            print("Opcion no valida. Ingrese nuevamente...")
            stage_choice = int(input("Enter the number of your choice: "))

        # Utilizar elif en lugar de varios if para seleccionar el proceso
        if stage_choice == 1:
            proceso.append("G")
        elif stage_choice == 2:
            proceso.append("L")
        elif stage_choice == 3:
            proceso.append("P")

        cont += 1

        print("Hay mas procesos?")
        print("1. Si")
        print("2. No")

        continuar_proceso = int(input("Enter the number of your choice: "))

        # Cambiar el bucle while para verificar la entrada correcta
        while continuar_proceso not in [1, 2]:
            print("Opcion no valida. Ingrese nuevamente...")
            continuar_proceso = int(input("Enter the number of your choice: "))

        if continuar_proceso == 2:  # Verificar si el usuario quiere terminar
            finproceso = True
            break  # Salir del bucle principal cuando el usuario decide terminar
        
    return proceso
