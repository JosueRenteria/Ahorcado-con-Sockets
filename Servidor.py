#Importar la libreria de los sockets.
import socket
from sqlite3 import connect

HOST = "127.0.0.1" # Direccion del loopback
PORT = 65123       # > 1023 (Puerto de Escucha)

# El bloque with es para abrir y cerrar el sockets. socket(IP, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Asociar el socket y poner en modo escucha.
    s.bind((HOST, PORT))
    s.listen()

    # Aceptar conecciones entrantes (conn = socket del cliente, addr = direccion del socket entrante).
    conn, addr = s.accept()

    #Enviar un mensaje al servidor.
    with conn:
        #Muestra la direccion IP del cliente.
        print(f"Conectado a {addr}")
        while True:
            #Aqui el cliente va a enviar algo.
            data = conn.recv(1024)

            #Ver si el usuario envio algo.
            if not data:
                break
            else:
                #Envia algo al Servidor.
                conn.sendall(data) #conn es es el socket cliente.
        
        #Cerramos la conecion de Nuestro Cliente.
        print(f"Desconectando a {addr}")
        conn.close()