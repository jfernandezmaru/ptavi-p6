#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os


try:
    """
    Intentamos construir el Servidor
    """
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    os.access(sys.argv[3], os.F_OK)
    AUDIO = sys.argv[3]

except ValueError:
    print "Usage: python server.py IP port audio_file"

print "Listening..."

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("SIP/2.0 400 BAD REQUEST" + '\r\n')
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print "El cliente nos manda " + line
            lista = line.split(" ")

            if lista[0] == "INVITE":

               self.wfile.write("SIP/2.0 100 BAD TRYING" + '\r\n' + "SIP/2.0 180 RING" + '\r\n' + "SIP/2.0 200 OK" + '\r\n' + '\r\n')
            
#           elif lista[0] == "ACK":
            
#           elif lista[0] == "BYE":

            else:
                self.wfile.write("SIP/2.0 405 Method Not Allowed" '\r\n')

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":

    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer((SERVER, PORT), EchoHandler)
    serv.serve_forever()
    
    
    
    
    
    
    
    
