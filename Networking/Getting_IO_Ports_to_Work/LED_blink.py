#!/usr/bin/env python
# Import proper libraries
import RPi.GPIO as GPIO
import time

# Use BCM pin numbering scheme
GPIO.setmode(GPIO.BCM)

# Set pin 17 as the output
GPIO.setup(17, GPIO.OUT)

# blink GPIO17 50 times
for i in range(0,50):
	GPIO.output (17, GPIO.HIGH)
	time.sleep (0.5)
	GPIO.output (17, GPIO.LOW)
	time.sleep (0.5)
