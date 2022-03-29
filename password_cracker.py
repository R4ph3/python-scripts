import hashlib
from hmac import digest

encontrada = 0
input_hash = input("Dime el hash de la contraseña: ")
diccionario = input("Dime el diccionario que quieres usar para crackear la contraseña")

try:
    pass_file = open(diccionario, "r")
except:
    print("El diccionario " + diccionario + " no ha sido encontrado")

    #Esto es para que busque todas las palabras en el diccionario que ha seleccionado el usuario
for palabra in pass_file:
    palabra_cifrada = palabra.encode("utf-8")
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    solucion = palabra_hasheada.hexdigest()

#Aqui hacemos un if para en caso de que logre una coincidencia
if solucion == input_hash:
    print("Contraseña encontrada! \n La contraseña es " + palabra)
    encontrada = 1



if not encontrada:
    print("Lo siento no se han encontrado coincidencias en el diccionario" + diccionario)


