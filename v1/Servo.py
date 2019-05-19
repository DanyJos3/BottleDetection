import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(11,GPIO.OUT)    #Ponemos el pin 11 como salida
p = GPIO.PWM(11,50)        #Ponemos el pin 11 en modo PWM y enviamos 50 pulsos por segundo

p.start(6)                  #Enviamos un pulso del 6% para girar el servo 90 grados
time.sleep(3)               #pausa de 3 segundos
p.ChangeDutyCycle(11)       #Enviamos un pulso del 11% para girar el servo hasta los 180 grados
time.sleep(0.2)             #pausa de 0.2 segundos

p.stop                      #Detenemos el servo 
GPIO.cleanup()              #Limpiamos los pines GPIO de la Raspberry y cerramos el script
