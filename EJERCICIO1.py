print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Guardar en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.
# El usuario debe meter una divisa y debe mostrar el símbolo o un mensaje de que la divisa no está en el diccionario.

# Guardar el diccionario en una variable
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

# Pedir al usuario que ingrese una divisa
entrada = input("Ingresa el nombre de la divisa (Euro, Dollar, Yen): ")

# Mostrar el símbolo o un mensaje si la divisa no está en el diccionario
if entrada in divisas:
    print(f"El símbolo de {entrada} es: {divisas[entrada]}")
else:
    print("La divisa no está en el diccionario.")
