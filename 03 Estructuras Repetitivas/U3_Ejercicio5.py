#Ejercicio 5 "Escape Room:"La Arena del Gladiador"
#NOMBRE DEL PERSONAJE

print("BIENVENIDO")
nombre = input("Nombre del Gladiador: ")


while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

#Estadísticas
vida_jugador = 100
vida_enemigo = 100
pociones = 3

danio_pesado = 15
danio_enemigo = 12

print("INICIO DEL COMBATE")



#CICLO DE COMBATE

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"{nombre} (vida: {vida_jugador}) vs Enemigo (vida: {vida_enemigo}) - Pociones: {pociones}")
    
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # Validación
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido")
        opcion = input("Opción: ")

    opcion = int(opcion)

    
    #ATAQUE PESADO

    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_pesado * 1.5
            print("Golpe crítico")
        else:
            danio = danio_pesado

        vida_enemigo -= danio
        print(f"Atacaste al enemigo por {danio} puntos de daño")

    
    #RÁFAGA VELOZ
    
    elif opcion == 2:
        print("Inicias una ráfaga de golpes")
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")



   
    #CURAR
    
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print("Te curaste sumas 30 puntos de vida")
        else:
            print("No quedan pociones")

    
    #TURNO ENEMIGO
    
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo te atacó por {danio_enemigo} puntos de daño")


#RESULTADO FINAL DEL OMBATE


if vida_jugador > 0:
    print(f"VICTORIA: {nombre} ha ganado la batalla")
else:
    print("DERROTA. Has caído en combate")