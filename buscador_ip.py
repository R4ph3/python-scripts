from nis import match
import re


entrada_ip = input("Dime la ip: ")
contador = 0

patron = "^\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$"
coincidencia = re.match(patron,entrada_ip)
if (match):
    campo = entrada_ip.split(".")
    for i in range(0,len(campo)):
        if (int(campo[i]) < 256):
            contador +=1
        else:
            contador = 0
if (contador == 4):
    print("La ip es valida")
else:
    print("No ha habido respuesta")
