from http import client
import socket
from traceback import print_tb

PORT = 5050
HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!Desconectando"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cliente.send(send_length)
    cliente.send(message)
    print(cliente.recv(2048).decode(FORMAT))
send("Hola mundo")
input()
send("hay conexion")

send(DISCONNECT_MESSAGE)