from socket import *
import sys # Terminar la ejecucion del codigo.

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099 

# Declaracion del socket del cliente.
socket_cliente = socket(AF_INET, SOCK_STREAM)
socket_cliente.connect((direccion_servidor, puerto_servidor))


#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Funcion para el encabezado de inicio del juego.
def Encabezado(vidas, palabra_secreta):
    # Opciones para las palabras.
    print("----Bienvenido al Juego del Ahorcado----\n")
    print(f"Te quedan {vidas} vidas.\n\n")
    print("La palabra a Encotrar es:")
    print(f"\t{palabra_secreta}")
    
# Funcion para ver si las palabras son iguales.
def Comparacion(palabra_antugua, palabra_nueva, palabra_final, vidas):
    # Opciones para las palabras.
    if palabra_antugua == palabra_nueva:
        palabra_antugua = palabra_nueva
        print("La Letra que escogiste fue correcta.")
    elif palabra_antugua == palabra_final:
        vidas = 0
        print(f"Filicidades Acabas de Encontrar la Palabra, que era: {palabra_final}")
    else:
        vidas = vidas - 1
        print("La Letra que escogiste fue erronea.")
    
    # Retorno de la funcion
    return palabra_antugua, vidas

#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Mensaje de Bienvenida.
print("BUENVENIDO AL CHAT CON EL SERVIDOR")

while True:
    # Entradas del programa.
    print("\nBienvenido al juego del Ahorcado escoge alguna de las siguientes opciones:\n")
    print("   1_Palabra Corta.\n")
    print("   2_Palabra Mediana.\n")
    print("   3_Palabra Larga.\n")
    print("   Cualquier otro numero para 'Salir'.\n")
    opcion_palabra = input()
    opcion_palabra_entero = int(opcion_palabra)

    # Por si la variable que se escogio es diferente a las opciones indicadas.
    if opcion_palabra_entero <= 0 or opcion_palabra_entero >= 4:
        # Eviamos mensaje.
        socket_cliente.send(opcion_palabra.encode())

        # Cerramos socket.
        socket_cliente.close()
        sys.exit()
    
    # Else para la condicion que si se optuvo correctamente.
    else:

        # Enviar Mensaje (Opcion a elegir de palabras).
        socket_cliente.send(opcion_palabra.encode())
        
        # Inicializacion de Vidas del Juego.
        Vidas = 5

        # Resivimos mensaje del Servidor (la palabra a Buscar en Secreto).
        palabra_encontrar_secreto = socket_cliente.recv(4096).decode()
        print(f"Servidor-{palabra_encontrar_secreto}")
#############################################################################################################################333
        # Resivimos mensaje del Servidor (la palabra a Buscar).
        palabra_final = palabra_encontrar_secreto = socket_cliente.recv(4096).decode()

        while Vidas > 0:
            # Encabezado para decir la palabra.
            Encabezado(Vidas, palabra_encontrar_secreto)

            # Ingresar la letra a encontra.
            print("Ingresa la letra a escoger")
            letra = input()

            # Enviamos la letra a encontrar.
            socket_cliente.send(letra.encode())

            # Recivimos palabra nueva.
            palabra_nueva = socket_cliente.recv(4096).decode()

            # Aqui se compararan las palabras. 
            palabra_encontrar_secreto, Vidas = Comparacion(palabra_encontrar_secreto, palabra_nueva, palabra_final, Vidas)




