#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.

try:
    """
    Intentamos construir el Cliente
    """
#    SERVER = 'localhost'
    METODO = sys.argv[1].upper()
    INICIO = sys.argv[2]
    NICK = INICIO.split("@")[0]
    SERVER = INICIO.split("@")[1].split(":")[0]
    PORT = int(INICIO.split("@")[1].split(":")[1])
    
    if METODO == "INVITE" or METODO == "BYE":
    
        # Contenido que vamos a enviar
        LINE = METODO + " sip:" + NICK + "@" + SERVER + " SIP/2.0" 
        
        # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        my_socket.connect((SERVER, PORT))
        
        my_socket.send(LINE + '\r\n')
        data = my_socket.recv(1024)
        print "Enviando: " + LINE
        print 'Recibido -- ', data
        print "Terminando socket..."
        
        # Cerramos todo
        my_socket.close()
        print "Fin."

except socket.error:
    print "Error: No server listening at " + SERVER + "port " + str(PORT)
except ValueError:
    print "Usage: python server.py IP port audio_file"
