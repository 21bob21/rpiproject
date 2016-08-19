import random, time
import RPi.GPIO as GPIO
import math
import thread

def rgbsetup(rpin,gpin,bpin,freq):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(rpin, GPIO.OUT)
	GPIO.setup(gpin, GPIO.OUT)
	GPIO.setup(bpin, GPIO.OUT)
	global RED
	RED = GPIO.PWM(rpin, freq)
	RED.start(0)
	global GREEN
	GREEN = GPIO.PWM(gpin, freq)
	GREEN.start(0)
	global BLUE
	BLUE = GPIO.PWM(bpin, freq)
	BLUE.start(0)
	global frequency
	frequency = freq

rgbsetup(11,9,10,100)

global redprev
redprev = 0
global greenprev
greenprev = 0
global blueprev
blueprev = 0

def changeto(redv,greenv,bluev,speed):
	global redprev
	global greenprev
	global blueprev
	GPIO.setwarnings(False)
	r = int(round(redv/2.55))
	g = int(round(greenv/2.55))
	b = int(round(bluev/2.55))
	print str(r) + " " + str(g) + " " + str(b)
	thread.start_new_thread(changered,(r,speed))
	thread.start_new_thread(changegreen,(g,speed))
	thread.start_new_thread(changeblue,(b,speed))
	time.sleep(2)

def changered(red,speed):
	global redprev
	if(red > redprev):
		for x in range (redprev,red):
	            RED.ChangeDutyCycle(x)
	            time.sleep(speed)
	else:
	        down = redprev - red
	        for x in range (0,down):
	            RED.ChangeDutyCycle(redprev - x )
	            time.sleep(speed)
	redprev = red

def changegreen(green,speed):
	global greenprev
	if(green > greenprev):
		for x in range (greenprev,green):
	            GREEN.ChangeDutyCycle(x)
	            time.sleep(speed)
	else:
	        down = greenprev - green
	        for x in range (0,down):
	            GREEN.ChangeDutyCycle(greenprev - x )
	            time.sleep(speed)
	greenprev = green

def changeblue(blue,speed):
	global blueprev
	if(blue > blueprev):
		for x in range (blueprev,blue):
	            BLUE.ChangeDutyCycle(x)
	            time.sleep(speed)
	else:
	        down = blueprev - blue
	        for x in range (0,down):
	            BLUE.ChangeDutyCycle(blueprev - x )
	            time.sleep(speed)
	blueprev = blue




RUNNING = True

try:
    while RUNNING:
	GPIO.setwarnings(False)
        r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	changeto(r,g,b,0.01)
 
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "/Quitting"
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    RED.stop()
    BLUE.stop()
    GREEN.stop()
    GPIO.cleanup()