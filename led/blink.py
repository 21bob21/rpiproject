import random
import time
from gpiozero import LED

led = LED(12)
led.on()

while True:
	randw = random.randint(1,8)
	time.sleep(randw)
	randb = random.randint(1,15)
	if randb > 8:
		led.off()
		time.sleep(0.2)
		led.on()
	else:
		led.off()
		time.sleep(0.2)
		led.on()
		time.sleep(0.16)
		led.off()
		time.sleep(0.2)
		led.on()

