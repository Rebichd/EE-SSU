#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import subprocess

#Use BCM pin numbering scheme
GPIO.setmode(GPIO.BCM)

#Set pin 17 as the output
GPIO.setup(17, GPIO.OUT)

#Used to display IP status to Users along with LED
ipflagNew = False
ipflagOld = False

#Will time out after approx. "timeOutVal" seconds
timeOutVal = 10
timeOutCount = 0

print ("Valid IP Detection Started...")
while True:
	output_ifconfig = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
	output_grep1 = subprocess.Popen(["grep", "inet"], stdin=output_ifconfig.stdout, stdout=subprocess.PIPE)
	output_grep2 = subprocess.Popen(["grep", "broadcast"], stdin=output_grep1.stdout, stdout=subprocess.PIPE)

	line = output_grep2.stdout.readlines()
	if not line:
		if timeOutCount == 0:
			print ("No IP Detected!")
		ipflagNew = False
		if ipflagNew != ipflagOld:
			ipflagOld = False
			print ("No IP Detected!")
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.25)
		GPIO.output(17, GPIO.LOW)
		time.sleep(0.25)
	else:
		ipflagNew = True
		if ipflagNew != ipflagOld:
			ipflagOld = True
			print ("IP Detected!")
	if timeOutCount == timeOutVal:
		print ("Valid IP Detection Complete...")
		break
	timeOutCount = timeOutCount + 1
	time.sleep(1)

GPIO.output(17, GPIO.LOW)
GPIO.setup(17, GPIO.IN)
