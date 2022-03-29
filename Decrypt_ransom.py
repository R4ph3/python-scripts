from cryptography.fernet import Fernet
import os


#En esta funcion vamos a cargar la llave

def cargar_llave():
    return open("key.key", "rb").read()



#Aqui vamos a desencriptar el ransom

def desencriptar(items, key):
    x = Fernet(key)
    for item in items:
        with open(item, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = x.decrypt(encrypted_data)
        with open(item, "wb") as file:
            file.write(decrypted_data)




if __name__ == "__main__":
    path_to_encrypt = "/home/remnux/Desktop/piton/archivos_ransomware"
    os.remove(path_to_encrypt + "/" + "readme.txt")

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + "/" + item for item in items]
    key = cargar_llave()
    desencriptar(full_path, key)