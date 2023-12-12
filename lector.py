import subprocess

lista = []
with open('prueba.csv', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        for valor in datos:
            lista.append(valor)

lista = list(filter(None, lista))
#print(lista)
lista_final = lista[0] + lista[1] + lista[2] + lista[3]
#print(lista_final)
resultado = subprocess.run(["powershell", lista_final], capture_output=True, text=True)