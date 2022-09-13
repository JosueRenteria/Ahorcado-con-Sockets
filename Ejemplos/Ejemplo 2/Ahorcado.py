# Declaramos las librerias del programa.
from socket import *
import sys # Terminar la ejecucion del codigo.
import os
import random

# Declaramos las listas de las palabras
palabras_cortas = ['Hola', 'Adios', 'Dia']
palabras_medianas = ['Paracaidas', 'Paracetamol']
palabras_largas = ['Trinidad y Tobago']


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

def remplazar_simbolo(palabra, secreto, simbolo):
    cantidad = palabra.count(simbolo)
    inicio = 0

    for i in range(cantidad):
        pos = palabra.find(simbolo, inicio)
        secreto = secreto[:pos] + simbolo +secreto[pos+1:]
        inicio = pos + 1
    
    return secreto
