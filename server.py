import socket
#Esta libreria sirve para ejecutar varios trozos de codigo a la vez
import threading


PORT = 5050
#Aqui va la IP del server,yo uso la local mia
#server = "127.0.0.1"
#Esta es otra forma de hacerlo,la cual te coge tu IP.
#Es preferible porque asi si se cambia la IP no hay que cambiar el codigo
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
#Esto lo ponemos para que el primer mensaje que se envie siempre al servidor
#sea un mensaje de longitud 64 para representar el numero de bytes
#que tendra el mensaje real
HEADER = 64
FORMAT = "utf-8"
#Mensaje para cuando se salfa del servidor
DISCONNECT_MESSAGE = "!Desconectando"
#Tenemos que abrirnos a conexiones
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)






#Esta es la que va a manejar la comunicacion servidor_cliente
def escuchar_clientes(conex, addr):
    print(f"[NUEVA CONEXION] {addr} conectado. ")

    conexion = True
    while conexion:
        #Aqui codificamos/descodificamos la informacion que envia el usuario al servidor 
        msg_length = conex.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conex.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                conexion = False

            print(f"[{addr}]:{msg}")
            #Esto es para enviar mensajes desde el server al cliente
            conex.send("Mensaje recibido".encode(FORMAT))

    conex.close()

#Aqui vamos a escribir codigo para que el servidor comienza a escuchar
# y a captar conexiones y se las pasara a la funcion de arriba 

def start():
    server.listen()
    print(f"[ESCUCHANDO] El servidor esta escuchando en {SERVER}")
    while True:
        #Esto almacena en addr la IP y puerto de cada nueva conexion al server
        #Y en conex se guardara el objeto de la conexion para reenviarlo
        conex, addr = server.accept()
        thread = threading.Thread(target=escuchar_clientes, args=(conex, addr))
        thread.start()
        print(f"[CONEXIONES ACTIVAS] {threading.activeCount() - 1} ")


print("[+] El servidor esta arrancando... ")
start()