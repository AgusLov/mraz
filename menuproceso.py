cont=0
finproceso=False
while cont<8 and not finproceso:
    print("Select a process:")
    print("1. Guillotina")
    print("2. Laser")
    print("3. Plegado")

    stage_choice = input("Enter the number of your choice: ")
    proceso = []
    while stage_choice in [1,2,3]:
        if stage_choice == 1:
            proceso.append("G")
            break
        elif stage_choice == 2:
            proceso.append("L")
            break
        elif stage_choice == 3:
            proceso.append("P")
            break
        else:
            print("Opcion no valida. Ingrese nuevamente...")
            stage_choice = input("Enter the number of your choice: ")
    cont+=1
    print("Hay mas procesos?")
    print("1. Si")
    print("2. No")
    continuar_proceso = input("Enter the number of your choice: ")
    
    while continuar_proceso in [1,2]:
        if stage_choice == 1:
            break
        elif stage_choice == 2:
            finproceso=True
            break
        else:
            print("Opcion no valida. Ingrese nuevamente...")
            continuar_proceso = input("Enter the number of your choice: ")   
    
    
    
print("termino el programa...")