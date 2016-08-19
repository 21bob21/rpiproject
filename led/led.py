import RPi.GPIO as GPIO
import time

def pwmsetup(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pin,GPIO.OUT)
	global pwm
	pwm = GPIO.PWM(pin, 100)

pwmsetup(12)

RUNNING = True

try:
    while RUNNING:
	GPIO.setwarnings(False)
	pwm.start(0)
    # Start PWM with the LED off
	pwm.ChangeDutyCycle(0)
	time.sleep(0.5)
 	pwm.ChangeDutyCycle(100)
	time.sleep(0.5)
# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
    print "\Quitting"
 
# Actions under 'finally' will always be called
finally:
    # Stop and finish cleanly so the pins
    # are available to be used again
    pwm.stop()
    GPIO.cleanup()