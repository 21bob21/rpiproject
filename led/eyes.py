import rgb
import time
import random
import thread

rgb.setup(11,9,10,100)
global RUNNING
RUNNING  = True
global mode
mode = 0

def changemode(m):
	global mode
	mode = m

def default():
	rgb.changeto(255,255,255,0.008)
	time.sleep(1)
	rgb.changeto(55,55,55,0.008	)
	time.sleep(1)

def speaking():
	rgb.changeto(0,0,255,0.004)
	time.sleep(0.7)
	rgb.changeto(0,255,0,0.004)
	time.sleep(0.7)
	rgb.changeto(255,0,0,0.004)
	time.sleep(0.7)

def listening():
	print "listening"

def loading():
	print "loading"

def face():
	print "face spotted"

modes = {
	0:default,
	1:speaking,
	2:listening,
	3:loading,
	4:face
}

def modechange():
	global RUNNING
	try:
	    while RUNNING:
		global mode
		modes[mode]()
		time.sleep(0.5)
	 
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

thread.start_new_thread(modechange,())