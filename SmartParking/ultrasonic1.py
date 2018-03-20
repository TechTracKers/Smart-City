
#import pymysql
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG=23
ECHO=24


GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


GPIO.output(TRIG,True)
time.sleep(0.0001)
GPIO.output(TRIG,False)

start=time.time()
end=time.time()



#print(start)
#print(end)


while GPIO.input(ECHO) == False:
                start=time.time()
while GPIO.input(ECHO) == True:

                end=time.time()

sig_time=end-start
distance=(sig_time*17150)
print(distance)
if distance<8:
        print("Slot 1 is full")
if distance>8:
        print("Slot 1 is empty")
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
TRIG1=18
ECHO1=25


GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)

GPIO.output(TRIG1,True)
time.sleep(0.001)
GPIO.output(TRIG1,False)
start1=time.time()
end1=time.time()
while GPIO.input(ECHO1)==False:
        start1=time.time()
while GPIO.input(ECHO1)==True:
        end1=time.time()

sig_time1=end1-start1
distance1=(sig_time1*17150)
print(distance)
print(distance1)
#if(distance<8):
#       print("Slot 1 is full")
#if(distance>8):
#       print("Slot 1 is empty")
if distance1<8:
        print("Slot 2 is full")
if distance1>8:
        print("Slot 2 is empty")
GPIO.cleanup()
#db=pymysql.connect('localhost','naman','mayank7857','rajasthan1')
#cursor=db.cursor()
#sql1="DELETE FROM god1"
#cursor.execute(sql1)
#sql="INSERT INTO god1(sensor1,sensor2) values('"+distance+"','"+distance1+"')"
#cursor.execute(sql)
#db.commit()
#sql2="select * from god1"
#cursor.execute(sql2)
#data=cursor.fetchone()
#print(data)
#db.close#b=list(a)
#db.close()

