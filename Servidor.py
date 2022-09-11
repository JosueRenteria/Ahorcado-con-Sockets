# Declaramos las librerias del programa.
from socket import *
import sys # Terminar la ejecucion del codigo.
import os
import random

# Dirreccion Loopback y puerto de Escucha.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099

# Generamos nuestro socket.
socket_servidor = socket(AF_INET,SOCK_STREAM)
# Establecer la coneccion con el servidor.
socket_servidor.bind((direccion_servidor, puerto_servidor))
socket_servidor.listen()    # Modo escucha del servidor.

# Declaramos las listas de las palabras
palabras_cortas = ['Hola', 'Adios', 'Dia']
palabras_medianas = ['Paracaidas', 'Paracetamol']
palabras_largas = ['Trinidad y Tobago']

#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Funcion para definir una palabra aleatoria.
def crear_cadenas(opcion):
    # Opciones para las palabras.
    if opcion == 1:
        palabra = random.choice(palabras_cortas)
    elif opcion == 2:
        palabra = random.choice(palabras_medianas)
    elif opcion ==  3:
        palabra.choice(palabras_largas)
    
    # Retorno de la funcion crear_cadena.
    secreto = '_'*len(palabra)
    return palabra, secreto

#Funcion para cambiar la letra si se encuentra.
def remplazar_simbolo(palabra, secreto, simbolo):
    cantidad = palabra.count(simbolo)
    inicio = 0

    for i in range(cantidad):
        pos = palabra.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo +secreto[pos+1:]
        inicio = pos + 1
    
    return secreto
#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Mensaje de Bienvenida.
print("BUENVENIDO AL CHAT CON EL CLIENTE")

while True:
    # Establecemos la coneccion.
    socket_conexion, addr = socket_servidor.accept()
    print("Conectamos con el cliente:", addr)

    while True:
        # Recivimos la variable de la opcion que desea el usuario
        opcion_palabra = socket_conexion.recv(4096).decode()
        opcion_palabra_entero =int(opcion_palabra)
        print(f"La opcion de palabras es: {opcion_palabra}")

        # Por si la variable que se escogio es diferente a las opciones.
        if opcion_palabra_entero <= 0 or opcion_palabra_entero > 4:
            print("Opcion erronea.")
            break
        
        #Si se escogio aqui se asigna la palabra que se enviara al Cliente.
        palabra_encontrar, palabra_encontrar_secreto = crear_cadenas(opcion_palabra_entero)

        # Enviar la palabra escondida.
        socket_conexion.send(palabra_encontrar_secreto.encode())
        print(f"La palabra a encontrar es: {palabra_encontrar}")
        print(f"La palabra secreta a encontrar es: {palabra_encontrar_secreto}")

        # Recivimos la letra a buscar en la palabra.
        
    
    # Mensaje de Desconeccion del Cliente
    print("El cliente se esta desconectando", addr)

    # Cerramos conexion.
    socket_conexion.close()
    sys.exit() # Solo por ahora para salir.