#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
#import netifaces as ni
from RPLCD.gpio import CharLCD

#Set the Mode for the pins
GPIO.setmode(GPIO.BCM)

#Make GPIO 7,8,26,19,13,6,27,11 as output
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

lcd = CharLCD(pin_rs=7, pin_e=8, pins_data=[25,24,23,18], numbering_mode=GPIO.BCM, cols=20, rows=1, auto_linebreaks=False)

#ni.ifaddress('wlan0')
ip = 'Hello World' #ni.ifaddress('wlan0')[ni.AF_INET][0]['addr']

try:
        i = 0
        while True:
                lcd.clear()
                lcd.cursor_pos = (0,0)
                lcd.write_string(ip)
                time.sleep(1)
                #ni.ifaddress('wlan0')
                ip = 'Hello World' #ni.ifaddress('wlan0')[ni.AF_INET][0]['addr']
                break
except KeyboardInterrupt:
        lcd.clear()
        GPIO.cleanup()
