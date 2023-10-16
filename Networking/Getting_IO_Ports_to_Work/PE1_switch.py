#!/usr/bin/env python
# Import proper libraries
import RPi.GPIO as GPIO
import time

# Use BCM pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set pin 17 as the INPUT
GPIO.setup(17, GPIO.IN)
while True:
	if(GPIO.input(17)):
		print("Button Pressed")
		#delay of one second
		time.sleep(1)
		#traps user in loop while button is pressed
		while GPIO.input(17):
			time.sleep(1)
		#displayed upon button release
		if(not GPIO.input(17)):
			print("Button Released")
			time.sleep(1)
