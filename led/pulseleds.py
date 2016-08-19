import time
import RPi.GPIO as GPIO
 
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
RUNNING = True

try:
    while RUNNING:
	GPIO.setwarnings(False)
    # Start PWM with the LED off
        RED.start(0)
	BLUE.start(0)
	GREEN.start(0)
        # Slowly ramp up the brightness of the LED
	up = 0
        for x in range (0,100):
            RED.ChangeDutyCycle(up)
	    GREEN.ChangeDutyCycle(up)
	    BLUE.ChangeDutyCycle(up)
            # Pause to slow ramping
            time.sleep(0.02)
            up = up + 1
        down = 99
        for x in range (0,99):
            RED.ChangeDutyCycle(down)
	    GREEN.ChangeDutyCycle(down)
	    BLUE.ChangeDutyCycle(down)
            # Pause to slow ramping
            time.sleep(0.01)
            down = down - 1
 
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
