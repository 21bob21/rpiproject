import random, time
import RPi.GPIO as GPIO

# Set GPIO to Broadcom system and set RGB Pin numbers
RUNNING = True
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
 
# Define a simple function to turn on the LED colors
def color(R, G, B, on_time):
    # Color brightness range is 0-100%
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)
 
    # Turn all LEDs off after on_time seconds
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)
 
print("Light It Up!")
print("Press CTRL + C to quit.\n")
print(" R  G  B\n---------")
 
# Main loop
try:
    while RUNNING:
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    print (x,y,z)
                    # Slowly ramp up power percentage of each active color
                    for i in range(0,101):
                        color((x*i),(y*i),(z*i), .02)
 
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
# regardless of what stopped the program
finally:
    # Stop and cleanup so the pins
    # are available to be used again
    GPIO.cleanup()