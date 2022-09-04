#Importar la libreria de los sockets.
import socket

HOST = "127.0.0.1" # Direccion del servidor a conectar.
PORT = 65123       # Puerto de Envio para entrar.

# El bloque with es para abrir y cerrar el sockets. socket(IP, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Hacer la conneccion con el Servidor (Aqui deja de estar bloqueado el Servidor).
    s.connect((HOST, PORT))

    #Va a enviar un String en binarioo (b = binario y lo convierte).
    print
    s.sendall(b"Hola Mundo")

    #El cliente resivira lo que le envia el servidor.
    data = s.recv(1024)

print("Recivido.", repr(data))