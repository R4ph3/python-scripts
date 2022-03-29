import socket
import subprocess
import sys

objetivo = socket.gethostbyname(input("Dime la IP a analizar guapeton ;) "))
print ("[+] Escaneando objetivo " + objetivo)



try:
    for port in range(1,150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} está abierto".format(port))
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)