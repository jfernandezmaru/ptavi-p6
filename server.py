#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys
import os


class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion") #no hay que imprimirlo
        line = self.rfile.read()
        line2 = line.split(" ")
        if line2[0] == "INVITE":
            self.wfile.write("SIP/2.0 100 TRYING" + '\r\n\r\n' +
            "SIP/2.0 180 RING" + '\r\n\r\n' + "SIP/2.0 200 OK" + '\r\n\r\n')
        elif line2[0] == "BYE":
            self.wfile.write("SIP/2.0 200 OK" + '\r\n\r\n')
        elif line2[0] == "ACK":
            self.wfile.write("SIP/2.0 200 OK" + '\r\n\r\n')
        elif line2[0] != "INVITE" and line2[0] != "BYE" and line2[0] != "ACK":
            self.wfile.write("SIP/2.0 405 Method Not Allowed")
        else
            self.wfile.write("SIP/2.0 400 Bad Request")
        # Leyendo línea a línea lo que nos envía el cliente
        print "El cliente nos manda " + line
        while 1:
            # Si no hay más líneas salimos del bucle infinito
            print "hola"
            if not line:
                break

if __name__ == "__main__":
    # Comprobamos que introducimos el numero correcto de parametros
    if len(sys.argv) != 4:
        sys.exit("Usage: python server.py IP port audio_file")

    # Creamos servidor de eco y escuchamos
    IP = sys.argv[1]
    PUERTO = int(sys.argv[2])
    FICH_AUDIO = sys.argv[3]
    serv = SocketServer.UDPServer(("", PUERTO), EchoHandler)
    print "Listening..."
    serv.serve_forever()
