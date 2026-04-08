#Ejercicio 1
edad = int(input("Ingrese su edad: ")) 
if edad >= 18: # Se evalúa si la edad ingresada es mayor o igual a 18 para determinar mayoría de edad
    print("Es mayor de edad")
else: # Si no cumple la condición anterior, automáticamente es menor de edad
    print("Es menor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6: # Se compara la nota con el mínimo requerido para aprobar (6)
    print("Aprobado")
else: # Si la nota es menor a 6, se considera desaprobado
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0: # Se usa el operador módulo (%) para verificar si el resto de dividir por 2 es 0 (número par)
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12: # Se clasifican las edades en rangos utilizando condiciones encadenadas
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un/a adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un/a adulto joven")
else:
    print("Es adulto")

#Ejercicio 5
clave = input("Introduzca una clave entre 8 y 14 digitos: ")
if 8 <= len(clave) <= 14: # Se evalúa si la longitud del texto está dentro del rango permitido
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
consumo = int(input("Ingrese su consumo mensual de energía eléctrica: "))
if consumo <= 150: # Se clasifica el consumo en distintos niveles según rangos numéricos
    print("Consumo bajo")
elif 151 <= consumo <= 300:
    print("Consumo medio")
elif 301 <= consumo <= 499:
    print("Consumo alto")
else:
    print("Considere medidas de ahorro energético")

#Ejercicio 7
palabra = input("Ingrese una frase o palabra:" )
if palabra[-1].lower() in "aeiou": # Se toma el último carácter del string y se pasa a minúscula para comparar
    print(palabra + "!")
else:
    print(palabra)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
menu = input("Ingrese una opción (1, 2 o 3):")
# Se evalúa la opción elegida para aplicar una transformación al string
if menu == "1":
    print(nombre.upper())
elif menu == "2":
    print(nombre.lower())
elif menu == "3":
    print(nombre.title())
else:
    print("opción invalida")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terreno: "))
# Se clasifican las magnitudes en rangos según la escala de Richter
if magnitud < 3:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

#Ejercicio 10
hemisferio = input(("Ingrese en que hemisferio se encuentra (S/N): "))
hemisferio = hemisferio.upper()

mes = int(input("Ingrese el mes expresado en numeros: "))
dia = int(input("Ingrese el día expresado en numeros: "))
# Se determina la estación según hemisferio y fecha (mes + día)
if hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in (1,2) or (mes == 3 and dia <= 20)):
        print ("Estas en Verano")
    elif (mes == 3 and dia >= 21) or (mes in (4,5) or (mes == 6 and dia <= 20)):
        print ("Estas en Otoño")
    elif (mes == 6 and dia >= 21) or (mes in (7,8) or (mes == 9 and dia <= 20)):
        print ("Estas en Invierno")
    elif (mes == 9 and dia >= 21) or (mes in (10,11) or (mes == 12 and dia <= 20)):
        print ("Estas en Primavera")
elif hemisferio == "N": # Mismas fechas pero estaciones invertidas respecto al hemisferio sur
    if (mes == 12 and dia >= 21) or (mes in (1,2) or (mes == 3 and dia <= 20)):
        print ("Estas en Invierno")
    elif (mes == 3 and dia >= 21) or (mes in (4,5) or (mes == 6 and dia <= 20)):
        print ("Estas en Primavera")
    elif (mes == 6 and dia >= 21) or (mes in (7,8) or (mes == 9 and dia <= 20)):
        print ("Estas en Verano")
    elif (mes == 9 and dia >= 21) or (mes in (10,11) or (mes == 12 and dia <= 20)):
        print ("Estas en Otoño")
else: # Si el hemisferio no es válido, se informa al usuario
    print("Hemisferio inválido")