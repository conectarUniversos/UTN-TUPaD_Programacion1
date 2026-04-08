# Ejercicio 1
print ("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
radio = float(input("Ingrese el radio de un círculo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"el área del círculo es: {area} y su perimetro: {perimetro}")

# Ejercicio 5
segundos = int(input("Ingrese la cantidad de segundos que quiera convertir en horas: "))
horas = segundos // 3600
print(f"{segundos} segundos ingresados equivale a {horas} hora/s")

# Ejercicio 6
numero = int(input("Ingrese un número y tendrás su tabla de multiplicar de dicho número: "))
print(f"Tabla de multiplicar para {numero}")
print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)

# Ejercicio 7
numero1 = int(input("Ingrese un número distinto de cero: "))
numero2 = int(input("Ingrese otro número distinto de cero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplica = numero1 * numero2
divide = numero1 / numero2
print(f"Resultado de la suma: {suma}")
print(f"Resultado de la resta: {resta} ") 
print(f"Resultado de la multiplicación: {multiplica} ") 
print(f"Resultado de la división: {divide}") 

# Ejercicio 8
altura = float(input("Ingrese su altura en metros:"))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura)**2
print(f"Su índice de masa corporal es: {imc}")

# Ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
farenheit = (9/5 * celsius) + 32
print(f"{celsius} Su equivalen a grados Farenheit es: {farenheit}")


# Ejercicio 10
numero1 = int(input("Ingrese un número:"))
numero2 = int(input("Ingrese otro número: "))
numero3 = int(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3)/3
print(f"El promedio de los 3 números ingresado es {promedio}")