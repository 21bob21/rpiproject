from gpiozero import Button
import os

button = Button(5)
button.wait_for_press()
os.system("sudo shutdown -h now")
