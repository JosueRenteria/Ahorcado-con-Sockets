from socket import *
import sys # Terminar la ejecucion del codigo.
import os # Utilizar funciones del cmd

# Dirreccion Loopback y puerto de Envio.
direccion_servidor = "127.0.0.1"
puerto_servidor = 9099 

# Declaracion del socket del cliente.
socket_cliente = socket(AF_INET, SOCK_STREAM)
socket_cliente.connect((direccion_servidor, puerto_servidor))

#-------------------------------------------------------FUNCIONES-------------------------------------------------------
# Funcion para el encabezado de inicio del juego (estilos del programa).
def Encabezado(vidas, palabra_secreta):
    # Opciones para las palabras.
    print("\t----------------------------------------")
    print("\t----Bienvenido al Juego del Ahorcado----")
    print("\t----------------------------------------\n")
    print(f"Te quedan {vidas} vidas.\n\n")
    print(f"La palabra a Encotrar es:\t{palabra_secreta}\n")
    
# Funcion para la comparacion de palabras y saber si son iguales.
def Comparacion(palabra_antigua, palabra_nueva, vidas):
    # Opciones cuando la palabra secreta es diferente a la palabra secreta resivida por el Servidor.
    if palabra_antigua != palabra_nueva:
        palabra_antigua = palabra_nueva
        print("La Letra que escogiste fue correcta.")

    # Cuando la letra es incorrecta y la palabra secreta es igual a la palabra secreta resivida por el Servidor.
    else:
        palabra_antigua = palabra_nueva
        vidas = vidas - 1 # Restacion de vidas.
        print("La Letra que escogiste fue erronea.")
    
    # Retorno de la funcion
    return palabra_antigua, vidas

# Encabezado cuando el jugador a Ganado.
def Marco_ganador():
    os.system('cls') # Borramos pantalla.
    print("\t#############################")
    print("\t#FELICIDADES ACABAS DE GANAR#")
    print("\t#############################")
    
# Encabezado cuando el jugador a Perdido.
def Marco_perdedor():
    os.system('cls') # Borramos pantalla.
    print("\t#########################")
    print("\t#LO SENTIMOS HAS PERDIDO#")
    print("\t#########################")
        
# Dibujo del Ahorcado dependiendo de los intentos.
def ImprimirAhorcado(vidas):
    if vidas == 0:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif vidas == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif vidas == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif vidas == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif vidas == 4:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif vidas == 5:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
#-------------------------------------------------------FUNCIONES-------------------------------------------------------

# Mensaje de Bienvenida.
print("\t\tBUENVENIDO AL CHAT CON EL SERVIDOR")

while True:
    # Menu inicial para ingresar la opcion de palabras a elegir.
    print("\nBienvenido al juego del Ahorcado escoge alguna de las siguientes opciones:\n")
    print("\t1_Palabra Corta.")
    print("\t2_Palabra Mediana.")
    print("\t3_Palabra Larga.")
    print("\tCualquier otro numero para 'Salir'.\n")
    opcion_palabra = input("Ingresa la opcion escogida: ") #Opcion elegida por el usuario.

    # Saber si la opcion que se eligio es un numero y si no lo es que vuelva a ingresar la opcion a elegir.
    if (opcion_palabra.isnumeric()) == False: # .isnumeric sirve para saber 
        print("\nNOTA: El dato que se ingreso no es un numero, porfavor ingresa un valor correcto.")
        os.system('pause') # Pausamos la pantalla.
        os.system('cls') # Borramos pantalla.

    # Si la opcion que se eligio es un numero entonces si entra en este proceso.
    else:
        # Aqui convertimos la opcion de palabra en entero para una mejor implementacion.
        opcion_palabra_entero = int(opcion_palabra)

        # Por si la variable que se escogio es diferente a las opciones indicadas.
        if opcion_palabra_entero <= 0 or opcion_palabra_entero >= 4:
            # Eviamos mensaje.
            socket_cliente.send(opcion_palabra.encode())

            # Cerramos socket y mandamos el mensaje de Salida.
            print("\nLa opcion que se eligio fue 'Salir', Desconectando del Servidor....")
            os.system('pause') # Pausamos la pantalla.
            socket_cliente.close()
            sys.exit()
        
        # Else para opciones elegidas por el Cliente a jugar..
        else:
            # Enviar la opcion de pañlabra a elegir.
            socket_cliente.send(opcion_palabra.encode())
            
            # Inicializacion de las vidas del Juego.
            Vidas = 5

            # Resivimos mensaje del Servidor (la palabra a Buscar en Secreto y la original).
            palabra_encontrar_secreto = socket_cliente.recv(4096).decode()
            socket_cliente.sendall(b"Se necesita la palabra correcta.") # Enviamos un acuse para resivir la palabra final.
            palabra_final = socket_cliente.recv(4096).decode()

            # Impresiones de las palabras resividas (solo para verificar por parte del programador).
            # print(f"La palabra secreta es: {palabra_encontrar_secreto}")
            # print(f"La palabra es: {palabra_final}")
            os.system('cls')

            # Ciclo para empezar a ingresar las letra a encontrar.
            while Vidas > 0:
                # Encabezado para decir la palabra.
                Encabezado(Vidas, palabra_encontrar_secreto)
                ImprimirAhorcado(Vidas)

                # Ingresar la letra a encontrar.
                letra = input("Ingresa la palabra a escoger: ").lower() # .lower() pone la letra en minuscula.

                #Condiciones para solo aceptar letras y no palabras.
                if len(letra) != 1:
                    print("\nPor favor solo Ingresa letras, no palabras ni mas de dos letras.")
                    print("Si ya sabes la palabra, por favor ingresa letra por letra.\n")
                    os.system('pause')
                    os.system('cls')

                else:
                    # Enviamos la letra a encontrar y resivimos del Servidor la nueva palabra secreta.
                    socket_cliente.send(letra.encode())
                    palabra_nueva = socket_cliente.recv(4096).decode()

                    # Aqui se compararan las palabras y se decide si se encontro una letra. 
                    palabra_encontrar_secreto, Vidas = Comparacion(palabra_encontrar_secreto, palabra_nueva, Vidas)

                    # Si ya se tiene que salir porque el jugador perdio o porque gano.
                    if palabra_encontrar_secreto == palabra_final:
                        Vidas = 0
                        Marco_ganador()
                        print(f"\nFilicidades Acabas de Encontrar la Palabra, que era: {palabra_final}\n")
                        os.system('pause') # Pausamos la pantalla.
                    elif Vidas == 0:
                        Marco_perdedor()
                        ImprimirAhorcado(Vidas)
                        print(f"\nLo sentimos te quedastes sin vidas, la palabra era: {palabra_final}\n")
                        os.system('pause') # Pausamos la pantalla.

                    # Borramos pantalla para cada juego.
                    os.system('cls')

                    #Aqui enviamos las vidas al Servidor y tambien termine su proceso.
                    vida_palabra = str(Vidas)
                    socket_cliente.send(vida_palabra.encode())
                    mensaje = socket_cliente.recv(1024)
                    # print(mensaje)