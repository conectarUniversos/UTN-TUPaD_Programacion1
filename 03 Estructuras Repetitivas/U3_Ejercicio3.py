#Ejercicio 3 "Agenda de Turnos con Nombres"
#Días con turnos disponibles
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

#Nombre del Operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Error. Ingrese solo letras: ")

#MENU
while True:
    print("\n1) Reservar turno  2) Cancelar turno  3) Ver agenda  4) Resumen  5) Salir")
    opcion = input("Opción: ")
    #Verifica opcion
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    # 1)RESERVA UN TURNO
    
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            dia = input("Error. Ingrese 1 o 2: ")
        dia = int(dia)

        nombre = input("Nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        # VALIDA SI EL NOMBRE ES REPETIDO
        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error: ya existe ese turno.")
                continue

            if lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles.")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: ya existe ese turno.")
                continue

            if martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles.")

    
    #2)CANCELA UN TURNO
    

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            dia = input("Error. Ingrese 1 o 2: ")
        dia = int(dia)

        nombre = input("Nombre paciente: ")
        while not nombre.isalpha():
            nombre = input("Error. Solo letras: ")

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No encontrado.")

        else:
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado.")
                

    
    #3)VER AGENDA DEL DIA
    
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) not in [1, 2]:
            dia = input("Error. Ingrese 1 o 2: ")
        dia = int(dia)

        if dia == 1:
            print("Lunes:")
            print("1:", lunes1 if lunes1 != "" else "(libre)")
            print("2:", lunes2 if lunes2 != "" else "(libre)")
            print("3:", lunes3 if lunes3 != "" else "(libre)")
            print("4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Martes:")
            print("1:", martes1 if martes1 != "" else "(libre)")
            print("2:", martes2 if martes2 != "" else "(libre)")
            print("3:", martes3 if martes3 != "" else "(libre)")

    
    # 4)VER RESUMEN
    
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("Lunes - Ocupados:", ocupados_lunes, "Libres:", 4 - ocupados_lunes)
        print("Martes - Ocupados:", ocupados_martes, "Libres:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    
    # 5)SALIR
    elif opcion == 5:
        print("SALIR")
        break