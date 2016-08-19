import random, time
import RPi.GPIO as GPIO
import math

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
	print "changing from " + str(r) + " to " + str(redprev)
	changered(r,speed)
	changegreen(g,speed)
	changeblue(b,speed)
	time.sleep(2)

def changered(red,speed):
	global redprev
	if(red < redprev):
		print "redup"
		up = redprev - red
		print "the difference is" + str(up)
		for x in range (redprev,red):
	            RED.ChangeDutyCycle(up)
	            time.sleep(speed)
            	    up = up + 1
	else:
		print "reddown"
	        down = red - redprev
		print "the difference is" + str(down)
	        for x in range (red,redprev):
	            RED.ChangeDutyCycle(down)
	            time.sleep(speed)
            	    down = down - 1
	redprev = red
	print redprev
	print red

def changeblue(blue,speed):
	global blueprev
	if(blue > blueprev):
		up = blue - blueprev
		for x in range (blueprev,blue):
	            BLUE.ChangeDutyCycle(up)
	            time.sleep(speed)
            	    up = up + 1
		    print up
	else:
	        down = blueprev - blue
	        for x in range (blue,blueprev):
	            BLUE.ChangeDutyCycle(down)
	            time.sleep(speed)
            	    down = down - 1
		    print down
	blueprev = blue

def changegreen(green,speed):
	global greenprev
	if(green > greenprev):
		up = green - greenprev
		for x in range (greenprev,green):
	            GREEN.ChangeDutyCycle(up)
	            time.sleep(speed)
            	    up = up + 1
	else:
	        down = greenprev - green
	        for x in range (green,greenprev):
	            GREEN.ChangeDutyCycle(down)
	            time.sleep(speed)
            	    down = down - 1
	greenprev = green


RUNNING = True

try:
    while RUNNING:
	GPIO.setwarnings(False)
        r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	changeto(r,g,b,0.02)
 
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    RED.stop()
    BLUE.stop()
    GREEN.stop()
    GPIO.cleanup()