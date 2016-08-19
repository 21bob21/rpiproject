import RPi.GPIO as GPIO
import time

x = 12
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(x,GPIO.OUT)

while True:
    time.sleep(1)
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,GPIO.LOW)
    time.sleep(1)
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,GPIO.HIGH)
