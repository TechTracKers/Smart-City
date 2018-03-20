
#import smtplib
#import pymysql
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


TRIG=22
ECHO=27

TRIG1=6
ECHO1=5


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)


GPIO.output(TRIG,True)
time.sleep(0.1)
GPIO.output(TRIG,False)

GPIO.output(TRIG1,True)
time.sleep(0.01)
GPIO.output(TRIG1,False)

start1=time.time()
end1=time.time()

start=time.time()
end=time.time()
#print(start)
#print(end)


while GPIO.input(ECHO)==False:
                start=time.time()
while GPIO.input(ECHO)==True:

                end=time.time()


while GPIO.input(ECHO1)==False:
        start1=time.time()
while GPIO.input(ECHO1)==True:
        end1=time.time()


sig_time=end-start
