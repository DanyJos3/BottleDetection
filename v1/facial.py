import imutils
import cv2
#import pygame
import numpy as np
#import RPi.GPIO as GPIO    
#import time 


#import sys

#GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
#GPIO.setup(31,GPIO.OUT)    #Ponemos el pin 21 como salida
#p = GPIO.PWM(31,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
#p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo
cap = cv2.VideoCapture(0)

#pygame.mixer.init()
#pygame.mixer.music.load("link.mp3")

f=0
flag=False
while(1):

        ret, frame = cap.read()
        frame = imutils.resize(frame,400 )
        if not ret:
                break
        

       
        cascade_bote = "cascade3.xml"
        botellaCascade = cv2.CascadeClassifier(cascade_bote)

       
        filtro = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("blanco y negro",filtro)
        
       

        botella = botellaCascade.detectMultiScale(  filtro,
                scaleFactor = 1.1,
                minNeighbors =5,
                minSize= (34,15),
                flags = cv2.CASCADE_SCALE_IMAGE)

       

        for (x, y, w, h) in botella:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255,255 ), 2)

        
 
        if len(botella) == 0 and f >= 25 and flag == True:
                #pygame.mixer.music.pause()
                flag = False
                f=0
               
        elif len(botella) >= 1 and flag == False:              
                #pygame.mixer.music.play(-1)
                flag =True
                
        elif flag == True:
                f = f+1
                      
        print(f)
        cv2.imshow("detector", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
       
cap.release()
cv2.destroyAllWindows()
