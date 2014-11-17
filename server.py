#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            print "El cliente nos manda " + line
            Metodo = line.split(" ")[0]
            if Metodo == "INVITE":
                Answer = "SIP/2.0 100 Trying\r\n\r\n"
                Answer += "SIP/2.0 180 Ring\r\n\r\n"
                Answer += "SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(Answer)
            elif Metodo == "ACK":
                print "Tratamiento ACK"
            elif Metodo == "BYE":
                print "Tratamiento BYE"
            

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", int(sys.argv[2])), EchoHandler)
    print "Listening..."
    serv.serve_forever()
