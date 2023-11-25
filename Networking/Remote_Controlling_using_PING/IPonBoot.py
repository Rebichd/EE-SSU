#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os
import subprocess
from RPLCD.gpio import CharLCD

#Set the Mode for the pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Make GPIO 7,8,25,24,23,18,27,22 as outputs
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#Setup LCD
lcd = CharLCD(pin_rs=7, pin_e=8, pins_data=[25,24,23,18], numbering_mode=GPIO.BCM, cols=20, rows=2, auto_linebreaks=False)

counter = 0
timeLimit = 120
IPflag = False

try:
	lcd.clear() #intial clear of lcd
	#This is for the scroll across the screen
	for i in range (17):
		lcd.clear()
		lcd.cursor_pos = (0,i)
		lcd.write_string('IP Address:')
		time.sleep(.5)

	#Loop throughs until the IP address is found or the time limit has been reached
	while True:
		lcd.cursor_pos = (0,2)
		lcd.write_string('IP Address:')
		time.sleep(1)

		output_ifconfig = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE)
		output_grep1 = subprocess.Popen(["grep", "inet"], stdin=output_ifconfig.stdout, stdout=subprocess.PIPE)
		output_grep2 = subprocess.Popen(["grep", "broadcast"], stdin=output_grep1.stdout, stdout=subprocess.PIPE)

		lineIP = str(output_grep2.stdout.readlines())
		if "inet" not in lineIP:
			print ("No IP Found")
			IPflag = False
		else:
			lineIndex = lineIP.index("inet")
			lineIndex2 = lineIP.index("netmask")
			myIPaddress = lineIP[(lineIndex+4):lineIndex2].strip()

			lcd.cursor_pos = (1,1)
			lcd.write_string(myIPaddress)
			IPflag = True
			break

		counter += 1
		if counter == timeLimit:
			print ("Time Limit Reached...")
			print ("Terminating IP display")
			if not IPflag:
				lcd.cursor_pos = (1,0)
				lcd.write_string("NO IP FOUND")
			break
		time.sleep(1)
	#Leaves the IP address up for an additional 10 seconds after it has been found 
	time.sleep(10)
	lcd.clear()

except KeyboardInterrupt:
	lcd.clear()
	GPIO.cleanup()
