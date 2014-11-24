#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys


# Cliente UDP simple.
Command_Line = sys.argv
if len(Command_Line) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
Metodo = Command_Line[1].upper()
Direccion = Command_Line[2]

# Dirección IP del servidor.
SERVER = Direccion.split("@")[1].split(":")[0]
PORT = int(Direccion.split("@")[1].split(":")[1])

# Contenido que vamos a enviar
Metodo = Command_Line[1].upper()
Direccion = Command_Line[2]
LINE = Metodo + " sip:" + Direccion.split(":")[0] + " SIP/2.0\r\n\r\n"

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

data_list = []
try:
    print "Enviando: " + LINE
    my_socket.send(LINE)
    data = my_socket.recv(1024)
    print 'Recibido -- ', data
    data_list = data.split(" ")
except socket.error:
    print "Error: No server listening at " + SERVER + " port " + str(PORT)

if len(data_list) == 7:
    if data_list[1] == "100" and data_list[3] == "180":
        if data_list[5] == "200":
            LINE = "ACK sip:" + Direccion.split(":")[0] + " SIP/2.0\r\n\r\n"
            my_socket.send(LINE)

print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
