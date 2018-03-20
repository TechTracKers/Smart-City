
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
sig_time1=end1-start1
distance=str(sig_time*17150)
print(distance)
distance1=sig_time1*17150


db=pymysql.connect('localhost','naman','mayank7857','hello')
cursor=db.cursor()
sql1="DELETE FROM kumar"
cursor.execute(sql1)
sql="INSERT INTO kumar(length)values('"+distance+"')"
cursor.execute(sql)
db.commit()

cursor.execute(sql)
sql2="select * from kumar"
cursor.execute(sql2)
data=cursor.fetchone()
print(data)
data1=float(data[0])
print(data1)
print(data1)


if data1>12:
        print("parking space is not empty")
else:
        print("parking space is empty empty")
db.close()

print(distance) 
#print(distance1)


GPIO.cleanup()




