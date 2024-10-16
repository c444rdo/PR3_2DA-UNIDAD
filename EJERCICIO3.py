print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Guardar en un diccionario precios de las frutas en una matriz, luego preguntar al usuario por fruta, un número de kilos y mostrar el precio de ese número de kilos de fruta.
# Si no está la fruta no está en el diccionario debe mostrar un mensaje informando eso mismo

# Guardar los precios de las frutas en un diccionario
precios_frutas = {
    'manzana': 20.5,  # precio por kilo
    'plátano': 10.8,
    'naranja': 20.0,
    'fresa': 40.0
}

# Preguntar al usuario por la fruta y el número de kilos
fruta = input("Ingresa el nombre de la fruta (manzana, plátano, naranja, fresa): ").lower()
kilos = float(input("Ingresa el número de kilos: "))

# Calcular y mostrar el precio
if fruta in precios_frutas:
    precio_total = precios_frutas[fruta] * kilos
    print(f"El precio de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:
    print("La fruta no está en el diccionario.")
