#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Practica 6 Javier Fernandez Marugan  PTAVI
"""
Clase (y programa principal) para un servidor de eco en UDP
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
                check1 = line.find("sip:")
                check2 = line.find("@")
                check3 = line.find("SIP")
                check4 = line.find("/2.0")
                if check1 >= 0 and check2 >= 0 and check3 >= 0 and check4 >= 0:
                    lista = line.split(" ")
                    Metodo = lista[0]
                    IP_Cliente = str(self.client_address[0])          
                    if Metodo == "INVITE":

                        self.wfile.write("SIP/2.0 100 Trying\r\n\r\n" + "SIP/"\
                        + "2.0 180 Ringing\r\n\r\n" + "SIP/2.0 200 OK\r\n\r\n")
                    elif Metodo == "ACK":
                    
                        os.system("chmod 777 mp32rtp")
                        Packet = "./mp32rtp -i " + IP_Cliente + \
                         " -p 23032 < " + AUDIO
                        os.system(Packet)
                    elif Metodo == "BYE":
                    
                        self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                        print "Cliente " + IP_Cliente + " cierra la conexión"
                    else:

                        self.wfile.write("SIP/2.0 405"\
                         + " Method Not Allowed\r\n\r\n")
                else:
                    
                    self.wfile.write("SIP/2.0 400 Bad Request\r\n")
            break

if __name__ == "__main__":

    try:

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
