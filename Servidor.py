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

# Declaramos las listas de las palabras.
palabras_cortas = ['hola', 'adios', 'dia', 'noche', 'casa', 'perros', 'gatos', 'estres', 'ahorrar', 'distancia']
palabras_medianas = ['paracaidas', 'paracetamol', 'ovoviviparo', 'caleidoscopio', 'electrolisis', 'ferrocarril', 'remolachas', 'tecnologia', 'multicolinealidad', 'paralelepipedos']
palabras_largas = ['trinidad y tobago', 'dias soleados', 'politecnico nacional', 'escuela superior de computo', 'maquinas inteligentes', 'cientificos tecnologicos', 'manejo de informacion', 'improvisacion de un humano', 'logica programable', 'inteligencia emocional']

#-------------------------------------------------------FUNCIONES-------------------------------------------------------
# Funcion para definir una palabra aleatoria.
def crear_cadenas(opcion):
    # Opciones para las palabras.
    if opcion == 1:
        palabra = random.choice(palabras_cortas) # Eleccion de palabras cortas.
    elif opcion == 2:
        palabra = random.choice(palabras_medianas) # Eleccion de palabras medianas.
    elif opcion ==  3:
        palabra = random.choice(palabras_largas) # Eleccion de palabras largas.
    
    # Retorno de la funcion crear_cadena.
    secreto = '_'*len(palabra)
    return palabra, secreto

#Funcion para cambiar la letra si se encuentra.
def remplazar_simbolo(palabra, secreto, simbolo):
    cantidad = palabra.count(simbolo)
    inicio = 0

    # Bucle para cambiar las letras en la palabra secreta.
    for i in range(cantidad):
        pos = palabra.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo +secreto[pos+1:]
        inicio = pos + 1
    
    return secreto
#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Mensaje de Bienvenida.
print("\tBIENVENIDO AL CHAT CON EL CLIENTE")

while True:
    # Establecemos la coneccion.
    socket_conexion, addr = socket_servidor.accept()
    print("Conectamos con el cliente:", addr)

    while True:
        # Recivimos la variable de la opcion que desea el usuario
        opcion_palabra = socket_conexion.recv(4096).decode()
        opcion_palabra_entero =int(opcion_palabra)
        print(f"La opcion de la palabras escogida por el Cliente {addr} es: {opcion_palabra}")

        # Por si la variable que se escogio es diferente a las opciones.
        if opcion_palabra_entero <= 0 or opcion_palabra_entero >= 4:
            # Salida del cliente (el cliente decidio salir del juego y rompemos los procesos).
            print(f"El Cliente {addr} decidio salir del Juego.")
            break
        
        #Si se escogio aqui se asignan las palabra que se enviaran al Cliente.
        palabra_encontrar, palabra_encontrar_secreto = crear_cadenas(opcion_palabra_entero)
        palabra_encontrar_secreto = remplazar_simbolo(palabra_encontrar, palabra_encontrar_secreto, ' ')

        # Envio de la palabra secreta y de la palabra original.
        socket_conexion.send(palabra_encontrar_secreto.encode())
        mensaje = socket_conexion.recv(1024) # Resivimos el mensaje de que el cliente resivio la palabra a encontrar.
        print(mensaje)
        socket_conexion.send(palabra_encontrar.encode())
        print(f"\nLa palabra secreta a encontrar es: {palabra_encontrar_secreto}")
        print(f"La palabra original a encontrar es: {palabra_encontrar}")

        # Inicializacion de las vidas que tendra el cliente.
        Vidas = 5

        # Ciclo para buscar las palabras que nos da el cliente, y las remplaza en la palabra secreta (para enviarlo al cliente).
        while Vidas > 0:
            # Resivimos la letra a buscar y se remplazan las letras.
            letra = socket_conexion.recv(4096).decode()
            palabra_nueva = remplazar_simbolo(palabra_encontrar, palabra_encontrar_secreto, letra)
            palabra_encontrar_secreto = palabra_nueva

            # Enviamos la nueva palabra resultante (al utilizar la funcion "remplazar_simbolo").
            socket_conexion.send(palabra_nueva.encode())

            # Optencion de las vidas que le quedan al cliente en su partida.
            Vidas_letra = socket_conexion.recv(4096).decode()
            Vidas = int(Vidas_letra)
            socket_conexion.sendall(b"Vidas Resividas.") # Enviamos el mensaje de llegada de vidas al cliente.

    # Mensaje de Desconeccion del Cliente cuando desea salir del juego.
    print("El cliente se esta desconectando", addr)

    # Cerramos conexion.
    socket_conexion.close()
    sys.exit() # Solo por ahora para salir.