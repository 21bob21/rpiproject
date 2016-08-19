import RPi.GPIO as GPIO
import random
import time

x = 12
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(x,GPIO.OUT)
GPIO.setup(x,GPIO.OUT)
GPIO.output(x,GPIO.HIGH)

while True:
    randw = random.randint(1,8)
    time.sleep(randw)
    randb = random.randint(1,15)s
    if randb > 8:
	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.LOW)
	time.sleep(0.2)
	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.HIGH)
    else:
    	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.LOW)
	time.sleep(0.2)
	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.HIGH)
	time.sleep(0.16)
	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.LOW)
	time.sleep(0.2)
	GPIO.setup(x,GPIO.OUT)
    	GPIO.output(x,GPIO.HIGH)
