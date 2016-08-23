import rgb
import time
import random
import thread
from eyemode import changemode

rgb.setup(11,9,10,100)
global RUNNING
RUNNING  = True
changemode(0)

def default():
	rgb.changeto(0,255,255,0.002)

def speaking():
	rgb.changeto(255,20,0,0.008)
	time.sleep(0.2)
	rgb.changeto(255,120,0,0.008)
	time.sleep(0.2)

def listening():
	rgb.changeto(255,0,255,0.007)
	time.sleep(0.6)
	rgb.changeto(255,180,255,0.004)
	time.sleep(0.1)

def loading():
	rgb.changeto(255,255,0,0.002)
	time.sleep(0.2)
	rgb.changeto(0,0,0,0.004)
	time.sleep(0.008)

def face():
	global x
	x = 2
	print "face spotted"
	rgb.changeto(0,255,0,0.008)
	time.sleep(0.001)
	rgb.changeto(0,255,255,0.008)
	

modes = {
	0:default,
	1:speaking,
	2:listening,
	3:loading
}

try:
	    while RUNNING:
		try:
			file = open("mode.txt","r")
			mode = int(file.read())
			file.close
		except ValueError:
			if mode != 4:
				modes[mode]()
				f = 1
			else:				
				if f == 1:
					face()
		else:
			if mode != 4:
				modes[mode]()
				f = 1
			else:				
				if f == 1:
					face()
		print f		
	# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
	    RUNNING = False
	    print "/Quitting"
	 
	# Actions under 'finally' will always be called
finally:
	    # Stop and finish cleanly so the pins
	    # are available to be used again
	    rgb.RED.stop()
	    rgb.BLUE.stop()
	    rgb.GREEN.stop()
    	    rgb.GPIO.cleanup()