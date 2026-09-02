
nombre = input("Cliente: ")

while not nombre.isalpha():
    nombre = input("Nombre inválido. Ingrese nuevamente: ")


cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Cantidad inválida. Ingrese nuevamente: ")

cantidad = int(cantidad)


total_sin_descuentos = 0
total_con_descuentos = 0


for i in range(cantidad):

    precio = input(f"Producto {i + 1} - Precio: ")

    while not precio.isdigit():
        precio = input("Precio inválido. Ingrese nuevamente: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ").lower()

    while descuento != "s" and descuento != "n":
        descuento = input("Ingrese S o N: ").lower()

    total_sin_descuentos += precio

    if descuento == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento


ahorro = total_sin_descuentos - total_con_descuentos
promedio = float(total_con_descuentos) / cantidad


print(f"\nCliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")