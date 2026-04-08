#Ejercicio 4 "Escape Room:La Bóveda"
# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0  #regla anti-spam

# Pedir y validar nombre del agente
agente = input("Nombre del agente: ")
while not agente.isalpha():
    agente = input("Error. Ingrese solo letras: ")

#WHILE PRINCIPAL
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    #Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Se bloquea por alarma. DERROTA.")
        break

    print("\n--- ESTADO ---")
    print(f"Energía: {energia} - Tiempo: {tiempo} - Cerraduras: {cerraduras_abiertas}/3 - Alarma: {alarma}")

    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")
    opcion = input("Opción: ")

    # Validación
    if not opcion.isdigit():
        print("Error: ingrese un número valido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        continue

    
    #MENU DE ACCIONES
    # 1) FORZAR CERRADURA  
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        # Regla anti-spam (3 veces seguidas)
        if racha_forzar == 3:
            print("La cerradura se trabo. Se activa la alarma.")
            alarma = True
            racha_forzar = 0
            continue

        # Riesgo de alarma si energía < 40
        if energia < 40:
            riesgo = input("Riesgo de alarma! Elegí un número (1-3): ")
            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                riesgo = input("Error. Ingrese un número entre 1 y 3: ")

            if int(riesgo) == 3:
                print("Fallaste. Se activó la alarma.")
                alarma = True
                continue

        # Abrir cerradura si no hay alarma
        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta.")

    
    # 2) HACKEAR PANEL

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0  #corta la racha

        print("Hackeando")
        for i in range(4):
            codigo_parcial += "*"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Hackeo completo. Cerradura abierta.")

    
    # 3) DESCANSAR
    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1
        racha_forzar = 0  #corta la racha

        if alarma:
            energia -= 10
            print("La alarma drena energía extra.")

        print("Descansaste")

#RESULTADO FINAL

if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")