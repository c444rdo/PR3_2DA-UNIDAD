print ("Martínez Estrada Ricardo / NO. de control: 1193 / 08.10.2024 / Práctica 2")
print (" ")

# Preguntar al usuario nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# Preguntar al usuario por sus datos
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu número de teléfono: ")

# Guardar los datos en un diccionario
usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

# Mostrar el mensaje
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
