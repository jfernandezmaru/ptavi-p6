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
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if not line:
                self.wfile.write("SIP/2.0 400 Bad Request\r\n")
                break
            else:
                print "El cliente nos manda " + line
                lista = line.split(" ")
                Metodo = lista[0]
                IP_Cliente = lista[1].split("@")[1]

                if Metodo == "INVITE":
                    self.wfile.write("SIP/2.0 100 Trying\r\n\r\n" + "SIP/2.0 180 Ringing\r\n\r\n" + "SIP/2.0 200 OK\r\n\r\n")

                elif Metodo == "ACK":
                    Packet = "./mp32rtp -i 127.0.0.1 -p 23032 < " + AUDIO
                    os.system(Packet)

                elif Metodo == "BYE":
                    self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                    print "El cliente " + IP_Cliente + " abandona la conexión"
                else:
                    self.wfile.write("SIP/2.0 405 Method Not Allowed\r\n\r\n")
            break

if __name__ == "__main__":

    try:
        """
        Intentamos construir el Servidor
        """
        SERVER = sys.argv[1]
        PORT = int(sys.argv[2])
        if not os.access(sys.argv[3], os.F_OK):
            print "Usage: python server.py IP port audio_file"
            sys.exit()
        AUDIO = sys.argv[3]

    except ValueError:
        print "Usage: python server.py IP port audio_file"

    print "Listening..."

    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer((SERVER, PORT), EchoHandler)
    serv.serve_forever()

