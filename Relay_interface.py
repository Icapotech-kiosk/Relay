import RPi.GPIO as GPIO
import time

temperature = 37

k1 = 26
k2 = 24
k5 = 21
k6 = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(k1, GPIO.OUT)
GPIO.setup(k2, GPIO.OUT)
GPIO.setup(k5, GPIO.OUT)
GPIO.setup(k6, GPIO.OUT)

GPIO.output(k1, True)
GPIO.output(k2, True)
GPIO.output(k5, True)
GPIO.output(k6, True)


try:
    while True:
        if temperature in range(36,39):
            
            #for door of small UV box
            GPIO.output(k5, False)
            
            #assuming stepper motor speed of 100 rpm
            # 1/4 th revolution for door opening
            # time in secs = (1/400)* 60 = 0.15 sec
            time.sleep(0.15)
            
            GPIO.output(k5, True)
        
            
            #delay for user to put the articles and close the door
            time.sleep(30)
            
            #for door of bigger UV box
            GPIO.output(k6, False)
            
            #assuming stepper motor speed of 100 rpm
            # 1/4 th revolution for door opening
            # time in secs = (1/400)* 60 = 0.15 sec
            time.sleep(0.15)
            
            GPIO.output(k6, True)
        
            
            #delay for user to put the articles and close the door
            time.sleep(30)
            
            #wait for 5 sec to start sanitization
            time.sleep(5)
            #start lamps
            GPIO.output(k1, False)
            GPIO.output(k2, False)
            #run lamps for X = 2 min
            time.sleep(120)
            #stop UV lamps
            GPIO.output(k1,True)
            GPIO.output(k2,True)
            
            #opens the door1 and 2
            GPIO.output(k5, False)
            GPIO.output(k6, False)
            time.sleep(0.15)
            GPIO.output(k5, True)
            GPIO.output(k6, True)
            
            #reset temperature variable
            
            



except KeyboardInterrupt:
    GPIO.cleanup()