#Ejercicio 1 "Caja del Kiosco" 
#Pedir nombre del cliente (No aceptar vacío en nombre. Si queda vacío, es error)
nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre = input("Error. Ingrese un nombre válido (solo letras): ")

#Pedir cantidad de productos. Cantidad > 0 (si ingresa 0, volver a pedir). 
cantidad = input("Ingrese cantidad de productos: ")
while not cantidad.isdigit() or int(cantidad) == 0:
    cantidad = input("Error. Ingrese un número entero mayor a 0: ")


cantidad = int(cantidad)

total_sin_descuento = 0
total_con_descuento = 0

#for para cada producto
for i in range(1, cantidad + 1):
    
    # Pedir precio (entero)
    precio = input(f"Producto {i} - Precio: ")
    while not precio.isdigit():
        precio = input("Error. Ingrese un precio válido (número entero): ")
    
    precio = int(precio)
    
    # Acumulador al total sin descuento
    total_sin_descuento += precio
    
    # Pedir si tiene descuento (S/N)
    descuento = input("¿Tiene descuento? (S/N): ").lower()
    while descuento not in ["s", "n"]:
        descuento = input("Error. Ingrese S o N: ").lower()
    
    # Aplicar descuento si elige s, precio con descuento 90%
    if descuento == "s":
        precio_desc = precio * 0.9
    else:
        precio_desc = precio
    
    # Acumulador al total con descuento
    total_con_descuento += precio_desc



#Cálculos ahorro y promedio
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad


#Mostrar resultados
print("\n--- FACTURA ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")