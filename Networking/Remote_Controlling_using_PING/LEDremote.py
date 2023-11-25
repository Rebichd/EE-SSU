#!/usr/bin/env python
#Import porper libraries
import RPi.GPIO as GPIO
import time
import os
import sys
import subprocess
from RPLCD.gpio import CharLCD

#Program asks user how long they would like to observe ping requests.
#For every request the LCD will tell the user and also show the size in bytes

#use BCM pin numberin scheme
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set pin 17 as the output
GPIO.setup(17, GPIO.OUT) #This is the LED 

#Make GPIO 7,8,26,19,13,6,27,11 as output
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

lcd = CharLCD(pin_rs=7, pin_e=8, pins_data=[25,24,23,18], numbering_mode=GPIO.BCM, cols=20, rows=2, auto_linebreaks=False)

#Ask user for ping watch time
watchTime = str(input("Enter amount of time in seconds for PING watch: "))
watchTime = "duration:" + str(watchTime)

print ("Starting PING Watch...")

lcd.clear() #intial clear of lcd

lcd.cursor_pos = (0,0)
lcd.write_string('Starting PING')
lcd.cursor_pos = (1,0)
lcd.write_string('Watch')
#time.sleep(3)

#Command to send linux command output and errors to PIPE
output = subprocess.Popen(['sudo', 'tshark', '-l', '-f', 'icmp', '-a', watchTime], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Loop to continue while still reading output from tshrak command above
while True:	
	pingString = str(output.stdout.readline())
	if pingString.__contains__('(ping) request'):
		lineIndex = pingString.index("ICMP")
		lineIndex2 = pingString.index("Echo")
		length = pingString[(lineIndex+4):lineIndex2].strip()
		byteCount = int(length) - 42
		byteDisplay = str(byteCount)

		#For LCD Display
		lcd.clear()
		lcd.cursor_pos = (0,0)
		lcd.write_string('PING Observed')
		lcd.cursor_pos = (1,0)
		lcd.write_string('Byte Count: ' + byteDisplay)	
		length = 0

	if output.stdout.readline() == b'':
		break

time.sleep(3)
lcd.clear()
lcd.write_string("Times Up..")
time.sleep(2)
lcd.clear()
print ("Times Up...Terminating PING Watch...")
