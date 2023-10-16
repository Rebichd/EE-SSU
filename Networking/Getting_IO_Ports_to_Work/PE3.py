#!/usr/bin/env python
#Import porper libraries
import RPi.GPIO as GPIO
import time
import os
import sys
import subprocess

#Program asks user how long they would like to observe ping requests.
#For every request the terminal will tell the user and also blink an LED

#use BCM pin numberin scheme
GPIO.setmode(GPIO.BCM)

#Set pin 17 as the output
GPIO.setup(17, GPIO.OUT)

#Ask user for ping watch time
watchTime = str(input("Enter amount of time in seconds for PING watch: "))
watchTime = "duration:" + str(watchTime)

print ("Starting PING Watch...")

#Command to send linux command output and errors to PIPE
output = subprocess.Popen(['sudo', 'tshark', '-l', '-f', 'icmp', '-a', watchTime], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Loop to continue while still reading output from tshrak command above
while True:
	if str(output.stdout.readline()).__contains__('(ping) request'):
		print ("ping request observed")
		#Turn on LED for  seconds
		GPIO.output(17, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(17, GPIO.LOW)
	if output.stdout.readline() == b'':
		break

time.sleep(1)

print ("Times Up...Terminating PING Watch...")
GPIO.output(17, GPIO.LOW)
GPIO.setup(17, GPIO.IN)
