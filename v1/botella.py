import imutils
import cv2
import numpy as np
import RPi.GPIO as GPIO    
import time 
import os
#OpenCV es un framework
#Importamos todas las librerias que vamos a utilizar.
#Tienen que estar previamente instaladas

cap = cv2.VideoCapture(0)  #con esto se prende la camara

f=0
flag=False
while(1):  #while infinito 

        ret, frame = cap.read() #Para obtener los frames 
        frame = imutils.resize(frame,400 )
        if not ret:
                break
       

        cascade_bote = "cascade3.xml" #carga la plantilla de haarcascade (Datos de botellas)
	
        botellaCascade = cv2.CascadeClassifier(cascade_bote) #llamamos a la funcion clasificador de cascada de OpenCV
       
        filtro = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convertir la imagen en B/N
#        cv2.imshow("blanco y negro",filtro) #Si se desea mostrar la imagen captura a blanco y negro
        
       

#Detecta objetos de diferentes tamaños en la imagen de entrada. Los objetos detectados se devuelven como una lista de rectángulos.
#Para detectar lo que exista en el xml tomando en cuenta la escala de grises

	botella = botellaCascade.detectMultiScale(  filtro,
                scaleFactor = 1.1,
                minNeighbors =5,
                minSize= (34,15),
                flags = cv2.CASCADE_SCALE_IMAGE)


        for (x, y, w, h) in botella:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255,255 ), 2)  #Para dibujar un rectangulo sobre la imagen identificada



	#Aqui empieza la programacion para abrir en servo en caso de haber identificado el objeto
	#Tenemos 3 variables
	#1)botella
	#2)bandera o flag
	#3)un contador
	# La tapa solo se abre si la bandera es verdadera,y se identifica algo en botella por mas de 5 segundos 
	
        if len(botella) >= 1 and f >= 5 and flag == True: 
                print("Abrir")
		
                os.system("python Servo.py") # Aqui mandamos a ejecutar el script que mueve el servo.
                flag=False
                f=0
 
        elif len(botella) >= 1  and flag == False:
                print("Bandera True")
                flag = True
                f=0
               
        elif len(botella) == 0 and flag == True:
                flag == False
                f=0
                
        elif flag == True:
                f = f+1
                      
        print(f)
        
        cv2.imshow("Detector de Botellas", frame) #Para mostrar la imagen que se esta viendo por la camara.
        if cv2.waitKey(1) & 0xFF == ord('q'): #Si se preciona Crtl + c o la letra q  se detiene el ciclo while
                break
       
#cerrar la camara y destruir sistema

cap.release()
cv2.destroyAllWindows()
