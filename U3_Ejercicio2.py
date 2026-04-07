#Ejercicio 2 "Acceso al Campus y Menú Seguro"
#Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"


intentos = 0
acceso = False

#LOGIN (máx 3 intentos)
while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas")
        intentos += 1



# Si falla 3 veces termina
if not acceso:
    print("Cuenta bloqueada")
else:
    
    #MENÚ cuando ingresa OK
    while True:
        print("\n1) Ver Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")
        
        # Valida que la opción sea un número
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        
        opcion = int(opcion)
        
        # Valida rango del menú
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue
        
        # Opciones del menú
        if opcion == 1:
            print("Inscripto")
        
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            
            # Valida mínimo 6 caracteres
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                continue
            
            confirmar = input("Confirmar clave: ")
            
            if nueva_clave != confirmar:
                print("Error: las claves no coinciden.")
            else:
                clave_correcta = nueva_clave
                print("Clave actualizada correctamente.")
        
        elif opcion == 3:
            print("Seguí así, estas cada vez mas cerca de tu objetivo!!")
        
        elif opcion == 4:
            print("Hasta la próxima!")
            break