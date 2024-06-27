try:
    entradas_vendidas = 0
    entradas_totales = 0
    def mostrar_escenario(escenario):
        print("\t\t\t ESCENARIO\n")
        for contador_entradas in range(0, 50, 10):
            fila = ""
            for contador_filas in range(10):
                fila += f"{escenario[contador_entradas + contador_filas]}\t"
            print(fila)
        print("\n")

    def comprar_entradas(escenario):
        precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
                6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
                11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
                16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
                21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
                26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
                31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
                36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
                41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
                46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}

        cantidad = int(input("Ingrese la cantidad de entradas a comprar (Sólo deben ser 1 o 2): \n"))
        if cantidad < 1 or cantidad > 2:
            print("Cantidad inválida.")
            return

        for _ in range(cantidad):
            mostrar_escenario(escenario)
            asiento = int(input("Seleccione el número del asiento que desea comprar: \n"))
            if escenario[asiento - 1] == 'X':
                print("El asiento no está disponible.")
                return
            escenario[asiento - 1] = 'X'
            precio = precios[asiento]
            run = input("Ingrese el RUN del titular de la entrada (sin guión ni puntos): \n")
            (nombre) = (input("Ingrese su nombre y apellido: \n"))
            print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}, {nombre}.\n")

    escenario = []
    for contador_agregar in range(1, 51):
        escenario.append(str(contador_agregar))

    while True:
        print ("Sanchez Producciones\n")
        print ("------------MENÚ USUARIO-------------\n")
        print ("Ingrese una opción")
        print ("1. Ingresar como comprador")
        print ("2. Ingresar como trabajador")
        Opcion_inicio = int(input(""))

        if Opcion_inicio == 1:
            print ("Sanchez Producciones\n")
            print ("------------MENÚ USUARIO-------------\n")
            print("1. Comprar entradas")
            print("2. Mostrar ubicaciones disponibles")
            print ("3. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                print ("\n--------PRECIOS DE LAS ENTRADAS--------\n")
                print (" 1.	VIP, $100.000. (Asientos del 1 al 20)\n", "2.	Normal $50.000. (Asientos del 21 al 30)\n", "3.	Económico, $10.000. (Asientos del 31 al 50)\n")
                comprar_entradas(escenario)
            elif opcion == '2':
                mostrar_escenario(escenario)
            elif opcion == '5':
                print("¡Gracias por utilizar el sistema de ventas!")
                break
            else:
                print("Opción inválida. Por favor, seleccione nuevamente.\n")

        if Opcion_inicio == 2:
            print ("------------MENÚ EMPRESA-----------\n")
            print ("1. Ganacias del local")
            print ("2. Lista de asistentes")
            print ("3. SALIR")
            opcion_Usuario = int(input("\nIngrese la opción que desea ejecutar\n"))

            match (opcion_Usuario):

                case 1:
                    print ("GANACIAS DEL LOCAL")
                    for contador_ventas in (escenario):
                        ventas = entradas_vendidas
                    #No puedo concentrarme y no practiqué. Le he fallado profe
                case 2: 
                    print("") #Le fallé profe. Lo siento mucho
                    #Voy a estudiar mucho para el exámen final
except:
    print ("Ha ocurrido un error")
