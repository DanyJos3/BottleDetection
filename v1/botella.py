import imutils
import cv2
import numpy as np
import RPi.GPIO as GPIO    
import time 
import os


cap = cv2.VideoCapture(0)

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
#        cv2.imshow("blanco y negro",filtro)
        
       

        botella = botellaCascade.detectMultiScale(  filtro,
                scaleFactor = 1.1,
                minNeighbors =5,
                minSize= (34,15),
                flags = cv2.CASCADE_SCALE_IMAGE)


        for (x, y, w, h) in botella:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255,255 ), 2)



        if len(botella) >= 1 and f >= 5 and flag == True:
                print("Abrir")
		
                os.system("python Servo.py")
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
        
        cv2.imshow("Detector de Botellas", frame) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
       
p.stop
GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()
