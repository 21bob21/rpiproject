import time
import RPi.GPIO as GPIO
 
# Assign the hardware PWM pin and name it
led = 10
RUNNING = True
 
# Configure the GPIO to BCM and set it to output mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setwarnings(False)
 
# Set PWM
pwm = GPIO.PWM(led, 100)
 
print "Pulsating LED. Press CTRL + C to quit"
 
# Main loop
try:
    while RUNNING:
	GPIO.setwarnings(False)
    # Start PWM with the LED off
        pwm.start(0)
        # Slowly ramp up the brightness of the LED
	up = 0
        for x in range (0,100):
            pwm.ChangeDutyCycle(up)
            # Pause to slow ramping
            time.sleep(0.01)
            up = up + 1
        down = 99
        for x in range (0,99):
            pwm.ChangeDutyCycle(down)
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
    pwm.stop()
    GPIO.cleanup()
