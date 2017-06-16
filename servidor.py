#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      tcpserver.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#
import socket
from socket import socket, error
from threading import Thread


class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """

    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data == 's' or input_data == 'S':
                    msg = '1'
                else:
                    msg = '0'

                self.conn.send(msg)

def main():
    s = socket()

    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 35000))
    s.listen(0)

    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        c.start()
        print("%s:%d se ha conectado." % addr)


if __name__ == "__main__":
    main()